# Maintenance workflow

A scheduled maintenance job compares working projects with their GitHub template repositories once a week.

## What the job does

1. Inventory known project paths.
2. Compare source modification times with template repositories.
3. Run repository checks on template repos.
4. Identify findings that would block a publish.
5. For published repos, update docs/code only after a check and build/smoke test pass.
6. Report what changed, what was published, and what needs manual review.

## What it must never publish

- live `.env` files
- tokens/passwords/API keys
- private tracker/indexer details
- live databases or caches
- local photos/media/documents
- private network addresses or private domains
- backup files containing old secrets

## Current repo set

- `gamefinder`
- `minecraft-server-dashboard`
- `lego-catalog`
- `homelab-projects`
- `jellyfin-signup-helper`
- `media-automation-stack-template`

## Candidate backlog

- command-center dashboard template
- Navidrome intelligence API
- Minecraft plugin updater
- IPTV/EPG cleanup tooling as docs/templates only
