#!/usr/bin/env bash

echo set webhook
python set_webhook.py

echo run "$*"
# Start command
exec "$@"
