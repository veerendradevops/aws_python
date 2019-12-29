import boto3
iam_cli=boto3.client(service_name='iam')
print(dir(iam_cli))