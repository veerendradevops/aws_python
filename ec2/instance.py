#/usr/bin/python
import boto3
#session=boto.session.Session(profile_name="default")
ec2_con_res=boto3.resource(service_name="ec2",region_name="us-east-1")
print dir(ec2_con_res)
