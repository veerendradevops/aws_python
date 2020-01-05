import json
import boto3
from io import BytesIO
import gzip
try:
    s3 = boto3.resource('s3')
    key='AWSLogs/GuardDuty/324466232308/us-east-1/2019/12/11/2b1db530-b049-3c38-be7e-18d7a74b2a90.jsonl.gz'
    obj = s3.Object('forguarddutyalerts111219',key)
    n = obj.get()['Body'].read()
    gzipfile = BytesIO(n)
    gzipfile = gzip.GzipFile(fileobj=gzipfile)
    content = gzipfile.read()
    print(content)
except Exception as e:
    print(e)
    raise e
