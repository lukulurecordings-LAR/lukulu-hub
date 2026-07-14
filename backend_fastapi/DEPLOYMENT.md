# FastAPI Cloud Deployment Guide

This backend is the trusted analytics and AI API layer for Lukulu Hub.

## Runtime

- Python 3.12
- FastAPI
- Uvicorn
- Supabase Python client
- OpenAI server-side insight generation

## Start command

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker start

```bash
docker build -t lukulu-hub-api .
docker run --env-file .env -p 8000:8000 lukulu-hub-api
```

## Required environment variables

```bash
ENVIRONMENT=production
CORS_ORIGINS=https://d79f9e4f13f65eacaa.v2.appdeploy.ai,https://lukulu-hub.vercel.app,https://hub.lukulurecordings.com
SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
SUPABASE_PUBLISHABLE_KEY=sb_publishable_REPLACE_ME
SUPABASE_SERVICE_ROLE_KEY=REPLACE_WITH_SERVER_SIDE_SECRET_ONLY
OPENAI_API_KEY=REPLACE_WITH_SERVER_SIDE_SECRET_ONLY
OPENAI_MODEL=gpt-4.1-mini
DEFAULT_ORGANIZATION_SLUG=lukulu-recordings
```

Never commit real keys. Add secrets through the hosting provider dashboard only.

## Health check

```bash
GET /v1/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "Lukulu Hub Analytics API",
  "version": "0.1.0"
}
```

## Analytics endpoints

```text
GET  /v1/analytics/overview
GET  /v1/analytics/releases
GET  /v1/analytics/catalog-health
GET  /v1/analytics/social
GET  /v1/analytics/people
GET  /v1/analytics/insights
POST /v1/analytics/insights/generate
```

## Deployment notes

1. Deploy the `backend_fastapi` folder as the FastAPI service root.
2. Set the start command to the Uvicorn command above, or use the Dockerfile.
3. Add the environment variables in the hosting dashboard.
4. Confirm `/v1/health` returns OK.
5. Connect the AppDeploy/Vercel frontend to the deployed API URL.
6. Keep OpenAI and Supabase service-role keys server-side only.

## Security baseline

- Supabase Row Level Security stays enabled.
- The service-role key is used only by the backend.
- The frontend must never receive `SUPABASE_SERVICE_ROLE_KEY` or `OPENAI_API_KEY`.
- Social posting must use official OAuth tokens, not passwords.
