import os
import uuid
import json
from datetime import datetime

DB_FILE = 'sessions_demo.json'

def save_raw_transcript(text: str) -> int:
    sid = int(uuid.uuid4().int >> 64)
    entry = {'id': sid, 'text': text, 'created_at': datetime.utcnow().isoformat()}
    with open(DB_FILE, 'a') as f:
        f.write(json.dumps(entry)+"\n")
    return sid
