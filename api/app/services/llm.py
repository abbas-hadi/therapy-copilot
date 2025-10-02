import os
import threading
import json
from app.models.db import save_analysis
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')

PROMPT = """
You are a clinical assistant. Given a transcript, return JSON with fields: distortions (list of {type, excerpt, confidence}), summary (list), risk_flags (list).
"""

def call_llm(transcript: str) -> dict:
    resp = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{'role': 'user', 'content': PROMPT + '\n\nTRANSCRIPT:\n' + transcript}],
        temperature=0.0,
        max_tokens=1000
    )
    text = resp.choices[0].message.content
    # naive parse - in prod use robust JSON extraction and schema validation
    start = text.find('{')
    end = text.rfind('}')
    if start==-1 or end==-1:
        return {'error': 'parse_failed', 'raw': text}
    return json.loads(text[start:end+1])

def analyze_transcript_async(session_id: int, transcript: str):
    def job():
        try:
            result = call_llm(transcript)
            save_analysis(session_id, result)
        except Exception as e:
            save_analysis(session_id, {'error': str(e)})
    thread = threading.Thread(target=job)
    thread.start()
    return True
