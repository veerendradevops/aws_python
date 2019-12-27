import boto3
ec2_resource=boto3.resource(service_name="ec2")
#print dir(ec2_resource)
instance=ec2_resource.Instance(id="i-0327af22956bbbe68")
instance.start()
