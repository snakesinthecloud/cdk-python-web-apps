import os
from dataclasses import asdict, dataclass

from aws_cdk import Stack, Tags
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr_assets as ecr_assets
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns
from constructs import Construct


@dataclass
class InfrastructureTags:
    Environment: str
    Product: str


class CdkEcsFargatePython311Flet(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        name = "cdk-ecs-fargate-python-3-11-flet"

        # Build the docker image
        image = ecr_assets.DockerImageAsset(
            self,
            "EcrImageAsset",
            directory=os.path.join(os.path.dirname(__file__), "."),
            file="Dockerfile",
            build_args={"--platform": "linux/amd64"},
        )

        # Set up networking
        # 2 public AZ/subnets like the following: x.x.1.0/24, x.x.2.0/24
        subnet_config_public = ec2.SubnetConfiguration(
            name=f"{name}-public",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24,
            reserved=False,
        )

        vpc = ec2.Vpc(
            self,
            "Vpc",
            max_azs=2,
            cidr="10.1.0.0/16",
            nat_gateways=None,
            subnet_configuration=[subnet_config_public],
        )
        cluster = ecs.Cluster(self, "EcsCluster", vpc=vpc)
        ec2.SecurityGroup(self, "SG", vpc=vpc)

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ecs_patterns/ApplicationLoadBalancedFargateService.html
        load_balanced_fargate_service = (
            ecs_patterns.ApplicationLoadBalancedFargateService(
                self,
                f"{construct_id}-ELB",
                service_name=name,
                cluster=cluster,
                desired_count=2,
                cpu=256,
                task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                    image=ecs.ContainerImage.from_docker_image_asset(image),
                    container_port=80,
                ),
                public_load_balancer=True,
                assign_public_ip=True,
            )
        )

        # Scaling settings
        scalable_target = load_balanced_fargate_service.service.auto_scale_task_count(
            min_capacity=1, max_capacity=5
        )

        scalable_target.scale_on_cpu_utilization(
            "CpuScaling", target_utilization_percent=50
        )

        scalable_target.scale_on_memory_utilization(
            "MemoryScaling", target_utilization_percent=50
        )

        # Tag all resources the same
        tags = InfrastructureTags(Environment="dev", Product="flet")
        for k, v in asdict(tags).items():
            Tags.of(self).add(k, v)
