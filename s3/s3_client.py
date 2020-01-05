import boto3
client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
result = paginator.paginate(Bucket='mu-bucket', Delimiter='/')
print(dir(client))
