# GZCTF mix demo

Repo-bound seed event for **GZCTF**: one challenge for every
(ChallengeType × ChallengeCategory) cell — 6 types × 12 categories = **72 challenges**.

Wire this URL into `/admin/repo-bindings` on a GZCTF deployment and the
background scanner will create the event + import every `challenge.yaml`
under each category folder.

## Layout

```
.gzevent                                     # event manifest (one game)
<Category>/<challenge-slug>/challenge.yaml   # 72 challenge definitions
<Category>/<challenge-slug>/dist/<file>      # attachment (Static/Dynamic Attachment types — 24 of these)
<Category>/<challenge-slug>/src/Dockerfile   # real Dockerfile for the FULL_BUILD subset (6 of these)
```

## What's actually wired up

- **All 24 attachment-type challenges** ship a `./dist/<file>` themed for
  the category (Caesar ciphertext for Crypto, pcap summary for Forensics,
  Solidity stub for Blockchain, …). The `provide:` field in the yaml
  points at it so GZCTF serves the file to players.

- **All 12 AttackDefense challenges** (one per category) have a real
  `./src/Dockerfile` with a category-themed vulnerable service — every
  one reads `/flag` at request time so the platform's per-tick flag
  rotation takes effect. Surfaces vary: Crypto = AES-CTR nonce reuse,
  Web = path-traversal alias, Mobile = hardcoded creds, AI = redact-list
  bypass, Forensics = metadata leak, Hardware = undocumented UART cmd,
  Pentest = nginx wildcard alias, etc.

- **+5 more buildable showcase challenges** (one per category sampler)
  to exercise the build path for non-A&D types:
    - `Web/web-service` (StaticContainer) — alpine + busybox httpd
    - `Crypto/crypto-per-team-box` (DynamicContainer) — python XOR oracle
    - `Misc/koth-misc-hill` (KingOfTheHill) — hill with PUT /koth/king
    - `Mobile/mobile-service` (StaticContainer) — nginx APK-landing page
    - `AI/ai-per-team-box` (DynamicContainer) — fake LLM prompt gate

  All 17 buildable rows leave `containerImage:` empty so
  `ChallengeImportService.ResolveBuildIntent` resolves to BuildNeeded
  (BuildStatus goes Queued → Building → Built on import; ~30s each on
  alpine; visible in /admin/games/<id>/challenges).

- **The remaining 55 container challenges** reuse `gzctf/echo-http:test`
  (a published demo image) so they stand up without a build.

Regenerated from `scripts/seed/gen-mix-repo.py` in the GZCTF repo.
