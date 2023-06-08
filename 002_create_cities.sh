#!/usr/bin/env bash
curl -X POST http://0.0.0.0:5001/api/v1/states/"$1"/cities -H "Content-Type: application/json" -d '{"name": "Eldoret"}' -vvv
curl -X POST http://0.0.0.0:5001/api/v1/states/"$1"/cities -H "Content-Type: application/json" -d '{"name": "Huruma"}' -vvv
curl -X POST http://0.0.0.0:5001/api/v1/states/"$1"/cities -H "Content-Type: application/json" -d '{"name": "Langas"}' -vvv
