#!/usr/bin/env bash

set -euo pipefail

echo "Installing workspace dependencies..."
npm install

echo "Done. Use the following commands in separate terminals:"
echo "  npm run dev:api"
echo "  npm run dev:web"
