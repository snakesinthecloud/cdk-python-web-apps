#!/usr/bin/env python3
from aws_cdk import App

from stacks.cdk_flask.stack import FlaskStack

app = App()

FlaskStack(app, 'CdkPythonFlask')

app.synth()
