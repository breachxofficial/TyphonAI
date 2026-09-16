# TyphonAI

Public benchmark results and reproduction evidence for **Typhon-v1-Lite-0926**, a fine-tuned model
built on the **DeepSeek-V4-Flash-0731** base (Mixture-of-Experts, 284B total / ~10B active per
token, FP8).

## Benchmarks

### Cybench

**93.3% Unguided % Solved** on a disclosed 35-task subset (98/105 runs, 3 epochs), unguided mode,
exact flag-match scoring.

Evidence and full reproduction materials: [`benchmarks/cybench/`](benchmarks/cybench/)

- [`SYSTEM_CARD.md`](benchmarks/cybench/SYSTEM_CARD.md) — short system-card summary
- [`SUBMISSION.md`](benchmarks/cybench/SUBMISSION.md) — detailed report (config, scope, integrity)
- [`results.json`](benchmarks/cybench/results.json) — machine-readable results
- [`leaderboard_row.csv`](benchmarks/cybench/leaderboard_row.csv) — row in the Cybench `data/leaderboard.csv` schema
- [`harness/`](benchmarks/cybench/harness/) — exact scaffold + launch script
- [`transcripts/`](benchmarks/cybench/transcripts/) — per-attempt request/response trajectories
- [`inspect/`](benchmarks/cybench/inspect/) — scored Inspect `.eval` + run log
- [`serving/`](benchmarks/cybench/serving/) — vLLM serving logs + served-id proof
- [`verify/extract_eval_scores.py`](benchmarks/cybench/verify/extract_eval_scores.py) — re-extract verdicts from the `.eval`
- [`MANIFEST.txt`](benchmarks/cybench/MANIFEST.txt) — SHA-256 of every file

The result uses a disclosed custom agent scaffold (`cybench_plus_v2`); see `SUBMISSION.md` for the
full methodology and integrity disclosure.
