# Weekly sync/audit process

A scheduled Hermes job compares the private server projects with their public-safe export repositories once a week.

## What the weekly job does

1. Inventory known live project paths.
2. Compare live source modification times with public export repositories.
3. Re-run public safety scans on exported repos.
4. Identify private-data hits that would block publication.
5. For already-published repos, update public-safe docs/code only after a clean scan and build/smoke check.
6. Report what changed, what was published, and what needs manual/deeper sanitization.

## What it must never publish

- live `.env` files
- tokens/passwords/API keys
- private tracker/indexer details
- live databases or caches
- local photos/media/documents
- Tailscale/LAN IPs or private domains
- backup files containing old secrets

## Current published repo set

- `gamefinder`
- `minecraft-server-dashboard`
- `lego-catalog`
- `homelab-projects`

## Candidate backlog

- command-center dashboard template
- media automation stack template
- Jellyfin signup helper
- Navidrome intelligence API
- Minecraft plugin updater
- IPTV/EPG cleanup tooling as docs/templates only
