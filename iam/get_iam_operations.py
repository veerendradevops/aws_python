import boto3
import pprint
iam_cli=boto3.client(service_name='iam')
#print(dir(iam_cli))
pprint.pprint(dir(iam_cli))