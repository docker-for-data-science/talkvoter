#!/bin/bash

export SITE_DIR=${SITE_DIR:-"/app/"}
export PYTHONPATH="${SITE_DIR}proj/:${PYTHONPATH}"
export PATH="/app/.local/bin/:${PATH}"
export SITE_DIR=${SITE_DIR}

cd ${SITE_DIR}proj/

exec "$@"
