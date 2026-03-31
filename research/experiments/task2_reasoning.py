"""
Task 2: Multi-step reasoning — requires chaining logic, not just lookup.
"""

QUESTION = """
A farmer has a field that is 120 meters long and 80 meters wide. 
He wants to divide it into the largest possible square plots with no land left over.
How many square plots will he have, and what is the side length of each plot?
"""

CORRECT_ANSWER = {
    "side_length": 40,  # GCD(120, 80) = 40
    "num_plots": 6,     # (120/40) * (80/40) = 3 * 2 = 6
}

def evaluate_answer(agent_response: str) -> dict:
    """Check if agent got both the side length and number of plots correct."""
    response_lower = agent_response.lower()
    
    got_side = "40" in agent_response
    got_count = "6" in agent_response
    
    # Check for GCD/reasoning mention
    mentions_gcd = any(w in response_lower for w in ["gcd", "greatest common divisor", "最大公约数", "最大公因数", "辗转相除"])
    
    return {
        "correct_side_length": got_side,
        "correct_num_plots": got_count,
        "shows_reasoning": mentions_gcd,
        "score": (1.0 if got_side and got_count else 0.5 if got_side or got_count else 0.0),
    }
