
# Media stack operations patterns

## Path contract first

Most media automation failures are path mismatches. Every downloader and organizer should agree on inside-container paths.

Preferred pattern:

```text
/data/downloads
/data/media
```

## Download client routing

When qBittorrent runs through a VPN network namespace:

- publish qBittorrent ports on the VPN container
- keep qBittorrent's own service behind the VPN namespace
- check the VPN health before blaming qBittorrent

## Imports and extraction

- Unpack archive downloads before Servarr import finalization.
- Keep archive extraction logs visible.
- Watch Servarr queues for stuck imports.
- Preserve hardlinks when possible.

## Transcoding safety

For background transcoders:

- cap CPU and memory at the container level
- run only one heavy job at a time on small servers
- pause when Jellyfin playback is active
- avoid converting music libraries unless the goal is explicitly lossy conversion

## Monitoring

Monitor both layers:

- container/process health
- user-facing HTTP/API behavior
