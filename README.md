# cdk-python-web-apps

Python based Web apps, built with custom Docker containers, deployed to AWS with CDK.

## What is this for?

This repository details ways to deploy Python Web frameworks (e.g. Flask) as standalone functions with AWS CDK.  Connections to the applications are proxied through API Gateway.

## Getting started

For up to date info see the [AWS CDK getting started guide](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html).

1.  `npm install -g aws-cdk`
2.  Activate a python virtual environment and install the CDK dependencies. (Using [pyenv](https://github.com/pyenv/pyenv)) 

```zsh
pyenv virtualenv 3.9.11 awscdk
pyenv local awscdk
pip install --upgrade pip
pip install -r requirements.txt
```

3.  `cdk bootstrap aws://ACCOUNT-NUMBER/REGION` (e.g. cdk bootstrap aws://1234567890/us-east-1)
4.  Make sure Docker is [installed and running](https://www.docker.com/products/docker-desktop/).

## Manifest

-   [Lambda + Python 3.9 + Flask 2.x](stacks/cdk_lambda_python_3_9_flask/)
-   [Lambda + Python 3.9 + FastAPI](stacks/cdk_lambda_python_3_9_fastapi/)
-   [ECS Fargate + Python 3.10 + Flask 2.x](stacks/cdk_ecs_python_3_10_flask/)
-   [Lambda + Python 3.11 + Flask 2.x](stacks/cdk_lambda_python_3_11_flask/)
-   [Lambda + Python 3.11 + FastAPI](stacks/cdk_lambda_python_3_11_fastapi/)

## Deploy

    # Deploy all at once
    cdk deploy --require-approval never --all --concurrency 5 --profile <your AWS profile>

    # Individual app deployment
    cdk deploy --require-approval never CdkLambdaPython39Flask --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython39FastAPI --profile <your AWS profile>
    cdk deploy --require-approval never CdkEcsFargatePython310Flask --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython311Flask --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython311FastAPI --profile <your AWS profile>

## Destroy

```zsh
yes | cdk destroy --all
```

Note: Instructions and configurations were built on MacOS 12.3.x with an M1 processor.  Docker commands and containers were built for platform: `linux/amd64`.
