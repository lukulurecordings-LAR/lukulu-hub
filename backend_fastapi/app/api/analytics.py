from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Query
from pydantic import BaseModel

from app.services.openai_insights import generate_label_insight
from app.services.supabase_analytics import (
    catalog_health,
    create_insight_report,
    get_default_organization_id,
    insight_reports,
    people_stats,
    release_performance,
    social_stats,
)

router = APIRouter(prefix='/v1/analytics', tags=['analytics'])


class AnalyticsOverview(BaseModel):
    total_releases: int
    total_streams: int
    total_revenue: float
    average_catalog_health: float
    social_posts_tracked: int
    people_records: int


async def resolve_org_id(organization_id: str | None = None) -> str:
    return organization_id or await get_default_organization_id()


@router.get('/overview', response_model=AnalyticsOverview)
async def overview(organization_id: str | None = Query(default=None)) -> AnalyticsOverview:
    org_id = await resolve_org_id(organization_id)
    releases = await release_performance(org_id)
    health = await catalog_health(org_id)
    social = await social_stats(org_id)
    people = await people_stats(org_id)

    total_streams = sum(int(row.get('total_streams') or 0) for row in releases)
    total_revenue = sum(float(row.get('total_revenue') or 0) for row in releases)
    avg_health = 0.0
    if health:
        avg_health = sum(float(row.get('latest_health_score') or 0) for row in health) / len(health)

    return AnalyticsOverview(
        total_releases=len(releases),
        total_streams=total_streams,
        total_revenue=round(total_revenue, 2),
        average_catalog_health=round(avg_health, 2),
        social_posts_tracked=len(social),
        people_records=len(people),
    )


@router.get('/releases')
async def releases(organization_id: str | None = Query(default=None)) -> list[dict[str, Any]]:
    return await release_performance(await resolve_org_id(organization_id))


@router.get('/catalog-health')
async def health(organization_id: str | None = Query(default=None)) -> list[dict[str, Any]]:
    return await catalog_health(await resolve_org_id(organization_id))


@router.get('/social')
async def social(organization_id: str | None = Query(default=None)) -> list[dict[str, Any]]:
    return await social_stats(await resolve_org_id(organization_id))


@router.get('/people')
async def people(organization_id: str | None = Query(default=None)) -> list[dict[str, Any]]:
    return await people_stats(await resolve_org_id(organization_id))


@router.get('/insights')
async def insights(organization_id: str | None = Query(default=None)) -> list[dict[str, Any]]:
    return await insight_reports(await resolve_org_id(organization_id))


@router.post('/insights/generate')
async def generate_insights(organization_id: str | None = Query(default=None)) -> dict[str, Any]:
    org_id = await resolve_org_id(organization_id)
    metrics = {
        'overview': (await overview(org_id)).model_dump(),
        'top_releases': await release_performance(org_id),
        'catalog_health': await catalog_health(org_id),
        'social': await social_stats(org_id),
        'people': await people_stats(org_id),
    }
    insight = generate_label_insight(metrics)
    return await create_insight_report(
        organization_id=org_id,
        title=insight['title'],
        summary=insight['summary'],
        recommendations=insight['recommendations'],
        source_metrics=insight.get('source_metrics', metrics),
    )
