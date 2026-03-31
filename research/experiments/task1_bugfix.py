"""
Task 1: Bug Fix — Binary Search with Off-by-One Error

The agent must find and fix the bug in this implementation.
There are TWO bugs: an off-by-one in the boundary check, and a wrong return value.
"""

# --- BUGGY CODE (give this to the agent) ---
BUGGY_CODE = '''
def binary_search(arr, target):
    """Return the index of target in sorted array arr, or -1 if not found."""
    left, right = 0, len(arr)  # BUG 1: should be len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0  # BUG 2: should return -1
'''

# --- TEST CASES ---
TEST_CASES = [
    ([1, 3, 5, 7, 9], 5, 2),
    ([1, 3, 5, 7, 9], 1, 0),
    ([1, 3, 5, 7, 9], 9, 4),
    ([1, 3, 5, 7, 9], 4, -1),
    ([1, 3, 5, 7, 9], 0, -1),
    ([1, 3, 5, 7, 9], 10, -1),
    ([], 1, -1),
    ([1], 1, 0),
    ([1], 2, -1),
    ([1, 2], 2, 1),
]

CORRECT_CODE = '''
def binary_search(arr, target):
    """Return the index of target in sorted array arr, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
'''

def evaluate_fix(agent_code: str) -> dict:
    """Run test cases against agent's fixed code. Returns score dict."""
    namespace = {}
    try:
        exec(agent_code, namespace)
    except Exception as e:
        return {"compiled": False, "error": str(e), "passed": 0, "total": len(TEST_CASES), "score": 0.0}
    
    func = namespace.get("binary_search")
    if not func:
        return {"compiled": True, "error": "function not found", "passed": 0, "total": len(TEST_CASES), "score": 0.0}
    
    passed = 0
    failures = []
    for arr, target, expected in TEST_CASES:
        try:
            result = func(arr, target)
            if result == expected:
                passed += 1
            else:
                failures.append(f"binary_search({arr}, {target}) = {result}, expected {expected}")
        except Exception as e:
            failures.append(f"binary_search({arr}, {target}) raised {e}")
    
    return {
        "compiled": True,
        "passed": passed,
        "total": len(TEST_CASES),
        "score": passed / len(TEST_CASES),
        "failures": failures[:5]  # limit output
    }

if __name__ == "__main__":
    # Verify correct code passes all tests
    result = evaluate_fix(CORRECT_CODE)
    print(f"Correct code: {result['passed']}/{result['total']} passed")
    assert result["score"] == 1.0, f"Correct code failed: {result}"
    
    # Verify buggy code fails
    result = evaluate_fix(BUGGY_CODE)
    print(f"Buggy code: {result['passed']}/{result['total']} passed")
    assert result["score"] < 1.0, "Buggy code should fail some tests"
    print("Task validation OK")
