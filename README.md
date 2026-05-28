# GZCTF mix demo

Repo-bound seed event for **GZCTF**: one challenge for every
(ChallengeType × ChallengeCategory) cell — 6 types × 12 categories = **72 challenges**.

Wire this URL into `/admin/repo-bindings` on a GZCTF deployment and the
background scanner will create the event + import every `challenge.yaml`
under each category folder.

Generated showcase entries — container-type rows reuse `gzctf/echo-http:test`,
dynamic types have placeholder flag templates. Useful for UI/scoreboard
parity testing, not as a real CTF.
