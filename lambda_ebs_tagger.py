import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    #def tagCopierNewVersion(test):
        #Application
        application = "test"
        #API call to open connection to the EC2 resource
        instances = boto3.resource('ec2').instances.all()
        tags_to_be_copied = []
        
        #processing
        for ec2 in instances:
            temp = ec2.tags
            for tag in temp:
                if tag["Value"] == application:
                    tag_value = tag["Value"]
                    print(tag_value)
                    tags_to_be_copied = ["GSID"]
                    #copy the tags of instances
                    if len(tags_to_be_copied) != 0:
                        for instance in instances:
                            tags_to_copy = [tag for tag in instance.tags
                                            if tag["Key"] in tags_to_be_copied] if instance.tags else []
                            if not tags_to_copy:
                                continue
                            #tag the EBS volumes
                            print(f"{instance.instance_id}:{instance.tags}")
                            for vol in instance.volumes.all():
                                print(f"{vol.attachments[0]['Device']}: {tags_to_copy}")
                                #copying tags
                                vol.create_tags(Tags=tags_to_copy)
                    else:
                        print("No tags available to copy")
