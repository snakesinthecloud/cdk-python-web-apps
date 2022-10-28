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


@dataclass
class EnvironmentVariables:
    STAGE: str


class CdkLambdaPython311FastAPI(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        name = "cdk-lambda-python-3-11-fastapi"
        description = "CDK Lambda Python 3.11 FastAPI"

        handler = lambda_.Function(
            self,
            f"{construct_id}-Handler",
            description=description,
            runtime=lambda_.Runtime.FROM_IMAGE,  # type: ignore
            handler=lambda_.Handler.FROM_IMAGE,  # type: ignore
            function_name=name,
            code=lambda_.Code.from_asset_image(
                directory=os.path.join(os.path.dirname(__file__), "."),
                file="Dockerfile",
                build_args={"--platform": "linux/amd64"},
            ),
            memory_size=128,
            timeout=Duration.seconds(29),
            environment=asdict(EnvironmentVariables("prod")),
        )

        apigw.LambdaRestApi(
            self,
            f"{construct_id}-API",
            rest_api_name=name,
            description=description,
            handler=handler.current_version,  # type: ignore
        )

        # Tag all resources the same
        tags = InfrastructureTags(Environment="prod", Product="FastAPI")
        for k, v in asdict(tags).items():
            Tags.of(self).add(k, v)
