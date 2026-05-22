# CMU 21-228 Discrete Mathematics — Lecture 2 Practice Problems
## Linear Recurrences, Matrix Powers, Grid Paths, Subtraction Method

> **The rule:** Solve everything by hand. Show every step.
> Target: 1 hour total. Spend ~30 min on Topic 1, ~30 min on Topic 2.
> If you can solve all of these without looking at notes — lecture is internalized.

---

## TOPIC 1 — Linear Recurrences and Matrix Algebra

### Problem 1.1 — Warm up: set up the recurrence

Count n-digit strings using digits {0,1,2,3,4,5,6,7,8,9} with:
- No two adjacent digits equal
- Last digit is **divisible by 3** (i.e. in {0,3,6,9})

Let dₙ = count of such strings ending in a digit divisible by 3.
Let fₙ = count of such strings ending in a digit NOT divisible by 3.

**Part A:** Find d₁ and f₁ (base cases).
Hint: For n=1, no leading zero restriction — all 10 digits allowed.

**Part B:** Write the recurrence relations for dₙ₊₁ and fₙ₊₁.
For each: think about what the previous digit could have been and how many choices you have for the next digit.

**Part C:** Verify your recurrence by computing d₂ and f₂ two ways:
- Using the recurrence formula
- Directly counting 2-digit strings

---

### Problem 1.2 — Matrix representation

Using the recurrence from Problem 1.1:

**Part A:** Write the matrix equation:
$$\begin{bmatrix} d_{n+1} \\ f_{n+1} \end{bmatrix} = M \begin{bmatrix} d_n \\ f_n \end{bmatrix}$$

What is M?

**Part B:** Write the general formula:
$$\begin{bmatrix} d_n \\ f_n \end{bmatrix} = M^{n-1} \begin{bmatrix} d_1 \\ f_1 \end{bmatrix}$$

**Part C:** Compute M² by hand (matrix multiplication).
Then compute d₃ and f₃ using M² × [d₁, f₁]ᵀ.
Verify against the recurrence: d₃ = 3·d₂ + 4·f₂ (or whatever your recurrence says).

---

### Problem 1.3 — Eigenvalues and diagonalization

For the matrix from lecture:
$$M = \begin{bmatrix} 4 & 5 \\ 5 & 4 \end{bmatrix}$$

**Part A:** Find the eigenvalues of M.
Method: solve det(M - λI) = 0.
Show the characteristic polynomial and its roots.

**Part B:** For each eigenvalue, find the eigenvector.
Method: solve (M - λI)v = 0 for each λ.

**Part C:** Write the diagonalization M = PDP⁻¹ where:
- P is the matrix of eigenvectors as columns
- D is the diagonal matrix of eigenvalues

**Part D:** Verify M = PDP⁻¹ by computing PDP⁻¹ by hand.
First find P⁻¹ (2×2 inverse formula), then multiply through.

---

### Problem 1.4 — Closed form from diagonalization

Using M = PDP⁻¹ from Problem 1.3:

**Part A:** Explain in one sentence why Mⁿ = PDⁿP⁻¹.
(Hint: write out M·M = PDP⁻¹·PDP⁻¹ and watch what cancels.)

**Part B:** Write Dⁿ explicitly.
(Hint: diagonal matrices raise easily — each entry just gets the power.)

**Part C:** The lecture found that:
$$e_n = \frac{1}{2} \cdot 9^n + \frac{1}{2} \cdot (-1)^n$$

Verify this formula for n = 1, 2, 3 using both:
- The formula directly
- The recurrence eₙ₊₁ = 4eₙ + 5oₙ from your earlier computation

Do they match?

**Part D:** Using the same approach, derive the formula for oₙ.
You should get oₙ = ½·9ⁿ - ½·(-1)ⁿ.
Verify for n = 1: o₁ should equal 5.

---

### Problem 1.5 — New recurrence, same method

Let aₙ = number of n-digit binary strings (digits 0 and 1) with no two consecutive 1s.

**Part A:** Find a₁ and a₂ by direct counting.

**Part B:** Define:
- zₙ = number of valid n-digit strings ending in 0
- oₙ = number of valid n-digit strings ending in 1

Find z₁, o₁. Write recurrence relations for zₙ₊₁ and oₙ₊₁.

**Part C:** Write the matrix M for this system.
Find its eigenvalues (characteristic polynomial).

**Part D:** You should get eigenvalues (1+√5)/2 and (1-√5)/2.
Do you recognize these numbers? What famous sequence do the aₙ values follow?

**Part E (written):** Without computing the full closed form — explain in 2 sentences why the golden ratio appears in binary strings with no consecutive 1s.

---

## TOPIC 2 — Combinatorial Grid Paths

### Problem 2.1 — Warm up: paths as strings

Count paths from top to bottom of a 3×3 grid (3 columns, 3 rows of edges) where at each step you go either Left (L) or Right (R) and always move downward.

**Part A:** How many steps total does each path take?
How many must be L? How many must be R?

**Part B:** Write the answer as a binomial coefficient C(n,k).
State what n and k represent.

**Part C:** Compute the numerical answer.

**Part D:** List all paths explicitly as strings of L's and R's.
Verify your count matches Part C.

---

### Problem 2.2 — Larger grid

Count paths from top to bottom of a 5×5 grid (5 columns, 5 rows of edges) where each step goes Left or Right and always downward.

**Part A:** Write the answer as C(n,k). Compute it.

**Part B:** Now add a constraint: the path must pass through the exact middle point of the grid (after exactly 2 steps, the path must be at the center column).

How many paths satisfy this constraint?
Hint: Split into two parts — top half and bottom half. Multiply.

**Part C:** How many paths do NOT pass through the center?
Use subtraction: Total − (paths through center).

---

### Problem 2.3 — The subtraction method

A 4×4 grid has a missing edge — the rightmost edge in the second row from the top is removed.

**Part A:** How many total paths are there (ignoring the missing edge)?

**Part B:** How many paths are forced to use the missing edge?
Method: count paths from top to the start of the missing edge × paths from end of missing edge to bottom.

**Part C:** How many valid paths avoid the missing edge?
Answer = Total − Bad paths.

---

### Problem 2.4 — Two missing edges

A 4×4 grid has TWO missing edges:
- The leftmost edge in row 2
- The rightmost edge in row 3

**Part A:** Count paths using Missing Edge 1 (call this A).
Count paths using Missing Edge 2 (call this B).
Count paths using BOTH missing edges (call this A∩B).

**Part B:** Use inclusion-exclusion:
Valid paths = Total − |A| − |B| + |A∩B|

Compute the answer.

**Part C (written):** Why do we add |A∩B| back in? What goes wrong if we just compute Total − |A| − |B|?

---

### Problem 2.5 — Connect recurrences to grid paths

Let P(n,k) = number of paths from the top to the k-th column after n steps downward in an infinite grid.

**Part A:** Find P(0,0). Find P(1,-1) and P(1,1).

**Part B:** Write a recurrence for P(n,k) in terms of P(n-1, k-1) and P(n-1, k+1).
Explain why this recurrence is true using the path structure.

**Part C:** Compute P(n,k) for n=0,1,2,3 and all valid k values.
Write the results in a triangle. What pattern do you recognize?

**Part D (written):** Explain in 2 sentences the connection between:
- Grid path counting
- Binomial coefficients C(n,k)
- Pascal's triangle

This is the same structure — just described three different ways.

---

## BOSS PROBLEM — Combine both topics

This problem uses recurrences AND grid paths together.

A frog starts at column 0. Each second it jumps either Left (to column -1) or Right (to column +1). The frog cannot visit column 3 or column -3 (it falls off).

Let Rₙ = number of ways the frog can be at column 0 after n jumps without ever falling off.
Let Sₙ = number of ways the frog can be at column ±1 after n jumps without ever falling off.
Let Tₙ = number of ways the frog can be at column ±2 after n jumps without ever falling off.

**Part A:** Find R₀, S₀, T₀ (base cases at n=0).

**Part B:** Write recurrence relations for Rₙ₊₁, Sₙ₊₁, Tₙ₊₁.
Hint: draw the possible positions and which jumps connect them.

**Part C:** Write this as a matrix equation. What is M?

**Part D:** Compute R₁, S₁, T₁ and R₂, S₂, T₂ using the recurrence.

**Part E:** The total number of unrestricted n-jump sequences is 2ⁿ.
The number of sequences where the frog falls off is 2ⁿ - (Rₙ + 2Sₙ + 2Tₙ).
Compute this for n = 1, 2, 3, 4.
What fraction of all paths fall off by step 4?

**Part F (written):** How does this boss problem connect the two main topics of today's lecture — recurrences and grid paths? Write 3 sentences.

---

## Mastery Checklist

You have internalized Lecture 2 when you can:

- [ ] Set up simultaneous recurrences from a verbal description
- [ ] Find base cases by direct counting
- [ ] Convert a system of recurrences into a matrix equation
- [ ] Compute Mⁿ using M = PDP⁻¹ → Mⁿ = PDⁿP⁻¹
- [ ] Find eigenvalues by solving det(M - λI) = 0
- [ ] Find eigenvectors for each eigenvalue
- [ ] Verify a closed form formula against small cases
- [ ] Represent a grid path as a string of L's and R's
- [ ] Express path counts as binomial coefficients C(n,k)
- [ ] Apply subtraction method: valid = total − bad
- [ ] Apply product rule: bad paths through a point = (paths to point) × (paths from point)
- [ ] Use inclusion-exclusion when there are two bad edges
- [ ] Connect Pascal's triangle to grid path counting

---

*CMU 21-228 Discrete Mathematics*
*Lecture 2: Linear Recurrences, Matrix Powers, Grid Paths*

generated by claude to practice the lecture 2 material
