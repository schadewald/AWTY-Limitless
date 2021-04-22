docker build -t auth-guard .
docker run --env-file .env --network host -it auth-guard
