#!/usr/bin/env python3
from aws_cdk import App

from stacks.cdk_ecs_python_3_10_flask.stack import CdkEcsFargatePython310Flask
from stacks.cdk_ecs_python_3_11_flet.stack import CdkEcsFargatePython311Flet
from stacks.cdk_lambda_python_3_9_fastapi.stack import CdkLambdaPython39FastAPI
from stacks.cdk_lambda_python_3_9_flask.stack import CdkLambdaPython39Flask
from stacks.cdk_lambda_python_3_11_django.stack import CdkLambdaPython311Django
from stacks.cdk_lambda_python_3_11_fastapi.stack import CdkLambdaPython311FastAPI
from stacks.cdk_lambda_python_3_11_flask.stack import CdkLambdaPython311Flask

app = App()

# Deploy all: cdk deploy --require-approval never --all --profile <aws profile>
# Deploy single stack: cdk deploy --require-approval never <name> --profile <aws profile>

CdkLambdaPython39Flask(app, "CdkLambdaPython39Flask")
CdkLambdaPython39FastAPI(app, "CdkLambdaPython39FastAPI")
CdkLambdaPython311Flask(app, "CdkLambdaPython311Flask")
CdkLambdaPython311FastAPI(app, "CdkLambdaPython311FastAPI")
CdkLambdaPython311Django(app, "CdkLambdaPython311Django")

CdkEcsFargatePython310Flask(app, "CdkEcsFargatePython310Flask")
CdkEcsFargatePython311Flet(app, "CdkEcsFargatePython311Flet")

app.synth()
