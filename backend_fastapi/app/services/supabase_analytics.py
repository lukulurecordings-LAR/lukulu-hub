from __future__ import annotations

from typing import Any

from fastapi import HTTPException
from supabase import Client, create_client

from app.core.config import get_settings


settings = get_settings()


def get_supabase_admin() -> Client:
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(status_code=500, detail='Supabase server credentials are not configured')
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


async def get_default_organization_id() -> str:
    client = get_supabase_admin()
    result = client.table('organizations').select('id, slug, name').eq('slug', settings.default_organization_slug).limit(1).execute()
    rows = result.data or []
    if not rows:
        fallback = client.table('organizations').select('id, slug, name').limit(1).execute()
        rows = fallback.data or []
    if not rows:
        raise HTTPException(status_code=404, detail='No organization found in Supabase')
    return rows[0]['id']


async def release_performance(organization_id: str) -> list[dict[str, Any]]:
    client = get_supabase_admin()
    result = client.table('v_release_performance_summary').select('*').eq('organization_id', organization_id).order('total_streams', desc=True).limit(100).execute()
    return result.data or []


async def catalog_health(organization_id: str) -> list[dict[str, Any]]:
    client = get_supabase_admin()
    result = client.table('v_catalog_health_summary').select('*').eq('organization_id', organization_id).order('latest_health_score').limit(100).execute()
    return result.data or []


async def social_stats(organization_id: str) -> list[dict[str, Any]]:
    client = get_supabase_admin()
    result = client.table('social_daily_stats').select('*, social_channels(platform, handle, public_url)').eq('organization_id', organization_id).order('stat_date', desc=True).limit(100).execute()
    return result.data or []


async def people_stats(organization_id: str) -> list[dict[str, Any]]:
    client = get_supabase_admin()
    result = client.table('artist_monthly_stats').select('*').eq('organization_id', organization_id).order('stat_month', desc=True).limit(100).execute()
    return result.data or []


async def insight_reports(organization_id: str) -> list[dict[str, Any]]:
    client = get_supabase_admin()
    result = client.table('ai_insight_reports').select('*').eq('organization_id', organization_id).order('report_date', desc=True).limit(30).execute()
    return result.data or []


async def create_insight_report(organization_id: str, title: str, summary: str, recommendations: list[dict[str, Any]], source_metrics: dict[str, Any]) -> dict[str, Any]:
    client = get_supabase_admin()
    payload = {
        'organization_id': organization_id,
        'title': title,
        'summary': summary,
        'recommendations': recommendations,
        'source_metrics': source_metrics,
        'status': 'draft',
    }
    result = client.table('ai_insight_reports').insert(payload).execute()
    rows = result.data or []
    if not rows:
        raise HTTPException(status_code=500, detail='Could not create AI insight report')
    return rows[0]
