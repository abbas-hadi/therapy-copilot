import json
from datetime import datetime
DB_FILE = 'sessions_demo.json'

def save_analysis(session_id: int, analysis: dict):
    entry = {'session_id': session_id, 'analysis': analysis, 'ts': datetime.utcnow().isoformat()}
    with open('analyses.json', 'a') as f:
        f.write(json.dumps(entry)+"\n")
    return True
