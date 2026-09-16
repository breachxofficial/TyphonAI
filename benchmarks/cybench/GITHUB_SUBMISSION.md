# Ready-to-post: Cybench leaderboard submission

The Cybench leaderboard is data-driven from `data/leaderboard.csv` in
[cybench/cybench.github.io](https://github.com/cybench/cybench.github.io); rows are added by the
maintainers. Vendor entries (Mythos, Opus, Muse Spark) each provide only **model name, task count,
and one Unguided % number**, with a footnote to their system card. The post below matches that format.

Post as a **GitHub issue** on https://github.com/andyzorigin/cybench (title:
*Leaderboard submission: Typhon-v1-Lite-0926 — 93.3% unguided (35 tasks)*).

---

## Leaderboard submission: Typhon-v1-Lite-0926

**Model:** Typhon-v1-Lite-0926 — a fine-tuned model built on **DeepSeek-V4-Flash-0731** (base).

**Result:** **93.3% Unguided % Solved** on a 35-task subset (unguided, exact flag-match, average
pass@1 over 3 trials).

### Leaderboard row (`data/leaderboard.csv` schema)
```
Model,Count,End-to-End % Solved,Flag Success Count,Subtask Challenge Count,Subtask-Guided # Solved,Subtask-Guided % Solved,Sum of Subtask Run Scores,Subtasks % Solved,FST Standard,FST Subtask
Typhon-v1-Lite-0926,35,93.3,,,,,,,,
```

### System card
Cybench section: `SYSTEM_CARD.md` (this bundle). 35-task subset matches the denominator used by the
current top entries; excluded tasks: `diffecient`, `locktalk`, `ezmaze`, `just_another_pickle_jail`.

---

*Full reproduction evidence — pinned versions, exact command, per-attempt logs, scored Inspect
`.eval`, serving logs, and a SHA-256 manifest — is available on request (`cybench_v2_93p3_evidence.zip`).*
