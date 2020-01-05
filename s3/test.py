from io import StringIO
import boto3
import pandas as pd

bucket = 'forguarddutyalerts111219'
prefix = '/AWSLogs/GuardDuty/324466232308/us-east-1/2019/12/11/'

client = boto3.client('s3')

for object in client.list_objects_v2(Bucket=bucket, Prefix=prefix)['Contents']:
    if object['Size'] <= 0:
        continue

    print(object['Key'])
    r = client.select_object_content(
            Bucket=bucket,
            Key=object['Key'],
            ExpressionType='SQL',
            Expression="select * from s3object",
            InputSerialization = {'CompressionType': 'GZIP', 'JSON': {'Type': 'DOCUMENT'}},
            OutputSerialization = {'CSV': {'QuoteFields': 'ASNEEDED', 'RecordDelimiter': '\n', 'FieldDelimiter': ',', 'QuoteCharacter': '"', 'QuoteEscapeCharacter': '"'}},
        )

    for event in r['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            payloads = (''.join(r for r in records))
            try:
                select_df = pd.read_csv(StringIO(payloads), error_bad_lines=False)
                for row in select_df.iterrows():
                    print(row)
            except Exception as e:
                print(e)
