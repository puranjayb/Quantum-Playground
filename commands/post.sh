#!/bin/bash

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"review": "Awesome Product"}' \
  http://localhost:8000/predict