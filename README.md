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
-   [Lambda + Python 3.11 + Django 4.1](stacks/cdk_lambda_python_3_11_django/)
-   [ECS Fargate + Python 3.11 + Flet](stacks/cdk_ecs_python_3_11_flet/)
-   [ECS Fargate + Python 3.11 + Django](stacks/cdk_ecs_python_3_11_django/)

## Cost

These are by no means a "production-level" deployment.  I don't expect deployed resources to be kept around for longer than a day.

I don't recommend deploying these all together, but doing so will allow you to compare all the different deployment models.

The largest cost with a deployment will be the ALB (part of ECS deployment) and the ECS cluster itself.  Deploying to Lambda you won't see any cost unless it's in use.

Keep this in mind based on your budget, and make sure to destroy resources when they aren't in use.  

## Deploy

    # Deploy all at once
    cdk deploy --require-approval never --all --concurrency 5 --profile <your AWS profile>

    # Individual app deployment
    cdk deploy --require-approval never CdkLambdaPython39Flask --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython39FastAPI --profile <your AWS profile>
    cdk deploy --require-approval never CdkEcsFargatePython310Flask --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython311Flask --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython311FastAPI --profile <your AWS profile>
    cdk deploy --require-approval never CdkLambdaPython311Django --profile <your AWS profile>
    cdk deploy --require-approval never CdkEcsFargatePython311Flet --profile <your AWS profile>
    cdk deploy --require-approval never CdkEcsFargatePython311Django --profile <your AWS profile>

## Destroy

```zsh
yes | cdk destroy --all
```

Note: Instructions and configurations were built on MacOS 12.3.x with an M1 processor.  Docker commands and containers were built for platform: `linux/amd64`.
