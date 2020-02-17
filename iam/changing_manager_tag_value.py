import json
import logging
import boto3
# Define Input Parameters and Clients

tag_user = []
non_tag_user = []
userlist = []

#Define Boto3 Clients
profile = 'default'

region = 'us-east-1'

boto3.setup_default_session(profile_name=profile, region_name=region)
iam = boto3.client('iam', region_name=region)

# Update Tags for Untagged Users
with open('test.json', 'r') as content:
  data = content.readlines()
  for i in data:
    obj = json.loads(i)
    #print(obj)
    for u in obj['User']:
    #    if obj['User'] == u:
            name = obj['User']
            #print(name)
            keyname = 'Manager'
            #print(keyname)
            tag_value = obj[keyname]
            #print(tag_value)
            user_template = [
               # {'Key': 'Name', 'Value': name.lower()},
                {'Key': 'Manager', 'Value': tag_value.lower()}
            ]
            create_tag = iam.tag_user(UserName=name, Tags=user_template)
            print(create_tag)