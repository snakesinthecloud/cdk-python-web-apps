# cdk_ecs_flask

Builds a Python 3.10, Flask 2.x docker container to deploy to AWS ECS.

## Build

```
./build.sh
```

## Test

Request:

```zsh
curl "http://localhost:80/health"
```

You can also enter the container and start the app.

```zsh
docker exec -it cdk_python_ecs_flask sh
python app.py
```

To view the app, you can browse to `http://127.0.0.1:80/` on your host computer.