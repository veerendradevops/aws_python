import boto3
#session=boto3.session.Session(profile_name="vinod-tester")
ec2_con_res=boto3.resource(service_name="iam")
print dir(ec2_con_res)   #to get the all operations in IAM
