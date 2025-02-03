#!/bin/bash

echo "🔧 Configuring Git to use repository-defined hooks..."

# 1️⃣ Temporarily Unset hooksPath to Let Pre-commit Install Hooks
git config --unset-all core.hooksPath || true  

echo "📦 Checking for Poetry installation..."
if ! command -v poetry >/dev/null 2>&1; then
  echo "🚨 Poetry is not installed. Please install it first: https://python-poetry.org/docs/#installation"
  exit 1
fi

echo "📥 Installing dependencies..."
poetry install  # Install both project and dependencies

echo "⚙️ Installing pre-commit hooks..."
poetry run pre-commit install --install-hooks --hook-type pre-commit  # Install hooks normally

# 2️⃣ Reapply Custom Hooks Path
git config core.hooksPath .githooks  

echo "✅ Setup complete! Git will now use hooks from .githooks/"

