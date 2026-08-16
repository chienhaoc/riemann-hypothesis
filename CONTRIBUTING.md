# Contributing & Independent Audit Guidelines

We welcome independent mathematicians, computer scientists, and AI alignment researchers to audit, replicate, and extend this empirical case study.

---

## How to Audit & Replicate

1. **Audit the Empirical Transcripts**:
   - Inspect raw entries in `02-raw-transcripts/2026-08-14.md`.
   - Use the indexing formula $\text{entry} = 2 \times \text{round} + 93$ to map human-facing audit rounds to journal entries.

2. **Run Symbolic Verifications**:
   - Navigate to `03-verification/` and execute any of the Python/SymPy scripts:
     ```bash
     python 03-verification/verify_dispersion_identity.py
     python 03-verification/verify_killing_lorentz_metric.py
     python 03-verification/count_rhetorical_keywords.py
     ```

3. **Submit New Failure Modes or Replications**:
   - If you identify additional cognitive failure modes in the raw transcripts, or have verified specific entries using formal proof assistants (Lean 4, Isabelle/HOL), please open an Issue or submit a Pull Request.

---

## Licensing
- Code and verification scripts: **MIT License** (`LICENSE`)
- Transcripts, documentation, and papers: **CC BY 4.0** (`LICENSE-DOCS.md`)
