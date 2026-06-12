# Template publishing workflow

This is the workflow used for turning a working homelab project into a repo other people can copy.

## 1. Export to a separate directory

Do not initialize a shareable repo directly in a live service directory. Copy only the files intended for the template into a separate export directory.

## 2. Replace live config with examples

- Real `.env` -> `.env.example` with placeholders.
- Local compose files -> generic compose templates.
- Private URLs -> service names or localhost examples.
- Host paths -> configurable environment variables.
- Live data -> excluded.

## 3. Remove history and runtime artifacts

Do not copy:

- `*.bak`, timestamped backups, old config snapshots
- `node_modules`, `__pycache__`, `.venv`
- logs, databases, generated caches
- live media, photos, documents, uploads

## 4. Check before publishing

Run a repository check for:

- private IPs and overlay/VPN addresses
- private domains and internal hostnames
- secrets, tokens, passwords, API keys
- host paths and disk labels
- long random-looking strings

## 5. Build or smoke test

Use the project’s intended runtime:

- Python: `python -m py_compile`, Flask test client, Docker build if local deps are missing.
- Node: `node --check`, `npm test`/`npm run check` where available, Docker build.
- Compose templates: `docker compose config` where safe.

## 6. Publish with normal HTTPS remote

Use a normal GitHub HTTPS remote and a temporary credential helper. Do not embed tokens in remote URLs or commit them to config files.

## 7. Verify remote

After push, fetch the GitHub URL and confirm README renders and the repo is public.
