#!/usr/bin/env python3
from aws_cdk import App

from stacks.cdk_ecs_flask.stack import EcsFlaskStack
from stacks.cdk_fastapi.stack import FastAPIStack
from stacks.cdk_fastapi_311.stack import FastAPIStack311
from stacks.cdk_flask.stack import FlaskStack
from stacks.cdk_flask_311.stack import FlaskStack311

app = App()

FlaskStack(app, "CdkPythonFlask")
FastAPIStack(app, "CdkPythonFastAPI")
EcsFlaskStack(app, "CdkEcsPythonFlask")
FlaskStack311(app, "CdkPython311Flask")
FastAPIStack311(app, "CdkPython311FastAPI")

app.synth()
