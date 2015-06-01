#! /bin/bash

COMMIT_MSG=${1:-"default msg"}
git add --all . && git commit -m "$COMMIT_MSG"
