#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"

RESET="\e[0m"
BOLD="\e[1m"
DIM="\e[2m"
PINK="\e[35m"
YELLOW="\e[33m"

ui_line() {
    printf '%b\n' "${PINK}---------------------------------------------------------------------${RESET}"
}

ui_header() {
    printf '\n%b\n' "${PINK}${BOLD}  ANTO426 GRUB THEME INSTALLER${RESET}"
    printf '%b\n' "${DIM}  Preset: anto426, color icons, ${ANTO426_GRUB_RESOLUTION:-${ANTO426_GRUB_SCREEN:-1080p}}.${RESET}"
    ui_line
}

ui_header

args=(-t anto426 -i color)

if [[ -n "${ANTO426_GRUB_RESOLUTION:-}" ]]; then
    args+=(-c "$ANTO426_GRUB_RESOLUTION")
else
    args+=(-s "${ANTO426_GRUB_SCREEN:-1080p}")
fi

if [[ "${ANTO426_GRUB_BOOT:-0}" == "1" ]]; then
    args+=(-b)
fi

exec "$script_dir/install.sh" "${args[@]}" "$@"
