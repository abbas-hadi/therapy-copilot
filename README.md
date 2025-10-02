# Therapy Copilot

Prototype -> Production-ready scaffold for Therapy Copilot (AI Copilot for therapists).

## Quickstart (local, dev)
1. Copy `.env.example` to `.env` and set values (OPENAI_API_KEY, DATABASE_URL, etc.)
2. Build and run with docker-compose (dev):
   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```
3. API available at http://localhost:8000
4. Frontend at http://localhost:3000

## Project structure
- `api/` FastAPI backend
- `web/nextjs-app` Frontend
- `worker/` Background job processor
- `infra/terraform` Skeleton for AWS resources

## Notes
- This scaffold is demo-grade. For production/HIPAA, follow the HIPAA checklist in docs/hipaa-checklist.md before processing PHI.
