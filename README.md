# Lukulu Hub

Lukulu Hub is the operating system for Lukulu Recordings: catalog management, artist profiles, release campaigns, AI promo generation, press kits, daily social automation, and deployment workflows.

## Production architecture

The recommended production direction is a hybrid stack:

- Frontend: Next.js on AppDeploy
- Backend: FastAPI on FastAPI Cloud
- Database, auth, storage, realtime: Supabase
- AI: OpenAI Responses API from trusted server-side code only
- CI/CD: GitHub Actions
- Creative assets: Adobe Express and Photoshop workflows

## Core modules

- Catalog and release database
- Artist Hub
- AI Gen All
- Auto Finalize
- Press Kit Builder
- Social Autopilot
- Spotify/DSP links
- Marketing Calendar
- Admin review and approval workflows

## Security rules

Never commit passwords, API keys, Facebook or Instagram logins, Supabase secret keys, OpenAI keys, or Meta access tokens. Use OAuth and encrypted secret storage only.

## Current live app

AppDeploy preview: https://d79f9e4f13f65eacaa.v2.appdeploy.ai/

Planned short domain: https://hub.lukulurecordings.com/
