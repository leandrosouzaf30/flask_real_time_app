aws ecr get-login-password --region eu-north-1 --profile real-time-app | docker login --username AWS --password-stdin 209479290955.dkr.ecr.eu-north-1.amazonaws.com
docker build -t real-time-app .
docker tag real-time-app:latest 209479290955.dkr.ecr.eu-north-1.amazonaws.com/real-time-app:latest
docker push 209479290955.dkr.ecr.eu-north-1.amazonaws.com/real-time-app:latest