import boto3
client = boto3.client('iam')
responcse = client.update_role(
   RoleName='vk_aws_cloudformation_role',
   Description='Allow Vk',
   MaxSessionDuration=7200
)