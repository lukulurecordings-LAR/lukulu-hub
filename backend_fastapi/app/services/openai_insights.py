from __future__ import annotations

from typing import Any

from openai import OpenAI

from app.core.config import get_settings


settings = get_settings()


def build_fallback_insight(metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        'title': 'Lukulu Hub Weekly Analytics Insight',
        'summary': 'Analytics data is ready. Add OpenAI credentials in FastAPI Cloud to generate richer label recommendations automatically.',
        'recommendations': [
            {'area': 'catalog', 'action': 'Prioritize releases with low catalog health scores and missing DSP links.'},
            {'area': 'social', 'action': 'Turn the strongest release into daily Instagram and Facebook content.'},
            {'area': 'artist', 'action': 'Update artist biographies and social links for people with active releases.'},
        ],
        'source_metrics': metrics,
    }


def generate_label_insight(metrics: dict[str, Any]) -> dict[str, Any]:
    if not settings.openai_api_key:
        return build_fallback_insight(metrics)

    client = OpenAI(api_key=settings.openai_api_key)
    response = client.responses.create(
        model=settings.openai_model,
        input=[
            {
                'role': 'system',
                'content': 'You are the analytics strategist for Lukulu Recordings, an Afro House record label. Create concise, practical business recommendations from label metrics.',
            },
            {
                'role': 'user',
                'content': f'Analyze these Lukulu Hub metrics and return a weekly executive insight: {metrics}',
            },
        ],
        text={
            'format': {
                'type': 'json_schema',
                'name': 'lukulu_analytics_insight',
                'strict': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'summary': {'type': 'string'},
                        'recommendations': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'area': {'type': 'string'},
                                    'action': {'type': 'string'},
                                },
                                'required': ['area', 'action'],
                                'additionalProperties': False,
                            },
                        },
                    },
                    'required': ['title', 'summary', 'recommendations'],
                    'additionalProperties': False,
                },
            }
        },
        store=False,
    )

    import json

    parsed = json.loads(response.output_text)
    parsed['source_metrics'] = metrics
    return parsed
