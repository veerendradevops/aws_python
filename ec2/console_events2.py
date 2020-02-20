from __future__ import print_function
import json
import re
import logging
import time
import datetime
import boto3
import os
from datetime import date, datetime, timedelta, timezone
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from botocore.exceptions import ClientError

#Define Boto3 Clients
ctrail = boto3.client('cloudtrail')
iam = boto3.client('iam')
s3client = boto3.client('s3')
sesclient = boto3.client('ses')
stsclient = boto3.client('sts')
ssm_client = boto3.client('ssm')


# Tag Related Variables
strCSV = "Service, CreationTime, CreatedBy, Action"
f= open(file_lb,"w+")
f.write(strCSV)
f.write('\n')
f.close()

def lambda_handler(event, context):
    rolearnlist = []
    region_name = 'eu-west-1'
    rolearnlist_from_ssm = ssm_client.get_parameter(Name='scmtpoc_dev_tag_role')
    rolearnlist_from_ssm_list = rolearnlist_from_ssm['Parameter']['Value'].split(",")
    rolearnlist = rolearnlist_from_ssm_list

    for role in rolearnlist:
        assumed_role_object=stsclient.assume_role(RoleArn=role,RoleSessionName="AssumeRoleSession1")
        credentials = assumed_role_object['Credentials']

        iam = boto3.client('iam',
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],region_name=region_name)

        ctrail = boto3.client('cloudtrail',
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],region_name=region_name)
        
        # Time Settings for Cloud Trail
        endtime = datetime.now()
        interval = timedelta(hours=24)
        starttime = endtime - interval
        ETime = str(endtime.strftime("%m/%d/%Y-%H:%M:%S"))
        STime = str(starttime.strftime("%m/%d/%Y-%H:%M:%S"))

        # Check Tags for Created Resources
        f= open(file_lb,"w+")
        f.write(strCSV)
        f.write('\n')
        f.close()

        for i in response:
            with open(file_lb,"a+") as f1:
                for j in i['Events']:
                time.sleep(1)
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