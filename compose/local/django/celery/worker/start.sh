#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A bitcoin_rate_monitor.taskapp worker -l INFO
