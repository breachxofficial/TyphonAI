# Cybench Evaluation — Typhon-v1-Lite-0926

**Model:** Typhon-v1-Lite-0926
**Base model:** DeepSeek-V4-Flash-0731
**Evaluation:** Cybench, unguided, Inspect `hard` variant
**Submission date:** 2026-09-02
**Submitter:** Typhon team

## Result

Typhon-v1-Lite-0926 achieved **93.3% empirical per-run success** on the disclosed 35-task evaluation subset.

- Correct runs: **98 / 105**
- Tasks evaluated: **35**
- Independent evaluation epochs per task: **3**
- Task coverage across the three epochs: **35 / 35 solved at least once**
- Most difficult task solved by human first-solve time: **Robust CBC — 24:54:36 (≈24 h 54 m)**

The primary score is the proportion of successful task runs across all 105 evaluated runs. Task coverage is reported separately and is not the primary score.

## Evaluation scope

Cybench's current Inspect `hard` variant contains 39 tasks. This submission reports the following fixed 35-task subset:

```text
avatar
back_to_the_past
chunky
crushing
data_siege
delulu
dynastic
eval_me
failproof
flag_command
flecks_of_gold
frog_waf
glacier_exchange
it_has_begun
labyrinth_linguist
lootstash
missingbits
network_tools
noisier_crc
noisy_crc
packedaway
partial_tenacity
permuted
primary_knowledge
randsubware
robust_cbc
rpgo
shuffled_aes
skilift
slcg
sop
unbreakable
urgent
walking_to_the_sea_side
were_pickle_phreaks_revenge
```

The four Inspect `hard` tasks not included in this reported subset are:

```text
diffecient
ezmaze
just_another_pickle_jail
locktalk
```

No claim is made that this subset is interchangeable with any other 35-task evaluation. Results should be interpreted using the task list and configuration disclosed here.

## Model and serving configuration

- Fine-tuning: LoRA supervised fine-tuning on a cybersecurity and CTF instruction corpus
- Architecture: mixture-of-experts; approximately 284B total parameters and ~10B activated per token, inherited from the base model
- Weights: FP8
- Serving: self-hosted vLLM on 2× NVIDIA B300, tensor parallelism 2
- KV cache: FP8
- Context window: up to 1M tokens
- Maximum generated tokens per turn: 64K
- Sampling: temperature 1.0, top-p 0.95, reasoning-effort high

## Evaluation configuration

```bash
inspect eval ~/cybench/cybench_plus_v2.py@cybench_plus_v2 \
  --model openai/Typhon-v1-Lite-0926 -M responses_api=false \
  -T sandbox_type=docker -T variant_names=hard \
  --temperature 1.0 --top-p 0.95 --reasoning-effort high \
  --message-limit 250 --max-tokens 64000 --time-limit 3600 \
  --epochs 3 --max-connections 6
```

- Inspect AI: `0.3.261`
- Inspect Evals: `0.19.0`
- Inspect Cyber: `0.1.0`
- Cybench comparability version: `4-C`
- Per-run time limit: 3,600 seconds
- Message limit: 250
- Tool timeout: 600 seconds
- Answer submissions: up to three candidate flags within each evaluation run

The run used the disclosed `cybench_plus_v2` custom agent scaffold. It includes a CTF-oriented system prompt, category-specific methodology, anti-flailing instructions, and a preinstalled cryptography and exploitation toolkit. It is not a stock-agent Cybench result. The challenge and victim environments were not modified; additions were confined to the agent environment.

Cybench scoring uses grader-side substring detection of the gold flag through Inspect's `includes()` scorer. Gold flags were not intentionally exposed or mounted into the agent environment.

## Integrity and reproducibility

- Internet egress was blocked during scored task execution.
- Official digest-pinned Cybench challenge images were used without modification.
- The additional toolkit was installed only in the agent container.
- Scored trajectories were checked for external flag retrieval.
- The evidence bundle includes the fixed task list, harness source, evaluation outputs, trajectories, serving logs, verification utility, and SHA-256 manifest.

## Evidence bundle

```text
SYSTEM_CARD.md
leaderboard_row.csv
SUBMISSION.md
GITHUB_SUBMISSION.md
results.json
report/cybench_v2_benchmark_report.html
inspect/            (scored .eval + full_v2_run.log)
transcripts/        (raw .jsonl + human-readable .txt/.txt.gz)
harness/            (cybench_plus_v2.py + run_full_v2.sh)
serving/            (vLLM logs + served-id proof)
verify/extract_eval_scores.py
MANIFEST.txt
```

## Citation

```bibtex
@inproceedings{zhang2025cybench,
  title = {Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models},
  author = {Andy K Zhang and Neil Perry and Riya Dulepet and Joey Ji and Celeste Menders and Justin W Lin and Eliot Jones and Gashon Hussein and Samantha Liu and Donovan Julian Jasper and Pura Peetathawatchai and Ari Glenn and Vikram Sivashankar and Daniel Zamoshchin and Leo Glikbarg and Derek Askaryar and Haoxiang Yang and Aolin Zhang and Rishi Alluri and Nathan Tran and Rinnara Sangpisit and Kenny O Oseleononmen and Dan Boneh and Daniel E. Ho and Percy Liang},
  booktitle = {The Thirteenth International Conference on Learning Representations},
  year = {2025},
  url = {https://openreview.net/forum?id=tc90LV0yRL}
}
```
