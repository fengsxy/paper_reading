#!/usr/bin/env python3
"""Run 5 DeepPlanning cases with MiniMax M2.7 baseline."""
import sys
import os
import json
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / 'travelplanning'))

MINIMAX_KEY = "sk-cp-G7Qi6okX-yju22CHZVQrFwWiVtyBmDpvkxnxnbzV-1ikPVU6ZWKVOxtEIwV63GECrD17rZzhZ1VEOCE0wX-hdqggeEcKVpjOIuOPnVjuzf69PPdsDpAa1BE"
os.environ['MINIMAX_API_KEY'] = MINIMAX_KEY

from travelplanning.agent.tools_fn_agent import run_agent_inference

output_dir = Path(__file__).parent / 'results' / 'minimax_5cases'
output_dir.mkdir(parents=True, exist_ok=True)

print(f"Running 5 cases with MiniMax M2.7...")

start = time.time()
result = run_agent_inference(
    model='minimax-m2.7',
    language='en',
    test_data_path=Path(__file__).parent / 'travelplanning' / 'data' / 'travelplanning_query_en_subset5.json',
    database_dir=Path(__file__).parent / 'travelplanning' / 'database' / 'database_en',
    tool_schema_path=Path(__file__).parent / 'travelplanning' / 'tools' / 'tool_schema_en.json',
    output_dir=output_dir,
    workers=1,
    max_llm_calls=150,
)

elapsed = time.time() - start

print(f"\n{'='*60}")
print(f"Results: {result['success']}/{result['total']} succeeded in {elapsed:.1f}s")

summary = {
    'model': 'minimax-m2.7',
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
        'final_plan_length': len(r.get('final_plan', '')),
    }
    summary['cases'].append(case_summary)

with open(output_dir / 'summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

# Print quick stats
for c in summary['cases']:
    print(f"  {c['id']}: {c['elapsed_time']:.1f}s, {c['final_plan_length']} chars, {'OK' if c['success'] else 'FAIL'}")
