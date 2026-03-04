#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="${PROJECT_DIR:-/var/www/NoteWeb}"
BACKEND_DIR="${BACKEND_DIR:-${PROJECT_DIR}/backendSrc}"
PYTHON_VENV_DIR="${PYTHON_VENV_DIR:-${BACKEND_DIR}/.venv}"

print_usage() {
  cat <<'EOF'
Usage: bash scripts/verify.sh

Performs a lightweight verification of the Ubuntu runtime expected by the
NoteWeb project. The script checks command availability, reports versions,
and verifies that runtime directories and the backend virtual environment exist.
EOF
}

report_command() {
  local command_name="$1"

  if command -v "${command_name}" >/dev/null 2>&1; then
    printf '[ok] %s: %s\n' "${command_name}" "$("${command_name}" --version 2>&1 | head -n 1)"
  else
    printf '[missing] %s\n' "${command_name}"
  fi
}

report_path() {
  local path_name="$1"

  if [ -e "${path_name}" ]; then
    printf '[ok] %s\n' "${path_name}"
  else
    printf '[missing] %s\n' "${path_name}"
  fi
}

main() {
  if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
    print_usage
    exit 0
  fi

  report_command node
  report_command npm
  report_command python3
  report_command pip

  report_path "${PROJECT_DIR}/logs"
  report_path "${PROJECT_DIR}/uploads"
  report_path "${PROJECT_DIR}/data"
  report_path "${PYTHON_VENV_DIR}"
}

main "$@"
