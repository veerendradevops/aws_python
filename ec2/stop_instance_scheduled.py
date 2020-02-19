import boto3

session=boto3.session.Session(profile_name="default")
ec2=boto3.client("ec2")

response2 = ec2.describe_tags(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'Test',
            ]
        }
    ]
    )
#print(response2)

for i in response2['Tags']:
    in_id = (i['ResourceId'])
    print(in_id)
    ec2.stop_instances(InstanceIds=[in_id])
    


