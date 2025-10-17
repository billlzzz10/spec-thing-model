#!/bin/bash
# A script to execute a command and return its output.

set -e

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <command>"
    exit 1
fi

eval "$@"