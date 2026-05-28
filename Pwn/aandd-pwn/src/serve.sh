#!/bin/sh
# Trivial demo "service" — echoes the contents of /flag so the
# A&D checker has something to verify. Real challenges would
# expose a vulnerable protocol here.
echo "OK"
if [ -r /flag ]; then cat /flag; else echo "no flag yet"; fi
