
# Homelab documentation system

A useful homelab archive has two layers:

1. reusable project templates others can clone
2. a private operations log for exact local details

## Public project layer

Use this for:

- generic Docker Compose templates
- helper apps
- reusable scripts
- setup guides
- architecture patterns
- screenshots/demo data that do not reveal private infrastructure

Public repos should read like normal projects, not like conversion notes.

## Private operations layer

Use this for:

- exact paths
- private network addresses
- personal domains
- container names
- local decisions
- change history
- recovery notes
- generated inventory

Do not store secret values, even in a private repo.

## Weekly archive workflow

1. Inventory live projects.
2. Regenerate private status docs.
3. Check public templates for local-environment leaks.
4. Check private docs for obvious secrets.
5. Push only passing repos.
6. Report blocked items and next template candidates.
