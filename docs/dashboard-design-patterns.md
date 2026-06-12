
# Dashboard design patterns

## Dense but readable

A homeserver dashboard should be dense enough to be useful but not so compressed that state is unclear.

Good widgets show:

- working/partial/broken state
- API-backed values
- timestamps or sample intervals
- current paths or target service names
- clear progress bars and speed values

## Avoid nested scroll traps

If a section is important, let the page grow instead of trapping it inside a tiny scroll box. Use internal scroll only for secondary lists like process tables.

## Service cards

Useful cards include:

- app name
- URL/port
- container state
- health/API state
- quick actions only when safe

## Disk cards

Separate activity and capacity:

- Disk Read/Write: live rates per device
- Disk Usage: used/free/total per mount

Use friendly drive names consistently across both.

## Theme guidance

For always-on admin dashboards:

- prefer dark muted colors
- avoid bright cyan/blue glare
- use status color sparingly
- verify real browser layout and console errors after CSS changes
