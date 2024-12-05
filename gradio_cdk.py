import os
from pathlib import Path
from constructs import Construct
from aws_cdk import (
    Stack,
    Duration,
    CfnOutput,
    Environment
)
from aws_cdk.aws_lambda import DockerImageFunction, DockerImageCode, Architecture, FunctionUrlAuthType

class GradioLambda(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function from Docker image
        lambda_fn = DockerImageFunction(
            self,
            "GradioApp",
            code=DockerImageCode.from_image_asset(str(Path.cwd()), file="Dockerfile"),
            architecture=Architecture.X86_64,
            memory_size=8192,
            timeout=Duration.minutes(2),
        )

        # Add Function URL with no authentication
        fn_url = lambda_fn.add_function_url(auth_type=FunctionUrlAuthType.NONE)

        # Output the Function URL
        CfnOutput(self, "FunctionUrl", value=fn_url.url)
