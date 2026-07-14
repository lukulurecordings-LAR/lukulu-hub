# Creative Asset Workflow: Adobe, Figma, Canva, AppDeploy

This workflow explains how Lukulu brand images should move through the design and app pipeline.

## Source assets

The uploaded Lukulu logo references include wood, silver, gold, and colorful textile directions. These should be treated as brand reference assets.

## Workflow

### 1. Adobe

Use Adobe tools to prepare production-ready image variants:

- clean square logo crops
- Instagram portrait crops
- story crops
- social background variants
- metallic/wood/color textile release visuals
- grain, scratch, and embossed texture treatments

Adobe is best for image finishing and template-based social graphics.

### 2. Canva

Use Canva for repeatable social templates:

- release spotlight template
- artist profile template
- catalog throwback template
- DJ promo template
- weekly label story template
- analytics milestone template

Canva templates should follow the four brand modes:

- Wood Heritage
- Silver Premium
- Gold Campaign
- Color Textile Celebration

### 3. Figma

Use Figma for the product design system:

- app screens
- components
- data analytics cards
- release cards
- people cards
- social autopilot approval flow
- mobile/desktop layouts

Current note: the connected Figma account reports View access, so edit access is needed before full Figma canvas updates can be pushed.

### 4. AppDeploy

Use AppDeploy resource slots for binary brand assets.

Do not inline images as base64 in source code. Recommended paths:

```text
public/resources/brand/lukulu-wood-logo.jpg
public/resources/brand/lukulu-silver-logo.jpg
public/resources/brand/lukulu-gold-logo.jpg
public/resources/brand/lukulu-color-textile-logo.jpg
```

The app can then reference those paths directly in release tiles, label profile, and the Social Autopilot module.

### 5. FastAPI/Supabase

FastAPI should store brand asset metadata in Supabase, not image bytes.

Recommended table later:

```sql
create table brand_assets (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid references organizations(id) on delete cascade,
  asset_type text not null,
  title text not null,
  storage_path text not null,
  usage_notes text,
  created_at timestamptz default now()
);
```

Supabase Storage can hold final production assets; database rows should hold metadata, URLs, usage tags, and approval state.

## Approval policy

All automated social posts should start in approval-first mode.

AI may generate:

- captions
- hashtags
- artwork prompts
- release blurbs
- design variant suggestions

AI should not publish directly until the Meta OAuth workflow is connected and trusted auto-post mode is explicitly enabled.
