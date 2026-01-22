#!/bin/bash
# Quick folder backup script
SRC_DIR="${1:-.}"
OUT="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$OUT" "$SRC_DIR"
echo "Saved $OUT"