"""
validate.py — Crafty framework: company state validator.

Scans all markdown files under company/execution/ and company/strategy/okr/,
extracts YAML frontmatter, and validates each against its JSON Schema
in crafty/schemas/.

Usage (from workspace root):
    python crafty/scripts/validate.py

Requirements:
    pip install jsonschema pyyaml
"""

import json
import sys
from pathlib import Path

import datetime

import yaml
from jsonschema import Draft202012Validator, ValidationError

# ── Paths ─────────────────────────────────────────────────────────────────────

# crafty/scripts/ → crafty/ → workspace root
ROOT = Path(__file__).parent.parent.parent
SCHEMAS_DIR = ROOT / "crafty" / "schemas"
SCAN_DIRS = [
    ROOT / "company" / "execution",
    ROOT / "company" / "strategy" / "okr",
]

# ── Schema registry ────────────────────────────────────────────────────────────

SCHEMA_MAP = {
    "objective":   SCHEMAS_DIR / "objective.schema.json",
    "key_result":  SCHEMAS_DIR / "key_result.schema.json",
    "initiative":  SCHEMAS_DIR / "initiative.schema.json",
    "project":     SCHEMAS_DIR / "project.schema.json",
    "task":        SCHEMAS_DIR / "task.schema.json",
}


def load_schema(doc_type: str) -> dict | None:
    path = SCHEMA_MAP.get(doc_type)
    if not path or not path.exists():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


# ── Frontmatter extraction ─────────────────────────────────────────────────────

def extract_frontmatter(md_path: Path) -> dict | None:
    """Parse YAML frontmatter delimited by '---' blocks."""
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return None

    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break

    if end is None:
        return None

    raw_yaml = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(raw_yaml)
        return _coerce_dates(data)
    except yaml.YAMLError as exc:
        print(f"  YAML parse error: {exc}")
        return None


def _coerce_dates(obj):
    """Recursively convert datetime.date / datetime.datetime to ISO strings."""
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _coerce_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_coerce_dates(i) for i in obj]
    return obj


# ── Validation ─────────────────────────────────────────────────────────────────

def validate_file(md_path: Path) -> list[str]:
    """Return a list of error strings for this file (empty = valid)."""
    errors = []

    frontmatter = extract_frontmatter(md_path)
    if frontmatter is None:
        errors.append("Missing or unparseable YAML frontmatter.")
        return errors

    doc_type = frontmatter.get("type")
    if not doc_type:
        errors.append("Missing 'type' field in frontmatter.")
        return errors

    schema = load_schema(doc_type)
    if schema is None:
        errors.append(f"No schema found for type '{doc_type}'.")
        return errors

    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(frontmatter), key=lambda e: e.path):
        path = " → ".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"[{path}] {error.message}")

    return errors


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> int:
    all_files = []
    for scan_dir in SCAN_DIRS:
        all_files.extend(scan_dir.rglob("*.md"))

    if not all_files:
        print("No markdown files found to validate.")
        return 0

    total = 0
    failed = 0

    for md_path in sorted(all_files):
        rel = md_path.relative_to(ROOT)
        errors = validate_file(md_path)
        total += 1

        if errors:
            failed += 1
            print(f"\n❌  {rel}")
            for err in errors:
                print(f"    • {err}")
        else:
            print(f"✓   {rel}")

    print(f"\n{'─' * 50}")
    print(f"Validated {total} file(s). {failed} failed, {total - failed} passed.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
