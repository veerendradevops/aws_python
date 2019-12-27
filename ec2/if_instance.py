import boto3
ec2_resource=boto3.resource(service_name="ec2")
#print dir(ec2_resource)
instance=ec2_resource.Instance(id="i-0327af22956bbbe68")
instance_state = "running"
if instance.state == instance_state:
   print ("instance is already running")
else:
   print ("instance is about to start")
   instance.start()

