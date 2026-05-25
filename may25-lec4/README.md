# CMU 21-228 Discrete Mathematics — Lecture 4 Practice Problems
## Diophantine Approximation, Dirichlet's Theorem, Proof Techniques

> **The rule:** Solve everything by hand. Show every step.
> Target: 1 hour total.
> ~10 min Topic 1, ~20 min Topic 2, ~20 min Topic 3, ~10 min Topic 4

---

## TOPIC 1 — Basics of Rational Approximation

### Problem 1.1 — Understanding the "Easy Theorem"

The Easy Theorem says: for any real number α and any positive integer n,
there exist integers p and q with 1 ≤ q ≤ n such that |α - p/q| ≤ 1/qn.

**Part A:** Apply this to α = π ≈ 3.14159 with n = 7.

- The fractions with denominator at most 7 near π are: 3/1, 22/7, 19/6, 16/5...
- Find which fraction p/q with q ≤ 7 gets closest to π.
- Compute the actual distance |π - p/q|.
- Verify the distance is ≤ 1/(q × 7).

**Part B:** Now use n = 100.

Without computing exact fractions — the theorem guarantees some p/q with q ≤ 100 satisfying |π - p/q| ≤ 1/(100q).

If q = 100, the bound becomes 1/10000 = 0.0001. 
If q = 10, the bound becomes 1/1000 = 0.001.

Which gives a tighter guarantee? Why does a smaller q with the same n give a WORSE bound even though 1/(qn) gets larger?

**Part C (written):** The lecture called the approximation 3141592/1000000 "dumb." Explain in 2 sentences what makes it dumb compared to 22/7 or 355/113, using the idea of "digits of precision per digit of denominator."

---

### Problem 1.2 — Checking approximation quality

For each approximation of π below, compute:
- The error |π - p/q|
- The bound 1/q²
- Whether the approximation satisfies Dirichlet's theorem (error ≤ 1/q²)

Use π ≈ 3.14159265...

| Approximation | p/q | Error | 1/q² | Satisfies? |
|---|---|---|---|---|
| 3/1 | | | | |
| 22/7 | | | | |
| 333/106 | | | | |
| 355/113 | | | | |

**Part A:** Fill in the table by hand. Show your computations.

**Part B:** Which approximation is most "impressive" — meaning largest ratio of (digits of precision)/(digits of denominator)? Justify.

**Part C:** The lecture said the exponent q² is the BEST possible — you cannot replace it with q³. What does this mean? Give an intuitive explanation in 2 sentences.

---

## TOPIC 2 — Dirichlet's Approximation Theorem

### Problem 2.1 — The Strong Bound version

Dirichlet's Theorem (Yellow): For any real α, there are INFINITELY MANY fractions p/q such that |α - p/q| ≤ 1/q².

Apply this to α = √2 ≈ 1.41421356...

**Part A:** Check each of these fractions — does it satisfy |√2 - p/q| ≤ 1/q²?

- 1/1
- 3/2
- 7/5
- 17/12
- 41/29

Show your computation for each. These are called the "convergents" of √2.

**Part B:** Notice the pattern in the numerators and denominators: 1, 3, 7, 17, 41...

Each term is roughly twice the previous plus the one before that.
Verify: 3 = 2(1) + 1, then 7 = 2(3) + 1, then 17 = 2(7) + 3...

What recurrence does this follow? Write it as aₙ₊₁ = ?

**Part C (written):** Dirichlet says there are INFINITELY MANY such fractions. But in Part A you only found 5. How do you know more exist? Write 2 sentences.

---

### Problem 2.2 — The Finite Range version (Green Theorem)

Dirichlet's Theorem (Green): For any real α and any positive integer n, there exist integers p and q with 1 ≤ q ≤ n such that |α - p/q| ≤ 1/(qn).

**Part A:** Apply with α = √3 ≈ 1.73205... and n = 5.

The multiples of α are: 1α, 2α, 3α, 4α, 5α.
Compute each multiple and find its distance to the nearest integer.

| q | qα | Nearest integer | Distance to nearest integer |
|---|---|---|---|
| 1 | 1.732... | 2 | 0.268... |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

**Part B:** The theorem says at least one row has distance ≤ 1/n = 1/5 = 0.2.

Which row(s) satisfy this? For those rows, identify p (the nearest integer to qα) and verify |α - p/q| ≤ 1/(qn).

**Part C:** Apply the same process with α = √3 and n = 10.

Compute qα for q = 1 to 10. Find the q where qα is closest to an integer. Verify the bound.

---

### Problem 2.3 — Green implies Yellow

The lecture showed: Green Theorem → Yellow Theorem.

The key steps were:
1. Green gives one good approximation for each choice of n
2. There are infinitely many choices of n
3. Therefore infinitely many good approximations — UNLESS we keep getting repeats
4. For irrational α, repeats lead to contradiction

**Part A:** Explain Step 1 more precisely.

If Green gives us p/q with |α - p/q| ≤ 1/(qn) and q ≤ n, why does this also give |α - p/q| ≤ 1/q²?

Write the chain of inequalities. Identify the key step where you use q ≤ n.

**Part B:** Why does the rational case not need any theorem?

If α = 22/7 exactly, write down infinitely many fractions that approximate α with error exactly 0. Show they all satisfy |α - p/q| ≤ 1/q² trivially.

**Part C:** The irrational case needs contradiction. Fill in this argument:

"Assume for contradiction that only finitely many fractions p/q satisfy |α - p/q| ≤ 1/q². Since there are finitely many, one must be closest to α — call this minimum distance δ > 0.

Now choose n large enough so that 1/n < δ.

Invoke the Green Theorem with this n. It gives us a fraction p'/q' with |α - p'/q'| ≤ 1/(q'n) ≤ 1/n < δ.

But this means |α - p'/q'| < δ which is a contradiction because..."

Complete the last sentence. Why is this a contradiction?

---

## TOPIC 3 — Proof Techniques

### Problem 3.1 — Proof by contradiction practice

Use proof by contradiction to prove the following:

**Claim:** There is no largest even integer.

Write a complete proof:
- State what you assume for contradiction
- Derive something that contradicts an assumption
- Conclude the claim is true

This is simpler than the lecture's argument but uses the exact same logical structure.

---

### Problem 3.2 — Case analysis practice

The lecture split into rational and irrational cases. Practice this technique.

**Claim:** For any real number α, the sequence α, 2α, 3α, ... either contains an integer or gets arbitrarily close to integers.

**Part A:** Prove the case where α is rational. (If α = p/q, what happens at q·α?)

**Part B:** For the irrational case, you cannot prove it fully with what we know yet. Instead — give a concrete example. Take α = √2. Compute qα for q = 1, 2, ..., 10. Show that some value gets within 0.1 of an integer.

**Part C (written):** The lecture said "deal with rational and irrational differently." Why can't you use the same proof for both? What breaks if you apply the rational argument to an irrational number?

---

### Problem 3.3 — Implication logic

The lecture proved: Green Theorem → Yellow Theorem.

This means: IF Green is true THEN Yellow is true.

**Part A:** What does it mean to say "A implies B"? Complete this sentence:

"If A implies B, and A is true, then..."

"If A implies B, and B is false, then..."

**Part B:** The lecture used this chain:
- Prove: Green → Yellow
- Later will prove: Green is true
- Therefore: Yellow is true

Why is this a valid strategy? Why not just prove Yellow directly?

**Part C (written):** Can you think of a case where proving an EQUIVALENT or STRONGER statement first, then deriving what you want, is easier than attacking the original directly? Give one example from mathematics or from your own experience (doesn't need to be formal).

---

## TOPIC 4 — Proximity to Integers

### Problem 4.1 — Equivalent reformulation

The lecture showed this equivalence:

|α - p/q| ≤ 1/(qn) is equivalent to |qα - p| ≤ 1/n

**Part A:** Prove this equivalence algebraically.

Start with |α - p/q| ≤ 1/(qn). Multiply both sides by q. What do you get?

**Part B:** The second form |qα - p| ≤ 1/n says "qα is within 1/n of the integer p."

Compute: for α = π and n = 7, compute qα for q = 1, 2, 3, 4, 5, 6, 7.

| q | qπ | Nearest integer p | |qπ - p| | ≤ 1/7 = 0.143? |
|---|---|---|---|---|
| 1 | 3.14159... | 3 | 0.14159... | Yes |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |

**Part C:** Which row gives the best approximation (smallest |qα - p|)? Convert it back to a fraction p/q and verify it's a good approximation to π.

---

### Problem 4.2 — The Pigeonhole preview

The lecture ended by saying the proof of Green Theorem uses combinatorics — specifically a technique called the Pigeonhole Principle. Next lecture will prove this.

For now, think about it intuitively.

**Part A:** Divide the interval [0,1) into n equal subintervals:
[0, 1/n), [1/n, 2/n), [2/n, 3/n), ..., [(n-1)/n, 1)

If I have n+1 points in [0,1), what must be true about at least two of them?

**Part B:** Now consider the n+1 numbers: {α} = fractional part of α (i.e., α - floor(α)).

The fractional parts of: 0, α, 2α, 3α, ..., nα — that's n+1 numbers in [0,1).

If two of these fractional parts fall in the same subinterval of width 1/n, what can you say about their difference?

**Part C (written):** In 3 sentences, sketch how this might prove the Green Theorem — that some qα is within 1/n of an integer. You don't need to be rigorous. Just describe the idea.

This is the preview of next lecture — where combinatorics meets number theory.

---

## BOSS PROBLEM — Connecting Everything

This problem ties together rational approximation, proof by contradiction, and the equivalent formulation.

**The claim:** For any irrational number α, the quantity {qα} (the fractional part of qα) is DENSE in [0,1). This means: for any subinterval (a,b) ⊂ [0,1), no matter how small, there exists some positive integer q such that {qα} ∈ (a,b).

**Part A:** Verify this experimentally for α = √2 and the interval (0.4, 0.5).

Compute {q√2} for q = 1, 2, 3, ..., 20. Find which q lands in (0.4, 0.5).

**Part B:** Why does this fail for rational α = p/q?

If α = 1/3, compute {q × 1/3} for q = 1, 2, ..., 10. What do you notice? What interval does {q × 1/3} never hit?

**Part C:** The claim says this is true for ALL irrational α. Assume for contradiction it's false — there exists some interval (a,b) that no {qα} ever enters.

What does this mean about how close qα ever gets to the integers near a and b? Derive a contradiction using Dirichlet's theorem.

**Part D (written):** The lecture said this whole topic connects to an app Po-Shen Loh built for COVID contact tracing (novid) and that discrete mathematics solves real problems. In 2 sentences — how might the idea of "something appearing in every interval" (density) be useful in a practical context like signal processing or communication?

---

## Mastery Checklist

You have internalized Lecture 4 when you can:

- [ ] Explain what makes an approximation p/q "impressive" vs "dumb"
- [ ] Compute whether a given fraction satisfies the 1/q² bound
- [ ] State the Easy Theorem and prove it in 3 sentences
- [ ] State Dirichlet's Theorem (both Yellow and Green versions)
- [ ] Explain why 1/q² is the best possible exponent
- [ ] Convert |α - p/q| ≤ 1/(qn) to |qα - p| ≤ 1/n algebraically
- [ ] Compute the table of qα values and identify the best approximation
- [ ] Write a complete proof by contradiction with: assumption, derivation, contradiction, conclusion
- [ ] Explain why rational and irrational α need separate treatment
- [ ] State the logical structure: prove Green, then derive Yellow
- [ ] Explain in words why infinitely many good approximations must exist for irrational α
- [ ] Sketch the Pigeonhole idea that will prove Green Theorem next lecture

---

*CMU 21-228 Discrete Mathematics*
*Math practice only — no computation*
*Lecture 4: Diophantine Approximation, Dirichlet's Theorem, Proof Techniques*


claude generated to fully internalize the lecture 4 
