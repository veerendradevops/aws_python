import boto3
import botocore.session
import json
import pprint
import re
import datetime
import time
from datetime import date, datetime, timedelta, timezone

 
# Time Settings for Cloud Trail
starttime = datetime.now()
interval = timedelta(hours=1)
endtime = starttime - interval
ETime = str(endtime.strftime("%m/%d/%Y-%H:%M:%S"))
STime = str(starttime.strftime("%m/%d/%Y-%H:%M:%S"))
profile = 'vk'
region = 'eu-central-1'
boto3.setup_default_session(profile_name=profile, region_name=region)
ctrail = boto3.client("cloudtrail")
sesclient = boto3.client('ses')
stsclient = boto3.client('sts')

paginator = ctrail.get_paginator('lookup_events')
print("Etime is + ", ETime)
print("Stime is +", STime)
print("starttime is +", starttime)
print("endtime is +", endtime)


#response = ctrail.lookup_events(StartTime=ETime , EndTime=STime)

response = paginator.paginate()
timeFile = time.strftime("%Y-%m-%d-%H%M%S")
filename = 'resourcelist-'+timeFile+'.csv'
#filename = 'resourcelist2.csv'
file_lb = filename

# Check Tags for Created Resources
strCSV = "Service, CreationTime, CreatedBy, Action"
f= open(file_lb,"w+")
f.write(strCSV)
f.write('\n')
f.close()



for i in response:
    with open(file_lb,"a+") as f1:
        for j in i['Events']:
            #time.sleep(1)
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
                        op = (ServiceName,Creation_Time,Created_By,Action)
                        str_op = str(op)
                        s1 = str(op).lstrip("(")
                        s1 = s1.rstrip(")")
                        f1.write(s1)
                        f1.write('\n')
