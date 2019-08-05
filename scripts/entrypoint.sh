#!/usr/bin/env bash

#make necessary changes in config.py
# gunicorn --pythonpath /src/ -b 0.0.0.0:$SERVICE_PORT rest_api:app
if [[ -z "${SERVICE_PORT}" ]]; then
  SERVICE_PORT="6162"
fi
# Need to export these variables since Click complains otherwise
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"
uvicorn --host 0.0.0.0 --port $SERVICE_PORT src.rest_api:app
