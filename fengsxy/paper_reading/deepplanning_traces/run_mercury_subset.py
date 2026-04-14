#!/usr/bin/env python3
"""
Simple Mercury 2 validation on 5 DeepPlanning cases.
Run: python run_mercury_subset.py
"""
import sys
import os
import json
import time
from pathlib import Path

# Add project paths
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / 'travelplanning'))

# Load env
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / '.env')

# Check API key
api_key = os.getenv('INCEPTION_API_KEY')
if not api_key:
    print("ERROR: INCEPTION_API_KEY not set in .env")
    sys.exit(1)

print(f"INCEPTION_API_KEY: {api_key[:20]}...")

# Run the 5-case subset
from travelplanning.agent.tools_fn_agent import run_agent_inference

output_dir = Path(__file__).parent / 'results' / 'mercury_5cases'
output_dir.mkdir(parents=True, exist_ok=True)

print(f"\nOutput: {output_dir}")
print(f"Running 5 cases with mercury-2...\n")

start = time.time()
result = run_agent_inference(
    model='mercury-2',
    language='en',
    test_data_path=Path(__file__).parent / 'travelplanning' / 'data' / 'travelplanning_query_en_subset5.json',
    database_dir=Path(__file__).parent / 'travelplanning' / 'database' / 'database_en',
    tool_schema_path=Path(__file__).parent / 'travelplanning' / 'tools' / 'tool_schema_en.json',
    output_dir=output_dir,
    workers=1,          # Run sequentially for mercury
    max_llm_calls=150,
)

elapsed = time.time() - start

print(f"\n{'='*60}")
print(f"Results: {result['success']}/{result['total']} succeeded in {elapsed:.1f}s")
print(f"Output: {output_dir}")

# Save summary
summary = {
    'model': 'mercury-2',
    'total': result['total'],
    'success': result['success'],
    'failed': result['failed'],
    'elapsed_time': elapsed,
    'cases': []
}

for r in result.get('results', []):
    case_summary = {
        'id': r.get('id'),
        'success': r.get('success'),
        'elapsed_time': r.get('elapsed_time', 0),
    }
    if r.get('success'):
        case_summary['final_plan_length'] = len(r.get('final_plan', ''))
    summary['cases'].append(case_summary)

with open(output_dir / 'summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\nSummary saved to {output_dir / 'summary.json'}")
