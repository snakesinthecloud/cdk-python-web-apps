# ECS, ELB, Python 3.11, and a Django app

Builds a Python 3.11, Django app, deployed to AWS ECS.

## Build

    ./build.sh

You can also enter the container and start the app.

```zsh
docker exec -it cdk_ecs_python_3_11_django sh
python manage.py runserver 0.0.0.0:80
```

To view the app, you can browse to `http://127.0.0.1/polls` on your host computer.
