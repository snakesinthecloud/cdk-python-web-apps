# cdk-python-web-apps
Python based Web apps, built with custom Docker containers, deployed to AWS with CDK.

## What is this for?

This repository details ways to deploy Python Web frameworks (e.g. Flask) as standalone functions with AWS CDK.  Connections to the applications are proxied through API Gateway.

## Getting started

For up to date info see the [AWS CDK getting started guide](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html).

1. `npm install -g aws-cdk`
2. Activate a python virtual environment and install the CDK dependencies. (Using [pyenv](https://github.com/pyenv/pyenv)) 

```zsh
pyenv virtualenv 3.9.11 awscdk
pyenv local awscdk
pip install --upgrade pip
pip install -r requirements.txt
```

3. `cdk bootstrap aws://ACCOUNT-NUMBER/REGION` (e.g. cdk bootstrap aws://1234567890/us-east-1)
4. Make sure Docker is [installed and running](https://www.docker.com/products/docker-desktop/).

## Manifest

 - [Flask 2.x with Python 3.9 pushed to Lambda](stacks/cdk_flask/)
 - [FastAPI with Python 3.9 pushed to Lambda](stacks/cdk_fastapi/)
 - [Flask 2.x with Python 3.10 pushed to ECS Fargate](stacks/cdk_ecs_flask/)

## Deploy

    cdk deploy --require-approval never --all

## Destroy

```zsh
yes | cdk destroy --all
```

Note: Instructions and configurations were built on MacOS 12.3.x with an M1 processor.  Docker commands and containers were built for platform: `linux/amd64`.