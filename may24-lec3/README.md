# CMU 21-228 Discrete Mathematics — Lecture 3 Practice Problems
## Rearrangements, Multinomial Coefficients, Grid Paths, Pascal's Triangle, Induction

> **The rule:** Solve everything by hand. Show every step.
> Target: 1 hour total.
> ~15 min Topic 1, ~10 min Topic 2, ~20 min Topic 3, ~15 min Topic 4

---

## TOPIC 1 — Rearrangements and Over-counting

### Problem 1.1 — Basic rearrangement formula

How many ways can you rearrange the letters in the word **MISSISSIPPI**?

- M appears 1 time
- I appears 4 times
- S appears 4 times
- P appears 2 times

**Part A:** Write the formula. State what n is and what each kᵢ is.

**Part B:** Compute the answer. Show the full fraction before simplifying.

**Part C:** Verify using the "choose" method:
- First choose positions for the I's: C(11, 4)
- Then choose positions for the S's from remaining: C(7, 4)
- Then choose positions for the P's from remaining: C(3, 2)
- Then M takes the last spot: C(1, 1)
- Multiply all together. Verify it matches Part B.

---

### Problem 1.2 — The checkmark and X logic

**Part A:** Explain in your own words why C(7,3) equals the number of rearrangements of 3 checkmarks and 4 X's.

Write 2 sentences maximum. No symbols — plain English only.

**Part B:** Use this logic directly to compute C(10, 4) by thinking of it as rearranging 4 checkmarks and 6 X's.
Write the formula and compute.

**Part C:** A student claims C(10,4) = C(10,6). Are they right? Explain why using the checkmark-X argument — no algebra allowed.

---

### Problem 1.3 — When over-counting gives the same answer two ways

You want to arrange 2 red balls, 3 blue balls, and 1 green ball in a row.

**Part A:** Use the multinomial formula directly.

**Part B:** Use the iterative choose method:
- Choose positions for red balls first
- Then blue balls from remaining
- Then green ball takes the last spot

**Part C:** Verify both give the same answer. Show why they must always give the same answer in one sentence.

---

## TOPIC 2 — Binomial and Multinomial Theorems

### Problem 2.1 — Binomial theorem connection

**Part A:** In the expansion of (x + y)⁵, what is the coefficient of x²y³?

Explain in one sentence WHY this coefficient equals C(5,2) — connect it to choosing which parentheses give you an x.

**Part B:** What is the coefficient of x⁴y in (x + y)⁵?
What is the coefficient of xy⁴?
What do you notice about these two? Why?

**Part C:** What is the coefficient of x³ in (x + 2)⁵?
Hint: treat this as (x + y)⁵ where y = 2.

---

### Problem 2.2 — Multinomial theorem

**Part A:** In the expansion of (x + y + z)⁶, what is the coefficient of x²y²z²?

Write it as a rearrangement: how many ways to arrange 2 x-choices, 2 y-choices, 2 z-choices from 6 parentheses?

**Part B:** In the expansion of (x + y + z)⁴, find the coefficient of:
- x⁴ (all four parentheses give x)
- x²yz (two x's, one y, one z)
- x²y² (two x's, two y's)

**Part C:** Add up ALL the coefficients in (x + y + z)⁴.
Hint: set x = y = z = 1. What do you get? Why does this make sense?

---

## TOPIC 3 — Grid Path Combinatorics

### Problem 3.1 — Dynamic programming from scratch

Draw a 3×3 grid (3 columns, 3 rows of edges). Label the top vertex as START.

**Part A:** Fill in the Pascal's triangle numbers at every vertex by adding the two numbers directly above. Show every addition explicitly.

**Part B:** What is the total number of paths from top to bottom? Read it from your completed grid.

**Part C:** Verify using the formula: paths = C(total steps, left steps). Make sure it matches.

---

### Problem 3.2 — Missing edge: both methods

Take a 4×4 grid. There is one missing edge — the leftmost edge connecting row 2 to row 3.

**Method A — Subtraction:**

**Part A:** Total paths with no restriction = ?

**Part B:** Paths that use the missing edge = (paths to top of missing edge) × (paths from bottom of missing edge to end).
Compute each factor separately. Multiply.

**Part C:** Valid paths = Total − Bad. Compute.

**Method B — Dynamic programming:**

**Part D:** Draw the grid. Fill in Pascal's triangle numbers at every vertex. When you reach a vertex whose only incoming edge is the missing one — what do you write? Why?

**Part E:** Read the answer from the bottom of your grid. Verify it matches Part C.

**Part F (written):** In this problem, both methods worked equally well. In what situation would dynamic programming be better than subtraction? Write 2 sentences.

---

### Problem 3.3 — Two missing edges

A 4×4 grid has TWO missing edges:
- Edge A: the rightmost edge in row 2
- Edge B: the leftmost edge in row 3

**Part A:** Use dynamic programming (Pascal's triangle with missing edges). Draw the grid and fill in all vertex numbers. Show your work at each step.

**Part B:** Read the total valid paths from the bottom.

**Part C:** Now try the subtraction method.
|Valid paths| = Total − |through A| − |through B| + |through A AND B|

Compute each term. Verify you get the same answer as Part B.

**Part D (written):** Why do we add back |through A AND B|? What goes wrong without it?

---

## TOPIC 4 — Identities and Proof by Induction

### Problem 4.1 — Sum of binomial coefficients

**Part A:** Compute C(5,0) + C(5,1) + C(5,2) + C(5,3) + C(5,4) + C(5,5).
Do it by computing each term. What is the total?

**Part B:** Explain using the subset argument:
"If I have 5 objects and I want to count ALL possible subsets (including empty set and full set), each object is either IN or OUT..."
Complete this argument to prove the sum equals 2⁵.

**Part C:** Explain using the binomial theorem:
"Set x = 1 and y = 1 in (x+y)⁵..."
Complete this argument.

**Part D:** Which explanation do you find more satisfying? Why? (1-2 sentences)

---

### Problem 4.2 — Proof by induction for a recurrence

Recall from Lecture 2: let aₙ = number of n-digit strings from {1,2,3} with no two adjacent digits equal.

From Lecture 2 you found: aₙ = 3 × 2ⁿ⁻¹

**Prove this by induction.**

**Part A — Base case:** Verify the formula for n = 1.
Compute a₁ directly (list all valid 1-digit strings). Check it matches 3 × 2⁰.

**Part B — Inductive hypothesis:** State clearly what you are assuming.
Write: "Assume that for some n = k, aₖ = ..."

**Part C — Inductive step:** Prove aₖ₊₁ = 3 × 2ᵏ.
Use the recurrence aₙ₊₁ = 2aₙ (from Lecture 2).
Substitute the inductive hypothesis. Show the algebra.

**Part D (written):** The lecture said: "You can always just whack it with induction even if you don't know the matrix algebra." What does this mean? What does induction give you that the matrix method doesn't and vice versa?

---

### Problem 4.3 — Induction for the even/odd formula

The lecture proved: eₙ = (9ⁿ + (-1)ⁿ) / 2

where eₙ = number of n-digit numbers with no two adjacent equal digits that end in even.

**Prove this by induction using:**
- Recurrence: eₙ₊₁ = 4eₙ + 5oₙ
- Known fact: eₙ + oₙ = 9ⁿ (no restriction on parity, just no equal adjacent digits)

**Part A — Base case:** Verify e₁ = (9¹ + (-1)¹)/2 = 4. ✓

**Part B — Express oₙ in terms of the known facts:**
From eₙ + oₙ = 9ⁿ and the inductive hypothesis for eₙ, find oₙ.

**Part C — Substitute into the recurrence:**
eₙ₊₁ = 4eₙ + 5oₙ

Substitute your expressions for eₙ and oₙ. Collect the 9ⁿ terms and the (-1)ⁿ terms separately.

**Part D — Simplify:**
Show that what you get equals (9ⁿ⁺¹ + (-1)ⁿ⁺¹) / 2.

Hint: how many 9ⁿ terms do you have total? What is 9 × 9ⁿ?
For (-1)ⁿ terms: what is (-1) × (-1)ⁿ?

---

## BOSS PROBLEM — Everything Combined

This problem uses rearrangements, Pascal's triangle, and induction together.

A frog starts at the top of a triangular grid with n rows. At each step it can go left-down or right-down. After n steps it lands on one of the n+1 bottom vertices.

Let f(n, k) = number of paths that land on the k-th vertex from the left at the bottom (k goes from 0 to n).

**Part A:** Compute f(4, k) for all k = 0, 1, 2, 3, 4 using dynamic programming. Draw the triangle and fill in the numbers.

**Part B:** You should recognize these numbers. What are they? Write f(n, k) as a binomial coefficient.

**Part C:** Prove by induction that f(n, k) = C(n, k).

Base case: f(1, 0) = 1 and f(1, 1) = 1. Verify both equal C(1,0) and C(1,1).

Inductive step: use the recurrence f(n+1, k) = f(n, k-1) + f(n, k) and the inductive hypothesis to show f(n+1, k) = C(n+1, k).

Hint: you will need Pascal's identity: C(n, k-1) + C(n, k) = C(n+1, k). Prove this identity algebraically first.

**Part D:** Using f(n, k) = C(n, k), find the total number of paths to ALL bottom vertices.
Sum C(n, k) for k = 0 to n. Use the identity from Topic 4 to simplify.

What does this answer mean in terms of paths?

**Part E (written):** The lecture connected Pascal's triangle to grid paths to binomial coefficients to the binomial theorem. In 3 sentences, explain this chain of connections in your own words — no symbols.

---

## Mastery Checklist

You have internalized Lecture 3 when you can:

- [ ] Apply the multinomial formula n!/(k₁!k₂!...kₘ!) to any rearrangement problem
- [ ] Solve the same rearrangement problem using the iterative choose method
- [ ] Verify both methods give the same answer and explain why they must
- [ ] Explain C(n,k) as a rearrangement of checkmarks and X's in one sentence
- [ ] State why C(n,k) = C(n, n-k) using the checkmark-X argument
- [ ] Find any coefficient in (x+y)ⁿ or (x+y+z)ⁿ using the multinomial argument
- [ ] Fill in Pascal's triangle on any grid using dynamic programming
- [ ] Handle missing edges in the grid by leaving that vertex count unchanged
- [ ] Apply subtraction method: valid = total − bad
- [ ] Apply inclusion-exclusion for two missing edges
- [ ] State when dynamic programming is better than subtraction
- [ ] Prove sum of row of Pascal's triangle = 2ⁿ using both subset argument and binomial theorem
- [ ] Write a complete proof by induction with base case, hypothesis, and step
- [ ] Explain the difference between what induction gives vs what matrix algebra gives

---

*CMU 21-228 Discrete Mathematics*
*Math practice only — no computation*
*Lecture 3: Rearrangements, Multinomial Theorem, Grid Paths, Induction*

generated by claude to fully internalize the lecture 3 
