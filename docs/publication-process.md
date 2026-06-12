# Public export process

This is the process used to turn private server projects into public-safe repositories.

## 1. Export to a separate directory

Never initialize a public repo directly in a live service directory. Copy only the files intended for publication into a separate export directory.

## 2. Replace live config with examples

- Real `.env` -> `.env.example` with placeholders.
- Local compose files -> generic compose templates.
- Private URLs -> service names or localhost examples.
- Host paths -> configurable environment variables.
- Live data -> excluded.

## 3. Remove unsafe history and backups

Do not copy:

- `*.bak`, timestamped backups, old config snapshots
- `node_modules`, `__pycache__`, `.venv`
- logs, databases, generated caches
- live media, photos, documents, uploads

## 4. Scan before publishing

Run a private-data scan for:

- private IPs and overlay/VPN addresses
- private domains and internal hostnames
- personal usernames/handles where not intended as public branding
- secrets, tokens, passwords, API keys
- host paths and disk labels
- long random-looking strings

## 5. Build or smoke test

Use the project’s intended runtime:

- Python: `python -m py_compile`, Flask test client, Docker build if local deps are missing.
- Node: `node --check`, `npm test`/`npm run check` where available, Docker build.
- Compose templates: `docker compose config` where safe.

## 6. Publish with normal HTTPS remote

Use a normal GitHub HTTPS remote and temporary credential helper. Do not embed tokens in remote URLs or commit them to config files.

## 7. Verify remote

After push, fetch the GitHub URL and confirm README renders and the repo is public.
