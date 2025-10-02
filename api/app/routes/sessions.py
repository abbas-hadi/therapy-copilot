from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.storage import save_raw_transcript
from app.services.llm import analyze_transcript_async

router = APIRouter()

@router.post('/upload')
async def upload_session(file: UploadFile = File(...)):
    if not file.filename.endswith('.txt'):
        raise HTTPException(status_code=400, detail='Only .txt transcripts supported in dev')
    content = (await file.read()).decode('utf-8')
    # store raw file (S3/local) and enqueue analysis
    session_id = save_raw_transcript(content)
    analyze_transcript_async(session_id, content)
    return {'session_id': session_id}

@router.get('/{session_id}')
def get_session(session_id: int):
    # fetch analysis from DB
    return {'session_id': session_id, 'status': 'processing_or_ready'}
