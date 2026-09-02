#!/bin/bash
# Deploy the Blossom site: rebuild, sync to the public Pages repo, push live.
set -e
cd "$(dirname "$0")"
python3 site/_build/build.py
DEPLOY=$(mktemp -d)
git clone -q --depth 1 https://github.com/hicdam/blossomgarden-site "$DEPLOY"
rsync -a --delete --exclude '.git' --exclude '_build' --exclude '*.zip' --exclude '.DS_Store' site/ "$DEPLOY/"
echo "blossomgarden.design" > "$DEPLOY/CNAME"
touch "$DEPLOY/.nojekyll"
cd "$DEPLOY"
git add -A
git diff --cached --quiet && { echo "No changes to deploy."; exit 0; }
git commit -m "Deploy $(date '+%Y-%m-%d %H:%M')

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
git push
echo "Deployed to blossomgarden.design"
