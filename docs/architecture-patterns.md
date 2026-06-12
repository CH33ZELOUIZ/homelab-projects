# Reusable architecture patterns

## Private admin dashboards

Admin dashboards that can control Docker, run commands, or edit service files should be treated like shell access.

Recommended pattern:

1. Bind only to LAN/VPN or put behind a real auth proxy.
2. Use fixed, curated actions instead of arbitrary command execution where possible.
3. If a browser terminal is included, make the risk obvious in the README.
4. Keep configuration in environment variables and examples, not hardcoded private URLs.
5. Verify rendered UI and API payloads before declaring changes complete.

## Container path contracts

Many homelab bugs come from mismatched paths between host, downloader, organizer, and library apps.

Reusable pattern:

- Pick one canonical inside-container path for each class of data.
- Document the host bind mount separately.
- If another service reports paths from its own container namespace, add a configurable mapping variable.
- Preserve hardlinks for media/download workflows when possible.

## Public-safe templates

A useful public repo should include:

- `README.md` with what it does, when to use it, setup, and risks.
- `.env.example` with placeholders only.
- `.gitignore` that blocks `.env`, databases, caches, logs, generated media, and bind-mount data.
- Dockerfile/Compose if Docker is the intended path.
- A safety scan script or checklist.
- No live config, backups, tokens, private paths, or personal domains.

## Status pages that are actually useful

For dashboards/jobs pages, show working state rather than hiding details:

- active vs completed sections
- progress percent
- current/final paths
- download/upload speed
- backend status or error message
- whether the system is fully working, partial, queued, or blocked
