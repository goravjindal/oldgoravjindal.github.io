#!/bin/bash
set -e

echo "=== Removing existing Ruby gems and environments ==="

# Remove user-installed gems (local gems)
echo "Removing Ruby gems from ~/.gem"
rm -rf ~/.gem

# Remove rbenv if installed
if [ -d "$HOME/.rbenv" ]; then
  echo "Removing existing rbenv at ~/.rbenv"
  rm -rf ~/.rbenv
fi

# Remove RVM if installed
if [ -d "$HOME/.rvm" ]; then
  echo "Removing existing RVM at ~/.rvm"
  rm -rf ~/.rvm
fi

# Unset Ruby env variables
unset GEM_HOME
unset GEM_PATH

echo "=== Removing system ruby packages (if installed via pacman) ==="
# WARNING: This removes system ruby which might break system packages relying on it!
# You might want to skip this if system ruby is used by your OS.

sudo pacman -Rs --noconfirm ruby || echo "Ruby package not installed or failed to remove, continuing..."

echo "=== Installing dependencies for rbenv ==="
sudo pacman -Syu --noconfirm base-devel git curl openssl libffi readline

echo "=== Installing rbenv and ruby-build ==="
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
cd ~/.rbenv && src/configure && make -C src

git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build

echo "=== Setting up rbenv in shell ==="
if ! grep -q 'rbenv init' ~/.bashrc; then
  echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(rbenv init -)"' >> ~/.bashrc
fi
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"

echo "=== Installing Ruby 3.4.4 ==="
rbenv install 3.4.4
rbenv global 3.4.4
rbenv rehash

echo "=== Ruby version ==="
ruby -v

echo "=== Testing erb ==="
if ruby -rerb -e 'puts "erb works"' ; then
  echo "Setup completed successfully!"
else
  echo "There was a problem loading erb."
fi

