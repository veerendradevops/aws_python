import boto3
res = boto3.resource('s3')
bucketName = res.Bucket('vkawsaccountlist')
for obj in bucketName.objects.filter(Prefix='version_1/'):
    print(obj.key)
    sorted = sorted(obj.key)
    print(sorted)
