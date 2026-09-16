#!/usr/bin/env bash
# Cybench hard (39-task) unguided run with the cybench_plus_v2 agent, internet-isolated
# (DOCKER-USER egress lock). Budgets: message-limit 250, time-limit 3600s, tool-timeout 600s.
set -euo pipefail
cd ~/cybench
source .venv/bin/activate
export OPENAI_API_KEY="$(cat ~/cybench/api_key)"
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export CYBENCH_ACKNOWLEDGE_RISKS=1
export INSPECT_EVALS_CACHE_DIR=$HOME/cybench/inspect-cache
mkdir -p ~/cybench/logs/full_v2
inspect eval ~/cybench/cybench_plus_v2.py@cybench_plus_v2 \
  --model openai/Typhon-v1-Lite-0926 \
  -M responses_api=false \
  -T sandbox_type=docker -T variant_names=hard \
  --temperature 1.0 --top-p 0.95 \
  --reasoning-effort high \
  --message-limit 250 --max-tokens 64000 \
  --time-limit 3600 \
  --epochs 3 \
  --max-connections 6 \
  --no-fail-on-error --retry-on-error 1 \
  --log-dir ~/cybench/logs/full_v2
echo "FULL_V2_DONE rc=$?"
