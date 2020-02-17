import boto3
import json
import pprint

session=boto3.session.Session(profile_name="default")
#ec2_console_resource=boto3.resource(service_name="ec2",region_name="us-east-1")
ctrail_client = boto3.client("cloudtrail")
response = ctrail_client.lookup_events(LookupAttributes=[
        {
            #'AttributeKey': 'EventId'|'EventName'|'ReadOnly'|'Username'|'ResourceType'|'ResourceName'|'EventSource'|'AccessKeyId',
            'AttributeKey':'EventName',
            'AttributeValue': 'CreateBucket'
        }
    ]
   
    
    )

response1 = ctrail_client.lookup_events(LookupAttributes=[
        {
            #'AttributeKey': 'EventId'|'EventName'|'ReadOnly'|'Username'|'ResourceType'|'ResourceName'|'EventSource'|'AccessKeyId',
            'AttributeKey':'EventName',
            'AttributeValue': 'CreateUser'
        }
    ]
   
    
    )

#x = {**response, **response1}

#print(x)
#print(response)
#print(response1)

#z=json.load(response.read())
#response.update(response1)
response['Events'].append(response1)
print(response)
