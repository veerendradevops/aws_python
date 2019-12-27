#!/usr/bin/python
import boto3
#session=boto3.session.Session(profile_name="vinod-tester")
ec2_console_resource=boto3.resource(service_name="ec2",region_name="us-east-1")
#print dir(ec2_console_resouce)
#my_instance=ec2_console_resource.Instance(id="i-05fbe76f3e0d7c2e4")
instance_id=raw_input("Enter your instance id to the status: ")
my_instance=ec2_console_resource.Instance(id=instance_id)
print my_instance.state
