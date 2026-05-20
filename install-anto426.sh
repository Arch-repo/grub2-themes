#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"

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
