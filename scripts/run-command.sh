#!/bin/bash
# A script to execute a command and return its output.

set -euo pipefail

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <command>"
    exit 1
fi

eval "$@"