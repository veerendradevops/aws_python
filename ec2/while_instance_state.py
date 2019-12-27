#!/usr/bin/python
import boto3
#session=boto3.session.Session(profile_name="default")
ec2_con_res=boto3.resource(service_name="ec2",region_name="us-east-1")
while True:
    in_id=raw_input("Enter Your instance id: ")
    my_in=ec2_con_res.Instance(id=in_id)
    print "This script will perform the following actions"
    print "1. start"
    print "2. stop"
    print "3. reboot"
    print "4. terminate"
    print "5. Exit"
    option=input("Enter your action by selecting a number between 1-5")
    if option==1:
       print "Please wait we ar starting instance"
       my_in.start()
    elif option==2:
        print "stopping the instance"
	my_in.stop()
    elif option==3:
	print "rebooting instance"
	my_in.reboot()
    elif option==4:
	print "terminating instance"
	my_in.terminate()
    elif option==5:
	print "Thank u"
	break
    else:
	print "invalid. please check bw 1 to 5"
