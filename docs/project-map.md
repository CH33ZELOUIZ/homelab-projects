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

## Jellyfin Signup Helper

**Use case:** Lightweight signup page for controlled Jellyfin account creation.

**Patterns worth reusing:**

- Validate usernames and passwords before calling Jellyfin.
- Create non-admin users with conservative policy defaults.
- Keep the user-facing public Jellyfin URL separate from the internal container URL.
- Treat signup pages as private/invite-only unless you add real public anti-abuse controls.
- Never publish Jellyfin databases or API keys.

Repo: <https://github.com/CH33ZELOUIZ/jellyfin-signup-helper>

## Media Automation Stack Template

**Use case:** Generic private media automation stack template.

**Patterns worth reusing:**

- Route qBittorrent through Gluetun with `network_mode: service:gluetun`.
- Expose qBittorrent ports on Gluetun, not qBittorrent.
- Use one shared `/data` mount across downloaders and media managers to preserve hardlinks.
- Keep all real VPN credentials, API keys, indexer/tracker details, and paths out of git.
- Document the path contract before users configure Sonarr/Radarr/Lidarr.

Repo: <https://github.com/CH33ZELOUIZ/media-automation-stack-template>

## Planned public exports

These are useful but require deeper sanitization before publication:

- Command Center dashboard template: private homelab dashboard layout, service cards, live widgets, and automation buttons.
- Navidrome intelligence/recommendation API: read-only music-library metadata helper.
- Minecraft plugin updater: small automation script for server plugin updates.
