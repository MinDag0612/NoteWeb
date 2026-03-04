#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="${PROJECT_DIR:-/var/www/NoteWeb}"
FRONTEND_DIR="${FRONTEND_DIR:-${PROJECT_DIR}}"
BACKEND_DIR="${BACKEND_DIR:-${PROJECT_DIR}/backendSrc}"
PYTHON_VENV_DIR="${PYTHON_VENV_DIR:-${BACKEND_DIR}/.venv}"
NODE_MAJOR="${NODE_MAJOR:-20}"

print_usage() {
  cat <<'EOF'
Usage: bash scripts/setup.sh

Prepares an Ubuntu host for the NoteWeb project by:
  - installing required system packages for Node.js and Python
  - installing Node.js LTS if it is missing or older than the configured major version
  - creating runtime directories used during later deployment phases
  - creating a Python virtual environment for the backend
  - installing backend Python dependencies

Optional environment variables:
  PROJECT_DIR      Default: /var/www/NoteWeb
  FRONTEND_DIR     Default: ${PROJECT_DIR}
  BACKEND_DIR      Default: ${PROJECT_DIR}/backendSrc
  PYTHON_VENV_DIR  Default: ${BACKEND_DIR}/.venv
  NODE_MAJOR       Default: 20
EOF
}

log_step() {
  printf '\n[setup] %s\n' "$1"
}

sudo_cmd() {
  if command -v sudo >/dev/null 2>&1; then
    sudo "$@"
  else
    "$@"
  fi
}

install_node() {
  local install_nodejs=1

  # Reuse the existing Node.js runtime when it already satisfies the baseline.
  if command -v node >/dev/null 2>&1; then
    local detected_major
    detected_major="$(node --version | sed -E 's/^v([0-9]+).*/\1/')"
    if [ "${detected_major}" -ge "${NODE_MAJOR}" ]; then
      install_nodejs=0
      log_step "Node.js $(node --version) is already available"
    fi
  fi

  if [ "${install_nodejs}" -eq 1 ]; then
    # Install a current LTS runtime for the CRA frontend and frontend build tasks.
    log_step "Installing Node.js ${NODE_MAJOR}.x from NodeSource"
    curl -fsSL "https://deb.nodesource.com/setup_${NODE_MAJOR}.x" | sudo_cmd bash -
    sudo_cmd apt-get install -y nodejs
  fi
}

prepare_runtime_directories() {
  # Create predictable runtime directories that later phases can reuse.
  log_step "Creating runtime directories"
  sudo_cmd mkdir -p \
    "${PROJECT_DIR}/logs" \
    "${PROJECT_DIR}/uploads" \
    "${PROJECT_DIR}/data"
}

prepare_backend() {
  if [ ! -d "${BACKEND_DIR}" ]; then
    log_step "Skipping backend setup because ${BACKEND_DIR} does not exist on this host"
    return
  fi

  # Isolate backend dependencies inside a project-local virtual environment.
  log_step "Creating backend virtual environment"
  python3 -m venv "${PYTHON_VENV_DIR}"

  # Install Python packages required by the FastAPI application.
  log_step "Installing backend Python dependencies"
  "${PYTHON_VENV_DIR}/bin/pip" install --upgrade pip
  "${PYTHON_VENV_DIR}/bin/pip" install -r "${BACKEND_DIR}/requirements.txt"
}

prepare_frontend() {
  if [ ! -f "${FRONTEND_DIR}/package.json" ]; then
    log_step "Skipping frontend dependency installation because ${FRONTEND_DIR}/package.json was not found"
    return
  fi

  # Install frontend packages so local development and future production builds are reproducible.
  log_step "Installing frontend JavaScript dependencies"
  (
    cd "${FRONTEND_DIR}"
    if [ -f "package-lock.json" ]; then
      npm ci
    else
      npm install
    fi
  )
}

main() {
  if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
    print_usage
    exit 0
  fi

  log_step "Updating apt package metadata"
  sudo_cmd apt-get update

  # Install the base toolchain needed by the Python backend and the React frontend.
  log_step "Installing base Ubuntu packages required by the project stack"
  sudo_cmd apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    git \
    build-essential \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    pkg-config \
    libssl-dev

  install_node
  prepare_runtime_directories
  prepare_backend
  prepare_frontend

  log_step "Setup completed successfully"
  printf '%s\n' \
    "Next steps:" \
    "  1. Copy .env.example to .env and provide real credentials." \
    "  2. Validate the host with bash scripts/verify.sh." \
    "  3. Continue with Phase 2 deployment tasks such as Nginx and process management."
}

main "$@"
