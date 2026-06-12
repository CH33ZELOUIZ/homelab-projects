# Public safety checklist

Before pushing a repo public, confirm:

- [ ] No `.env` or real config files are present.
- [ ] `.env.example` uses placeholders only.
- [ ] No LAN, VPN, or Tailscale IP addresses.
- [ ] No private domains or internal hostnames.
- [ ] No passwords, API keys, passkeys, tokens, cookies, or webhook URLs.
- [ ] No private tracker/indexer names or IDs unless intentionally generic and safe.
- [ ] No live databases, logs, backups, caches, generated media, or personal photos.
- [ ] No host-specific mount paths or disk names.
- [ ] README explains setup and security risks.
- [ ] Build/syntax/smoke test passes.
- [ ] Git status contains only intended public files.
