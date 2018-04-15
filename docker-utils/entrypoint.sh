#!/bin/bash

export SITE_DIR=${SITE_DIR:-"/app/"}
export SITE_DIR=${SITE_DIR}

cd ${SITE_DIR}proj/

exec "$@"
