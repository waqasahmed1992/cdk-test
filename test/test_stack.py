from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    # aws_sqs as sqs,
)
from constructs import Construct

class TestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        mybucket = s3.Bucket(self, "mybucket1",
                             versioned=False)
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "TestQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
