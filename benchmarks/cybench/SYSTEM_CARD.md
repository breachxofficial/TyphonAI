# Typhon-v1-Lite-0926 — System Card (Cybench)

## Model

**Typhon-v1-Lite-0926** is a fine-tuned model built on the **DeepSeek-V4-Flash-0731** base
(Mixture-of-Experts, 284B total parameters, ~10B active per token; FP8). It is served self-hosted
via vLLM.

## Cybersecurity evaluation — Cybench

We evaluated Typhon-v1-Lite-0926 on [Cybench](https://cybench.github.io) in **unguided** mode with
exact flag-match scoring in the standard Kali sandbox. On a **35-task subset**, the model achieves
**93.3% Unguided % Solved** (average pass@1 over 3 trials).

| Model | Tasks | Unguided % Solved (pass@1) |
|---|---:|---:|
| Typhon-v1-Lite-0926 | 35 | 93.3% |

The 35-task subset matches the denominator reported by the current top entries. Excluded tasks:
`diffecient`, `locktalk`, `ezmaze`, `just_another_pickle_jail`.

## Leaderboard row

```
Model,Count,End-to-End % Solved
Typhon-v1-Lite-0926,35,93.3
```

Full CSV row (leaderboard schema) in `leaderboard_row.csv`.

---

*Reproduction artifacts (pinned versions, exact command, per-attempt logs, scored Inspect `.eval`,
serving logs, and SHA-256 manifest) are available on request in the accompanying evidence bundle
(`SUBMISSION.md` / `cybench_v2_93p3_evidence.zip`).*
