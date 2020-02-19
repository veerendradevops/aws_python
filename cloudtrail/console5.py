import boto3
import botocore.session
import json
import pprint
import re
import datetime
from datetime import date, datetime, timedelta, timezone

 
# Time Settings for Cloud Trail
starttime = datetime.now()
interval = timedelta(hours=24)
endtime = starttime - interval
ETime = str(endtime.strftime("%m/%d/%Y-%H:%M:%S"))
STime = str(starttime.strftime("%m/%d/%Y-%H:%M:%S"))
profile = 'vk'
region = 'eu-central-1'
boto3.setup_default_session(profile_name=profile, region_name=region)
ctrail = boto3.client("cloudtrail")

paginator = ctrail.get_paginator('lookup_events')

#response = ctrail.lookup_events(StartTime=ETime , EndTime=STime)

response = paginator.paginate(StartTime=ETime,EndTime=STime)

for i in response:
    for j in i['Events']:
        e_name = j['EventName']
        if (re.search('Create.+', e_name)):
            #print(e_name)
            u_name = j['Username']
            #print(u_name)
            if ((re.search('.tui.+', u_name)) or (re.search('.sonata.+', u_name))):
                 temp = j['Resources']
                 if len(temp) != 0 :
                    ServiceName   = j['Resources'][0]['ResourceName']
                    Creation_Time = j['EventTime']
                    Created_By    = j['Username']
                    Action        = j['EventName']
                    print(ServiceName,Creation_Time,Created_By,Action)
