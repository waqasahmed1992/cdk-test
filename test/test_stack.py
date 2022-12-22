from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    # aws_sqs as sqs,
)
from constructs import Construct

class ArtifactBucketClass(Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        if is_prod:
            mybucket = s3.Bucket(self, "mybucket1",
                                 versioned=self.node.try_get_context('prod')['versioned'],
                                 block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
        else:
            mybucket = s3.Bucket(self,"nybucket1",
                                 versioned=self.node.try_get_context('dev')['versioned'],
                                 public_read_access=True)
        
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "TestQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
