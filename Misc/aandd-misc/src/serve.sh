#!/bin/sh
# Misc A&D — echoes the flag prefixed with a banner. Trivial.
echo "[gzctf-misc] OK"; cat /flag 2>/dev/null || echo "no flag yet"
