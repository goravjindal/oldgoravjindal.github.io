#!/bin/bash

set -e

echo "Detected Ruby version: $(ruby -e 'print RUBY_VERSION')"

RUBY_VER=$(ruby -e 'print RUBY_VERSION')
GEM_USER_DIR="$HOME/.local/share/gem/ruby/$RUBY_VER"
GEM_BIN_DIR="$GEM_USER_DIR/bin"

echo "Using gem user dir: $GEM_USER_DIR"
echo "Using gem bin dir: $GEM_BIN_DIR"

# Clean up old gem directories except current version
echo "Cleaning up old gem directories (except current version)..."
for dir in "$HOME/.local/share/gem/ruby/"*; do
    if [[ "$dir" != "$GEM_USER_DIR" ]]; then
        echo "Removing old gem dir: $dir"
        rm -rf "$dir"
    fi
done

# Make sure gem bin dir exists
mkdir -p "$GEM_BIN_DIR"

# Install bundler gem with user install
echo "Installing bundler gem (user install)..."
gem install --user-install bundler

# Install jekyll gem with user install
echo "Installing jekyll gem (user install)..."
gem install --user-install jekyll

# Add gem bin dir to PATH if not already there
if ! grep -qF "$GEM_BIN_DIR" "$HOME/.bashrc"; then
    echo "Adding $GEM_BIN_DIR to PATH in ~/.bashrc"
    echo "" >> "$HOME/.bashrc"
    echo "# Added by setup_jekyll_local.sh for Ruby gems" >> "$HOME/.bashrc"
    echo "export PATH=\"$GEM_BIN_DIR:\$PATH\"" >> "$HOME/.bashrc"
else
    echo "$GEM_BIN_DIR already in PATH in ~/.bashrc"
fi

# Export gem bin dir to PATH for current script/session
export PATH="$GEM_BIN_DIR:$PATH"

echo "Current PATH: $PATH"

# Verify bundler is available
if ! command -v bundle &> /dev/null; then
    echo "Error: bundle command not found even after PATH update."
    echo "Try restarting your shell or running: source ~/.bashrc"
    exit 1
fi

echo "Running bundle install..."
bundle install

echo "Setup complete! You can now use jekyll and bundle commands."

