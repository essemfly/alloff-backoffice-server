docker buildx build --platform=linux/amd64 -t backoffice-server .
docker tag backoffice-server:latest 193142563486.dkr.ecr.ap-northeast-2.amazonaws.com/backoffice-server:latest
docker push 193142563486.dkr.ecr.ap-northeast-2.amazonaws.com/backoffice-server:latest