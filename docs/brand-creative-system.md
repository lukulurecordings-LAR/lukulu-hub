# Lukulu Brand Creative System

This document captures the visual direction from the uploaded Lukulu identity references and translates it into implementation rules for the app, Figma, Canva, Adobe Express, and release artwork workflows.

## Core visual identity

Lukulu Recordings should feel like an Afro House record label, not a generic SaaS dashboard. The design language combines:

- carved wood surfaces
- metallic silver and gold logo variants
- black premium stage/lighting backgrounds
- African geometric line patterns
- speaker cones, drums, and music hardware
- textured scratches, embossing, shadows, and grain
- release-artwork tiles that feel physical and collectible

## Approved source directions

### 1. Natural carved wood direction

Use this for warm label identity, heritage storytelling, artist bios, and label profile pages.

Visual cues:

- brown wood grain
- carved Africa silhouette
- carved cursive Lukulu wordmark
- physical speaker/drum objects
- realistic shadows
- warm studio lighting

Best uses:

- label biography page
- artist profile headers
- print/export profile
- long-form press kit cover
- culture/story posts

### 2. Metallic silver direction

Use this for premium dashboard surfaces, analytics, backend status, and technology-forward views.

Visual cues:

- black background
- silver Africa mark
- silver speaker cone
- monochrome metal finish
- subtle glow
- high contrast

Best uses:

- app chrome
- dashboard headers
- Data Analytics tab
- GitHub/FastAPI/Supabase integration cards
- executive reporting

### 3. Gold premium direction

Use this for campaign-ready releases, hero CTAs, and high-value social posts.

Visual cues:

- black background
- gold embossed Africa mark
- glowing speaker cone
- gold cursive wordmark
- luxury music-brand energy

Best uses:

- Generate Everything / Auto Finalize CTAs
- social hero templates
- release-week announcements
- DJ promo graphics
- campaign-complete states

### 4. Colorful textile direction

Use this selectively for cultural celebration, festival posts, fan engagement, and special campaigns.

Visual cues:

- bold African textile patterns
- red, green, yellow, blue accents
- strong linework
- layered graphics
- bright Afro-house energy

Best uses:

- Instagram carousel posts
- culture posts
- Sunday label story
- celebratory release milestones
- merchandise concepts

## App design rules

The Lukulu Hub app should keep a base of black, charcoal, silver, and warm wood tones. Bright textile color should be used as an accent, not as the default dashboard background.

Recommended app hierarchy:

1. Command Center: black/silver metallic theme
2. Data Analytics: black/silver, subtle grid/pattern, executive style
3. Label Profile: carved wood warmth
4. People: wood + silver profile cards
5. Releases: artwork tiles, each release can choose wood/gold/silver/colorful treatment
6. Social Autopilot: gold highlights for approved/scheduled posts

## Component rules

### Cards

- dark rounded panels
- embossed border highlights
- subtle inner shadow
- scratch/grain overlay
- African geometric pattern at low opacity

### Release tiles

Each release tile should show:

- title
- primary artist
- catalog number
- UPC or DSP match state
- ISRC where available
- catalog health score
- small artwork-style visual

### Buttons

Primary buttons should feel like metal or polished lacquer:

- white/silver primary for neutral actions
- gold primary for campaign actions
- dark outlined secondary buttons

### Typography

- large strong headings
- narrow uppercase labels for system status
- elegant serif or editorial feel for label biography
- avoid generic startup-style typography

## Canva direction

Create reusable Canva templates for:

- Instagram release spotlight
- Instagram story
- Facebook post
- artist profile card
- label biography card
- Traxsource/Beatport release announcement
- weekly catalog throwback
- Sunday label story

Template variants:

- Wood Heritage
- Silver Premium
- Gold Campaign
- Color Textile Celebration

## Adobe direction

Use Adobe Express/Photoshop workflows for:

- release artwork enhancement
- social post templates
- background color variants
- grain/scratch overlays
- metallic or wood-styled campaign visuals
- cropped square/portrait/story sizes

Preferred sizes:

- Instagram square: 1080x1080
- Instagram portrait: 1080x1350
- Instagram/Facebook story: 1080x1920
- Facebook post: 1200x630
- YouTube/press thumbnail: 1280x720

## Figma direction

Figma file should include:

- design tokens for black/silver/gold/wood/textile accents
- reusable card components
- release tile component
- people profile card
- analytics metric card
- social autopilot card
- label profile print layout
- mobile and desktop frames

Note: the connected Figma account currently has View access. Editing requires a Figma seat or file with edit permissions.

## Asset storage plan

When binary uploads are available through the app/resource flow, store brand sources under:

```text
public/resources/brand/lukulu-wood-logo.jpg
public/resources/brand/lukulu-silver-logo.jpg
public/resources/brand/lukulu-gold-logo.jpg
public/resources/brand/lukulu-color-textile-logo.jpg
```

For AppDeploy updates, images should be added through resource upload slots rather than inlined as base64.

## AI content use

AI-generated copy should describe the label as:

- Afro House and African electronic music
- cultural rhythm and modern dancefloor energy
- DJ-ready releases
- African storytelling
- premium independent label identity

Avoid describing the brand as generic EDM, pop, or corporate tech unless the context is analytics/backend infrastructure.
