#!/usr/bin/env python3
"""
Simple test to verify output.csv exists and has expected columns.
"""

import sys
import csv
from pathlib import Path

def test_output_exists():
    out_path = Path("output.csv")
    assert out_path.exists(), "output.csv does not exist"
    print("✓ output.csv exists")

def test_output_structure():
    out_path = Path("output.csv")
    with open(out_path) as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        # We expect at least some columns; check non-empty
        assert fields and len(fields) > 0, "CSV has no header"
        print(f"✓ CSV header: {fields}")
        # Check at least one data row
        rows = list(reader)
        assert len(rows) > 0, "CSV has no data rows"
        print(f"✓ {len(rows)} data rows")

if __name__ == "__main__":
    try:
        test_output_exists()
        test_output_structure()
        print("All checks passed.")
        sys.exit(0)
    except AssertionError as e:
        print(f"❌ {e}")
        sys.exit(1)