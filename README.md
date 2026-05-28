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

- **6 container-type challenges have a real `./src/Dockerfile`** — leaving
  `containerImage:` empty in the yaml so GZCTF's auto-build pipeline
  picks them up (`ChallengeImportService.ResolveBuildIntent`):
    - `Web/web-service` — alpine + busybox httpd
    - `Crypto/crypto-per-team-box` — python XOR oracle
    - `Pwn/and-pwn` — A&D socat service that serves /flag
    - `Misc/koth-misc-hill` — KotH hill with PUT /koth/king
    - `Mobile/mobile-service` — nginx APK-landing page
    - `AI/ai-per-team-box` — fake LLM prompt gate
  These exercise the build pipeline end-to-end on import (you'll see
  BuildStatus go Queued → Building → Built in /admin/games/<id>/challenges).

- **The remaining 60 container challenges** reuse `gzctf/echo-http:test`
  (a published demo image) so they stand up without a build.

Regenerated from `scripts/seed/gen-mix-repo.py` in the GZCTF repo.
