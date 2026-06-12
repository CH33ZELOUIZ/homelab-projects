# CH33ZE Homelab Projects

Copy-ready homelab projects, Docker templates, and setup guides from CH33ZE.

This repo is the map. Individual tools live in their own repositories so they can be cloned and used independently.

## Projects

| Project | What it solves | Repo |
| --- | --- | --- |
| GameFinder | Search console/ROM-capable Prowlarr indexers, send downloads to qBittorrent, and stage completed files into a RomM-style library layout. | <https://github.com/CH33ZELOUIZ/gamefinder> |
| Minecraft Server Dashboard | Mobile-friendly dashboard for a Dockerized Minecraft server: status, logs, RCON commands, settings, file browser, icon upload, and shell access for trusted admins. | <https://github.com/CH33ZELOUIZ/minecraft-server-dashboard> |
| LEGO Catalog | Dockerized Flask app for tracking LEGO sets and minifigures with owned/wanted lists, CSV import/export, metadata enrichment, cached images, and review workflows. | <https://github.com/CH33ZELOUIZ/lego-catalog> |
| Jellyfin Signup Helper | Tiny self-hosted signup page for creating Jellyfin users, plus optional default home/library preference setup. | <https://github.com/CH33ZELOUIZ/jellyfin-signup-helper> |
| Media Automation Stack Template | Docker Compose template for Gluetun, qBittorrent, Servarr apps, Jellyfin/Jellyseerr, and Unpackerr. | <https://github.com/CH33ZELOUIZ/media-automation-stack-template> |

## Design goals

- Share working homelab patterns as reusable templates.
- Keep each app Docker-friendly and understandable.
- Prefer `.env.example` and setup docs over hardcoded local paths.
- Explain security boundaries honestly, especially for dashboards that control Docker or automation services.
- Keep the projects easy to update as the live setup evolves.

## Start here

- [Project map](docs/project-map.md)
- [Reusable architecture patterns](docs/architecture-patterns.md)
- [Template publishing workflow](docs/template-publishing-workflow.md)
- [Maintenance workflow](docs/maintenance-workflow.md)
- [Template check checklist](docs/template-checklist.md)
- [Project archive checklist](docs/project-archive-checklist.md)
- [Media stack operations patterns](docs/media-stack-operations-patterns.md)
- [Dashboard design patterns](docs/dashboard-design-patterns.md)
- [Homelab documentation system](docs/homelab-documentation-system.md)

## License

MIT. Copyright (c) 2026 CH33ZE.
