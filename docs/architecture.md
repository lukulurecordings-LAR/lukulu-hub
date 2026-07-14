# Lukulu Hub Architecture

## Recommended stack

Use a hybrid deployment model:

1. Next.js frontend on AppDeploy.
2. FastAPI backend on FastAPI Cloud.
3. Supabase for Auth, Postgres, Storage, Realtime, Queues, and RLS.
4. OpenAI Responses API behind the FastAPI backend.
5. GitHub Actions for CI/CD.
6. Adobe Express / Photoshop for branded social and promo assets.
7. Intercom for support and user feedback once connected.

## Backend API modules

- `/v1/health`
- `/v1/auth/me`
- `/v1/artists`
- `/v1/releases`
- `/v1/tracks`
- `/v1/campaigns`
- `/v1/ai/gen-all`
- `/v1/ai/auto-finalize`
- `/v1/social/daily-post`
- `/v1/uploads/sign`
- `/v1/jobs/{job_id}`

## Social Autopilot

Daily social automation should use official Meta OAuth and APIs, never raw Facebook or Instagram passwords.

Workflow:

1. AI drafts a daily post from the catalog.
2. The app creates Facebook and Instagram variants.
3. The app generates a design prompt for Adobe/Canva-style assets.
4. User reviews and approves.
5. Backend posts or schedules through official Meta APIs.
6. Every action is written to an audit log.

## Supabase baseline

Core tables:

- organizations
- organization_members
- profiles
- artists
- releases
- release_artists
- tracks
- track_artists
- campaigns
- assets
- social_posts
- ai_jobs
- audit_logs

RLS must be enabled for all exposed tables. Access should be organization-scoped.

## AI safety and secrets

- OpenAI API key stays server-side only.
- Meta tokens stay encrypted in backend secrets or a secure token store.
- Supabase secret keys stay server-side only.
- GitHub secrets should use protected environments.
- Publishing automation should start with approval mode before trusted auto-posting.
