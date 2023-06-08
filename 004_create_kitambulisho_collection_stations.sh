#!/usr/bin/env bash
#curl -X POST http://0.0.0.0:5001/api/v1/cities/0585c235-9935-4040-b0b2-2b3b9127f620/places -H "Content-Type: application/json" -d '{"name": "Kapsoya", "staff_user_id": "1b61600c-5d08-4f22-b19c-7f8b18c89a2b"}' -vvv
curl -X POST http://0.0.0.0:5001/api/v1/cities/"$1"/places -H "Content-Type: application/json" -d '{"name": "Kapsoya", "staff_user_id": "62de0569-ceb5-476a-b797-5757a0c526aa"}' -vvv
#curl -X POST http://0.0.0.0:5001/api/v1/cities/0585c235-9935-4040-b0b2-2b3b9127f620/places -H "Content-Type: application/json" -d '{"name": "Kenyaree", "staff_user_id": "cd3389ec-9915-4d27-8d7b-9a7b04f42a18"}' -vvv
curl -X POST http://0.0.0.0:5001/api/v1/cities/"$1"/places -H "Content-Type: application/json" -d '{"name": "Kenyaree", "staff_user_id": "86e7edd9-9bc9-447b-a4f6-af17ded93978"}' -vvv


