#!/usr/bin/env python3
import os
from aws_cdk import App, Environment
from gradio_cdk import GradioLambda

app = App()

# Define environment by reading AWS credentials
env = Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION")
)

# Instantiate your stack
GradioLambda(app, "GradioLambdaStack", env=env)

app.synth()
