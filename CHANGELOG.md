# Changelog

Versioning: [SemVer](https://semver.org/).

## [Unreleased]
### Removed
- Disabled leftovers: Embeddium, old Iris 1.8.12, Sodium addon jars, tensura_trepu, wiki mod

### Fixed
- Music toasts showed raw ids (e.g. `menu-02`) for TIMM tracks: TIMM's `musics.json` keys lacked the `music/` path segment that MusicNotification looks up. Merged override in `kubejs/assets/musicnotification/musics.json`.
