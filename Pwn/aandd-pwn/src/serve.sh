#!/bin/sh
# Pwn A&D — trivial 'echo /flag' service for the checker.
# A real challenge would expose a vulnerable binary here.
echo "OK"; if [ -r /flag ]; then cat /flag; else echo "no flag yet"; fi
