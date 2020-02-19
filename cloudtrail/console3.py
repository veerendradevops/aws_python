import boto3
import botocore.session
import json
import pprint
import re
import datetime
from datetime import date, datetime, timedelta, timezone


# Time Settings for Cloud Trail
#endtime = datetime.now()
#interval = timedelta(hours=24)
#starttime = endtime - interval
profile = 'vk'
region = 'eu-central-1'
boto3.setup_default_session(profile_name=profile, region_name=region)
ctrail_client = boto3.client("cloudtrail")
response = ctrail_client.lookup_events()
for i in response['Events']:
    #print(i)
    ename = i['EventName']
    uname = i['Username']
    #print(ename)
    #print(uname)
    if re.search('Create.+', ename):
        print(ename)







#for j in i['CloudTrailEvent']
 #   print(j)




#for j in response['Events']:
 #   uname = j['Username']
    #print(uname)




#print(response)
#print("End Of response****************")

    #evt= json.loads(i['CloudTrailEvent'])
    #print(evt['userIdentity']['principalId'])
