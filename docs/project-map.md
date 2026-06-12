# Project map

## GameFinder

**Use case:** Find ROM/game releases through Prowlarr, add selected results to qBittorrent, and organize finished payloads for RomM.

**Patterns worth reusing:**

- Scope Prowlarr searches to known game/console-capable indexers instead of querying every enabled indexer.
- Use explicit category filtering and server-side rejection of movies, TV, audio, books, and unrelated categories.
- Keep qBittorrent source payloads in place for seeding; hardlink/copy into the library instead of moving files.
- Add a jobs/status page that shows real progress, speeds, paths, and completion state.
- Use optional RomM DB/resource integration for recommendation widgets while still working without it.

Repo: <https://github.com/CH33ZELOUIZ/gamefinder>

## Minecraft Server Dashboard

**Use case:** Private web control panel for a Dockerized Minecraft server.

**Patterns worth reusing:**

- Bind-mount the Minecraft data directory for logs/settings/file operations.
- Use Docker inspect for container state and Docker actions for start/stop/restart.
- Use RCON for game commands rather than shelling into server internals for every operation.
- Keep API access private-network-only by default.
- Document the risk of mounting `/var/run/docker.sock` clearly.

Repo: <https://github.com/CH33ZELOUIZ/minecraft-server-dashboard>

## LEGO Catalog

**Use case:** Personal LEGO set/minifigure inventory with metadata enrichment and CSV workflows.

**Patterns worth reusing:**

- Keep live database and cached images out of git.
- Cache remote images locally but make cache rebuildable.
- Support CSV import/export for interoperability.
- Use review states for uncertain item identification instead of pretending every match is exact.
- Allow optional local photo review through a configurable mounted folder.

Repo: <https://github.com/CH33ZELOUIZ/lego-catalog>

## Planned public exports

These are useful but require deeper sanitization before publication:

- Command Center dashboard template: private homelab dashboard layout, service cards, live widgets, and automation buttons.
- Media automation stack template: generic Docker Compose patterns for Gluetun, qBittorrent, Servarr apps, Jellyfin/Jellyseerr, Unpackerr, and related tooling.
- Jellyfin signup helper: small account/self-service helper pattern.
- Navidrome intelligence/recommendation API: read-only music-library metadata helper.
- Minecraft plugin updater: small automation script for server plugin updates.
