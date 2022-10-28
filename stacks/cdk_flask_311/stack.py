import os
from dataclasses import asdict, dataclass

from aws_cdk import Duration, Stack, Tags
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as lambda_
from constructs import Construct


@dataclass
class InfrastructureTags:
    Environment: str
    Product: str


class FlaskStack311(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        handler = lambda_.Function(
            self,
            "CdkPythonFlask-Handler",
            description="CDK Flask",
            runtime=lambda_.Runtime.FROM_IMAGE,  # type: ignore
            handler=lambda_.Handler.FROM_IMAGE,  # type: ignore
            function_name="cdk-flask-311",
            code=lambda_.Code.from_asset_image(
                directory=os.path.join(os.path.dirname(__file__), "."),
                file="Dockerfile",
                build_args={"--platform": "linux/amd64"},
            ),
            memory_size=128,
            timeout=Duration.seconds(29),
        )

        apigw.LambdaRestApi(
            self,
            "CdkPythonFlask311-API",
            rest_api_name="cdk-flask-311",
            description="This service proxies to a Flask-based Lambda.",
            handler=handler.current_version,
        )

        # Tag all resources the same
        tags = InfrastructureTags(Environment="dev", Product="flask")
        for k, v in asdict(tags).items():
            Tags.of(self).add(k, v)
