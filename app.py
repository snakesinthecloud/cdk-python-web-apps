#!/usr/bin/env python3
from aws_cdk import App

from stacks.cdk_ecs_flask.stack import EcsFlaskStack
from stacks.cdk_fastapi.stack import FastAPIStack
from stacks.cdk_flask.stack import FlaskStack

app = App()

FlaskStack(app, 'CdkPythonFlask')
FastAPIStack(app, 'CdkPythonFastAPI')
EcsFlaskStack(app, 'CdkEcsPythonFlask')

app.synth()
