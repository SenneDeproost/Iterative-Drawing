#!/usr/bin/env bash

# Create virtualenv if it doesn't exist.
if [ ! -d env ]; then
  virtualenv env
  source ./env/bin/activate
  pip install -r ./src/requirements.txt
 else
 source ./env/bin/activate
fi

# Run server
python src/manage.py runserver 0.0.0.0:8000

# Stop server
deactivate

