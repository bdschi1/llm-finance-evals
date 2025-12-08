# Data and factual errors in investment tasks

This document covers **data-related errors** where the model misreads, misuses, or fabricates numeric or factual information from the provided context.

---

## 1. Directional misread

- Getting the **direction** of a change wrong (up vs down, improvement vs deterioration).
- Example: Calling margin **expansion** when the provided text clearly shows margin compression.

**Impact:** Can completely invert the thesis or risk assessment.

---

## 2. Magnitude distortion

- Correct direction but obviously wrong **magnitude** (e.g., turning +3% into +30%).
- Example: Treating a modest guidance change as a “major reset” or vice versa.

**Impact:** Miscalibrates conviction and position sizing.

---

## 3. Time period confusion

- Mixing up time frames (QoQ vs YoY, current vs prior year) or applying old data to a new period.
- Example: Using last year’s growth rate when the prompt clearly provides the latest figure.

**Impact:** Leads to stale or misleading conclusions.

---

## 4. Ignoring provided numbers

- The model restates stories qualitatively but ignores clearly stated numeric context.
- Example: Talking about “strong growth” when the prompt shows low single-digit growth.

**Impact:** Reduces the value of the model as an assistant to analysts who care about numbers.

---

## 5. Mismatched company or sector facts

- Pulling in facts that belong to another company, ticker, or sub-sector.
- Example: Applying a biotech-style pipeline risk discussion to a hospital operator.

**Impact:** Signals shallow pattern-matching instead of real understanding.

---

## 6. Fabricated or altered input data

- Inventing numbers, events, or labels that are not in the prompt.
- Example: Adding a margin figure or growth rate with no basis in the provided text.

**Impact:** Can be worse than no answer, especially if used in models or dashboards.

---

## 7. Misuse of factor data

- Misreading factor tables or style exposures (e.g., calling a value stock “growth”).
- Example: The prompt shows clear momentum and leverage exposure, but the model calls the name “defensive”.

**Impact:** Directly affects risk aggregation and scenario analysis.
