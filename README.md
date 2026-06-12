# CH33ZE Homelab Projects

Public-safe project index and reusable setup notes from a real self-hosted homeserver buildout.

This repo is the map. Individual tools live in their own repositories so they can be cloned and used independently.

## Published projects

| Project | What it solves | Repo |
| --- | --- | --- |
| GameFinder | Search console/ROM-capable Prowlarr indexers, send downloads to qBittorrent, and stage completed files into a RomM-style library layout. | <https://github.com/CH33ZELOUIZ/gamefinder> |
| Minecraft Server Dashboard | Mobile-friendly private dashboard for a Dockerized Minecraft server: status, logs, RCON commands, settings, file browser, icon upload, and shell. | <https://github.com/CH33ZELOUIZ/minecraft-server-dashboard> |
| LEGO Catalog | Dockerized Flask app for tracking LEGO sets and minifigures with owned/wanted lists, CSV import/export, metadata enrichment, cached images, and review workflows. | <https://github.com/CH33ZELOUIZ/lego-catalog> |

## Design goals

- Share working homelab patterns without publishing private infrastructure.
- Keep each app Docker-friendly and understandable.
- Prefer `.env.example` and setup docs over hardcoded server paths.
- Explain security boundaries honestly, especially for dashboards that control Docker or automation services.
- Keep published repos in sync with the private server through a weekly sanitized export/audit process.

## What is intentionally not included

- API keys, passwords, tokens, passkeys, cookies, or private tracker details.
- LAN/VPN/Tailscale IPs, private domains, or internal hostnames.
- Live databases, media libraries, cached personal images, logs, or backups.
- Host-specific mount paths or disk labels.

## Start here

- [Project map](docs/project-map.md)
- [Reusable architecture patterns](docs/architecture-patterns.md)
- [Public export and sanitization process](docs/publication-process.md)
- [Weekly sync/audit process](docs/weekly-sync.md)
- [Public safety checklist](docs/sanitization-checklist.md)

## License

MIT for original code and docs in this repo. Each linked project has its own license file.
