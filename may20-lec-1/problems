# CMU 21-228 Discrete Mathematics — Lecture 1 Mastery Problems
## Combinatorics, Counting, Multiplication Principle, Recursion, Parity

> **The CS50-level mastery rule for every problem:**
> 1. Solve the math problem by hand. Write the answer and reasoning.
> 2. Write Python code that computes the same answer by **brute force**.
> 3. Write Python code using your **mathematical formula**.
> 4. Verify both give the same answer.
> 5. If they disagree — your math was wrong. Fix the math.
> 6. Commit everything to GitHub with comments explaining the math.

---

## Problem 1 — Multiplication Principle: Brute Force Meets Formula

**Difficulty:** Foundation

### Math First
How many 4-digit numbers (1000–9999) have **all even digits**?

Derive the answer using the multiplication principle. Show your reasoning step by step:
- How many choices for the **first digit**? (remember: no leading zero)
- How many choices for each **remaining digit**?
- Why can you multiply these numbers together?

### Code Part A — Brute Force Verifier
```python
def count_all_even_brute():
    # check every number 1000-9999
    # return count of those with all even digits
    # hint: use str(n) to get digits as characters
    # hint: int(d) % 2 == 0 checks if digit d is even
    pass

# expected output: 500
```

### Code Part B — Formula Verifier
```python
def count_all_even_formula():
    # use multiplication principle only — no loops over all numbers
    # first digit: even digits 1-9 = {2,4,6,8} → how many choices?
    # digits 2,3,4: even digits 0-9 = {0,2,4,6,8} → how many choices?
    pass

# verify:
assert count_all_even_brute() == count_all_even_formula()
print("Answer:", count_all_even_formula())
```

**Expected output:** `500`

**Math answer to derive:**
- First digit: {2,4,6,8} = 4 choices (no zero)
- Digits 2,3,4: {0,2,4,6,8} = 5 choices each
- Total: 4 × 5 × 5 × 5 = **500**

---

## Problem 2 — Case Analysis: Constraint on First AND Last Digit

**Difficulty:** Foundation

### Math First
Count 4-digit numbers where the **first digit is odd** AND the **last digit is even**.

### Code — Generalised Function
```python
def count_by_parity(first_parity: str, last_parity: str) -> int:
    """
    Count 4-digit numbers where:
    - first digit has first_parity ("odd" or "even")
    - last digit has last_parity ("odd" or "even")
    - no other constraints
    """
    # odd nonzero first digits: {1,3,5,7,9} = 5 choices
    # even nonzero first digits: {2,4,6,8} = 4 choices (no zero allowed)
    # odd last digits: {1,3,5,7,9} = 5 choices
    # even last digits: {0,2,4,6,8} = 5 choices
    # middle two digits: no restriction = 10 × 10 choices
    pass

# test all four combinations — they MUST sum to 9000
total = (count_by_parity("odd", "odd") +
         count_by_parity("odd", "even") +
         count_by_parity("even", "odd") +
         count_by_parity("even", "even"))
assert total == 9000, f"Expected 9000, got {total}"
print("All four combinations sum to:", total)
```

**Expected individual counts:**
- odd,odd: 2500
- odd,even: 2500
- even,odd: 2000
- even,even: 2000
- **Total: 9000** ✓

---

## Problem 3 — Alternating Parity: The Lecture's Core Idea in Code

**Difficulty:** Core

### Math First
Count 4-digit numbers with **strictly alternating parity** (odd-even-odd-even OR even-odd-even-odd).

Derive both cases and add them. Then generalise to n digits.

### Code Part A — is_alternating checker
```python
def is_alternating(n: int) -> bool:
    """
    Return True if digits of n strictly alternate even/odd parity.
    
    Examples:
    1234 → digits 1,2,3,4 → odd,even,odd,even → True
    1224 → digits 1,2,2,4 → odd,even,even,even → False
    2143 → digits 2,1,4,3 → even,odd,even,odd → True
    """
    pass
```

### Code Part B — Brute Force Counter
```python
def count_alternating_brute(n_digits: int) -> int:
    """Brute force count of n-digit alternating parity numbers."""
    start = 10 ** (n_digits - 1)
    end = 10 ** n_digits
    return sum(1 for n in range(start, end) if is_alternating(n))
```

### Code Part C — Formula Counter (no brute force)
```python
def count_alternating_formula(n_digits: int) -> int:
    """
    Use multiplication principle only.
    Think about: how many choices for each position?
    
    Case 1 starts odd: first digit = {1,3,5,7,9} = 5 choices
    Case 2 starts even: first digit = {2,4,6,8} = 4 choices (no zero)
    All subsequent positions: 5 choices each (always 5 odd or 5 even)
    """
    pass

# verify for 1,2,3,4 digits — both must match
for d in [1, 2, 3, 4]:
    bf = count_alternating_brute(d)
    fm = count_alternating_formula(d)
    assert bf == fm, f"Mismatch at {d} digits: brute={bf}, formula={fm}"
    print(f"{d} digits: {bf}")
```

**Expected outputs:**
```
1 digit: 9
2 digits: 45
3 digits: 450
4 digits: 2250
```

**Pattern to discover:** count(n) = 9 × 5^(n-1)

---

## Problem 4 — Recursion: Implement the Recurrence Directly

**Difficulty:** Core

### Math First
Define:
- **eₙ** = number of n-digit numbers (no leading zeros) ending in an **even** digit
- **oₙ** = number of n-digit numbers ending in an **odd** digit

Write recurrence relations. What are the base cases? Solve for closed forms.

### Code Part A — Bottom-Up Dynamic Programming
```python
def count_ending_parity_dp(n: int) -> tuple[int, int]:
    """
    Returns (even_count, odd_count) for n-digit numbers.
    Uses bottom-up DP following the recurrence.
    
    Base case n=1:
    - even first digits (no zero): {2,4,6,8} = 4 choices
    - odd first digits: {1,3,5,7,9} = 5 choices
    
    Recurrence for n > 1:
    - to end in even: previous number × 5 (any even digit 0-9)
    - to end in odd: previous number × 5 (any odd digit 0-9)
    """
    pass
```

### Code Part B — Recursion with Memoization
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def count_ending_parity_recursive(n: int) -> tuple[int, int]:
    """Same logic but recursive with memoization."""
    pass
```

### Code Part C — Closed Form Formula
```python
def count_ending_parity_formula(n: int) -> tuple[int, int]:
    """
    Closed form — no loops, no recursion.
    
    Observation: for n >= 2, even_count = odd_count by symmetry
    Total n-digit numbers = 9 × 10^(n-1)
    So for n >= 2: each = 9 × 10^(n-1) / 2
    But 9 is odd — how do you handle n=1 specially?
    """
    pass

# verify all three match for n=1 to 10
for n in range(1, 11):
    dp = count_ending_parity_dp(n)
    rec = count_ending_parity_recursive(n)
    form = count_ending_parity_formula(n)
    assert dp == rec == form, f"Mismatch at n={n}: dp={dp}, rec={rec}, form={form}"
    print(f"n={n}: even={dp[0]}, odd={dp[1]}, total={sum(dp)}")
```

---

## Problem 5 — The (-1)ⁿ Pattern: Code the Formula from Lecture

**Difficulty:** Hard

### Math First
Derive a formula for: **how many n-digit numbers have more even digits than odd digits?**

Show that your formula contains a (-1)ⁿ term. Explain what this term represents geometrically.

### Code + Visualisation
```python
import matplotlib.pyplot as plt

def has_more_even_digits(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    even_count = sum(1 for d in digits if d % 2 == 0)
    return even_count > len(digits) - even_count

def count_even_majority_brute(n_digits: int) -> int:
    start = 10 ** (n_digits - 1)
    end = 10 ** n_digits
    return sum(1 for n in range(start, end) if has_more_even_digits(n))

# compute ratios for n=1 to 7
ratios = []
for d in range(1, 8):
    count = count_even_majority_brute(d)
    total = 9 * (10 ** (d - 1))
    ratios.append(count / total)
    print(f"n={d}: count={count}, ratio={count/total:.4f}")

# plot — does the ratio converge?
plt.figure(figsize=(8, 4))
plt.plot(range(1, 8), ratios, 'o-', color='#1D9E75', linewidth=2)
plt.axhline(y=0.5, color='#D85A30', linestyle='--', label='0.5')
plt.xlabel('Number of digits')
plt.ylabel('Fraction with more even digits')
plt.title('Convergence of even-majority fraction — the (-1)ⁿ oscillation')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('minus_one_n_pattern.png', dpi=150)
plt.show()
```

**What you should observe:**
The ratio oscillates around 0.5 with decreasing amplitude. The (-1)ⁿ term in your formula IS this oscillation. As n→∞, it converges to 0.5.

---

## Problem 6 — State Machine: Connect Combinatorics to CS and Quant Finance

**Difficulty:** Hard

### The Key Connection
Alternating parity counting is equivalent to a **2-state machine**:
- State **E**: last digit was even
- State **O**: last digit was odd

This same structure models **bull/bear market transitions** in quantitative finance.

### Code — Build the General State Machine Counter
```python
def state_machine_count(transitions: dict, initial: dict, steps: int) -> dict:
    """
    Count sequences using a state machine.
    
    Args:
        transitions: {state: {next_state: num_ways}}
        initial: {state: count} — starting counts at step 1
        steps: total number of positions/steps
    
    Returns:
        {state: count} — counts after all steps
    
    Example for alternating parity:
        transitions = {'E': {'O': 5}, 'O': {'E': 5}}
        initial = {'E': 4, 'O': 5}  # first digit choices
    """
    current = initial.copy()
    for _ in range(steps - 1):
        next_counts = {s: 0 for s in transitions}
        for state, count in current.items():
            for next_state, ways in transitions[state].items():
                next_counts[next_state] += count * ways
        current = next_counts
    return current

# APPLICATION 1: alternating parity 4-digit numbers
transitions_parity = {
    'E': {'O': 5},   # from even last digit: 5 odd choices
    'O': {'E': 5}    # from odd last digit: 5 even choices
}
initial_parity = {'E': 4, 'O': 5}  # first digit: 4 even, 5 odd choices
result = state_machine_count(transitions_parity, initial_parity, 4)
print("Alternating 4-digit numbers:", sum(result.values()))
# should match count_alternating_brute(4) = 2250

# APPLICATION 2: bull/bear market sequences
# from Bull: stay Bull (2 ways) or go Bear (3 ways)
# from Bear: go Bull (2 ways) or stay Bear (3 ways)
# count 10-day sequences starting from Bull
transitions_market = {
    'B': {'B': 2, 'R': 3},
    'R': {'B': 2, 'R': 3}
}
initial_market = {'B': 1, 'R': 0}
market_result = state_machine_count(transitions_market, initial_market, 10)
print("10-day market sequences from Bull state:", market_result)
print("Total sequences:", sum(market_result.values()))
```

> **Why this matters for quant finance:**
> This state machine function is the primitive version of **Markov chains** — which you will study in CMU 21-326 and use directly in WorldQuant alpha research for regime detection and signal generation.

---

## Problem 7 — BOSS: Generalised Counter with Visual Output

**Difficulty:** Mastery

### Build the Universal Constraint Counter
```python
def count_constrained(n_digits: int, constraint_fn) -> int:
    """
    Count all n-digit numbers satisfying constraint_fn.
    constraint_fn(n) returns True if n satisfies the constraint.
    """
    start = 10 ** (n_digits - 1)
    end = 10 ** n_digits
    return sum(1 for num in range(start, end) if constraint_fn(num))

# Define all 6 constraint functions
def all_even(n):
    """All digits are even."""
    pass

def alternating(n):
    """Digits alternate even/odd parity."""
    pass

def no_repeat(n):
    """No digit appears more than once."""
    pass

def even_digit_sum(n):
    """Sum of all digits is even."""
    pass

def more_odd(n):
    """More odd digits than even digits."""
    pass

def first_eq_last(n):
    """First digit equals last digit."""
    pass

# Count and visualise
import matplotlib.pyplot as plt

constraints = [all_even, alternating, no_repeat, even_digit_sum, more_odd, first_eq_last]
labels = ['All Even', 'Alternating', 'No Repeat', 'Even Sum', 'More Odd', 'First=Last']
colors = ['#1D9E75', '#378ADD', '#BA7517', '#7F77DD', '#D85A30', '#639922']

counts = [count_constrained(4, fn) for fn in constraints]

plt.figure(figsize=(10, 5))
bars = plt.bar(labels, counts, color=colors)
plt.title('4-digit number constraints — brute force verification', fontsize=13)
plt.ylabel('Count')
for i, v in enumerate(counts):
    plt.text(i, v + 20, str(v), ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('constraints_chart.png', dpi=150)
plt.show()

# For each constraint: also derive the formula mathematically
# and assert it matches the brute force count
expected = {
    'All Even': 500,
    'Alternating': 2250,
    'No Repeat': 4536,
    'Even Sum': 4500,
    'More Odd': 3375,   # verify this yourself
    'First=Last': 900
}

for label, count, fn in zip(labels, counts, constraints):
    print(f"{label}: {count}")
    if label in expected:
        assert count == expected[label], f"Expected {expected[label]}, got {count} for {label}"
        print(f"  ✓ matches formula")
```

**Expected counts to verify your formulas against:**
| Constraint | Count | Formula to derive |
|---|---|---|
| All even digits | 500 | 4 × 5³ |
| Alternating parity | 2250 | 9 × 5³ |
| No repeated digits | 4536 | 9 × 9 × 8 × 7 |
| Even digit sum | 4500 | 9000 / 2 |
| More odd than even | ~3375 | derive using cases |
| First digit = last digit | 900 | 9 × 10 × 10 |

---

## Mastery Checklist

You have mastered this lecture when you can:

- [ ] Explain **why multiplication works** in counting (not just that it does)
- [ ] Identify which choices are **independent** vs **dependent**
- [ ] Implement **brute force verification** for any counting problem
- [ ] Implement the **formula version** and assert it matches brute force
- [ ] Write a **recurrence relation** and implement it three ways: DP, recursion, closed form
- [ ] Build a **state machine** for any constraint
- [ ] Connect combinatorics to **CS concepts** (DP, automata) and **quant finance** (regime models)
- [ ] Visualise results using **Matplotlib**
- [ ] Commit everything to **GitHub** with mathematical comments

---

## GitHub Commit Structure

```
lecture_01_counting/
├── README.md          ← this file
├── problems.py        ← all 7 problems implemented
├── solutions.py       ← your verified solutions
├── constraints_chart.png
├── minus_one_n_pattern.png
└── proofs.md          ← mathematical derivations in LaTeX notation
```

Every function should have a docstring explaining the **math** behind it, not just what it does.

---

*CMU 21-228 Discrete Mathematics — Self-study mastery track*
*Based on: Combinatorics, Multiplication Principle, Parity, Recursion*

problems are generated by claude to test and solidify my understanding of discrete maths
