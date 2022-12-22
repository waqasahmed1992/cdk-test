from aws_cdk import Stack
from aws_cdk import aws_ec2 as _ec2

from constructs import Construct

class VpcClass(Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        my_custom_vpc = _ec2.Vpc(self, "mycustomvpc1",
                                 max_azs=self.node.try_get_context('az'),
                                 cidr=self.node.try_get_context('cidr'),
                                 subnet_configuration=[
                                     _ec2.SubnetConfiguration(
                                     name= "Public Subent",
                                     cidr_mask=self.node.try_get_context('mask'),
                                     subnet_type=_ec2.SubnetType.PUBLIC,
                                     map_public_ip_on_launch=False,
                                     )
                                #    _ec2.SubnetConfiguration(
                                #      name= "Private Subent",
                                #      cidr_mask=self.node.try_get_context('mask'),
                                #      subnet_type=_ec2.SubnetType.PRIVATE_WITH_EGRESS,
                                #      map_public_ip_on_launch=False,
                                #      )
                                 ]
                                 )