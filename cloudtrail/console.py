import boto3
import json
import pprint

profile = 'vk'
region = 'eu-central-1'
boto3.setup_default_session(profile_name=profile, region_name=region)
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
#print(response1['Events'][1]['Username'])
print(response)

#for Username in response['Events']

