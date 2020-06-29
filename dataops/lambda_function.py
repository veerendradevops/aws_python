import json
import boto3
import os

init_script = """#!/bin/bash
sudo yum update -y
wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
sudo rpm -ivh mysql80-community-release-el7-3.noarch.rpm
sudo yum install -y mysql-server
systemctl start mysqld
sudo systemctl start mysqld
export AWS_ACCESS_KEY_ID= <secretkey>
export AWS_SECRET_ACCESS_KEY= <secret-key>
export AWS_DEFAULT_REGION=us-east-1
aws s3 sync s3://vkdataopsbucket/ /home/ec2-user/
mysql -h database-1.afbjhq.us-east-1.rds.amazonaws.com -u admin -p password < /home/ec2-user/sql/test.sql
shutdown -h +5"""

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']
#NAME = os.environ['NAME']
ec2 = boto3.resource('ec2')


def lambda_handler(event, context):
    instance = ec2.create_instances(

        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        #SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        InstanceInitiatedShutdownBehavior='terminate',
        UserData=init_script
    )

    print("New instance created:", instance[0].id)

    
