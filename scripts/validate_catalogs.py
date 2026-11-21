#!/usr/bin/env python3
"""Validate GAME ROOM BR FPKGi-style catalog JSON files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

OPTIONAL_TEXT_FIELDS = (
    "title_id",
    "region",
    "version",
    "release",
    "min_fw",
    "cover_url",
    "developer",
    "license",
    "source_url",
    "official_sha256",
)
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def _https_url(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_document(
    path: str,
    document: object,
    seen_urls: dict[str, str] | None = None,
) -> tuple[list[str], int]:
    """Return (errors, item_count) for one catalog document."""
    errors: list[str] = []
    if not isinstance(document, dict):
        return [f"{path}: JSON root must be an object"], 0

    data = document.get("DATA")
    if not isinstance(data, dict):
        return [f"{path}: required root member 'DATA' must be an object"], 0

    seen = seen_urls if seen_urls is not None else {}
    for pkg_url, metadata in data.items():
        label = f"{path} [{pkg_url}]"
        if not isinstance(pkg_url, str) or not _https_url(pkg_url):
            errors.append(f"{label}: PKG URL must be a valid HTTPS URL")
            continue

        parsed = urlparse(pkg_url)
        if not parsed.path.lower().endswith(".pkg"):
            errors.append(f"{label}: URL path must end in .pkg")

        normalized_url = pkg_url.strip()
        previous = seen.get(normalized_url)
        if previous:
            errors.append(f"{label}: duplicate PKG URL also listed in {previous}")
        else:
            seen[normalized_url] = path

        if not isinstance(metadata, dict):
            errors.append(f"{label}: metadata must be an object")
            continue

        name = metadata.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}: required field 'name' must be non-empty text")

        size = metadata.get("size")
        valid_size = (
            isinstance(size, int) and not isinstance(size, bool) and size > 0
        ) or (
            isinstance(size, str) and size.isdigit() and int(size) > 0
        )
        if not valid_size:
            errors.append(f"{label}: required field 'size' must be a positive byte count")

        for field in OPTIONAL_TEXT_FIELDS:
            if field in metadata and metadata[field] is not None and not isinstance(metadata[field], str):
                errors.append(f"{label}: field '{field}' must be text or null")

        for field in ("cover_url", "source_url"):
            value = metadata.get(field)
            if value is not None and not _https_url(value):
                errors.append(f"{label}: field '{field}' must be a valid HTTPS URL")

        digest = metadata.get("official_sha256")
        if digest is not None and isinstance(digest, str) and not SHA256_RE.fullmatch(digest):
            errors.append(f"{label}: 'official_sha256' must contain exactly 64 hexadecimal characters")

    return errors, len(data)


def validate_repository(root: Path) -> tuple[list[str], int, int]:
    catalog_files = sorted(root.rglob("*.json"))
    if not catalog_files:
        return ["No catalog JSON files found"], 0, 0

    errors: list[str] = []
    total_items = 0
    seen_urls: dict[str, str] = {}

    for file_path in catalog_files:
        relative_path = file_path.relative_to(root).as_posix()
        try:
            with file_path.open("r", encoding="utf-8") as stream:
                document = json.load(stream)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"{relative_path}: cannot read valid UTF-8 JSON ({exc})")
            continue

        file_errors, item_count = validate_document(relative_path, document, seen_urls)
        errors.extend(file_errors)
        total_items += item_count

    return errors, len(catalog_files), total_items


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="catalog repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()

    errors, file_count, item_count = validate_repository(args.root)
    if errors:
        print("CATALOG VALIDATION FAILED")
        for error in errors:
            print(f" - {error}")
        print(f"Checked {file_count} JSON files; found {item_count} entries.")
        return 1

    print(f"CATALOG VALIDATION PASSED: {file_count} JSON files, {item_count} entries.")
    print("Note: this checks JSON structure and URL format, not remote file availability or PKG bytes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
