import time
import json
from app.services.llm import call_llm
# Demo worker: scans sessions_demo.json and processes entries that lack analyses.
SESSIONS_FILE = 'sessions_demo.json'
ANALYSES_FILE = 'analyses.json'

def load_sessions():
    try:
        with open(SESSIONS_FILE, 'r') as f:
            lines = f.readlines()
        entries = [json.loads(l) for l in lines]
        return entries
    except FileNotFoundError:
        return []

def processed_ids():
    try:
        with open(ANALYSES_FILE, 'r') as f:
            lines = f.readlines()
        entries = [json.loads(l) for l in lines]
        return set(e['session_id'] for e in entries)
    except FileNotFoundError:
        return set()

def main():
    while True:
        sessions = load_sessions()
        done = processed_ids()
        for s in sessions:
            sid = s['id']
            if sid in done:
                continue
            print('Processing', sid)
            result = call_llm(s['text'])
            with open(ANALYSES_FILE, 'a') as f:
                f.write(json.dumps({'session_id': sid, 'analysis': result}) + '\n')
        time.sleep(5)

if __name__ == '__main__':
    main()
