
# Project archive checklist

Use this when turning a working homelab project into a durable GitHub artifact.

## For every project

- [ ] README explains what it does and who it is for.
- [ ] Setup steps are copyable.
- [ ] Architecture is documented.
- [ ] Operations/troubleshooting notes exist.
- [ ] Security risks are stated clearly.
- [ ] Generated data, logs, caches, and secrets are ignored.
- [ ] License exists.

## For Docker projects

- [ ] `Dockerfile` or image strategy is documented.
- [ ] `docker-compose.yml` is usable with placeholders/examples.
- [ ] `.env.example` exists.
- [ ] Volumes and path contracts are explained.

## For dashboards

- [ ] API endpoints are documented.
- [ ] Auth/network placement is documented.
- [ ] Privileged mounts such as Docker socket are explained.
- [ ] Browser verification is part of the workflow.

## For private operations archives

- [ ] Exact paths and service names are documented.
- [ ] Recovery steps are documented.
- [ ] Change history is grouped by area.
- [ ] Raw transcripts are not committed unless reviewed.
- [ ] Secret scan passes before push.
