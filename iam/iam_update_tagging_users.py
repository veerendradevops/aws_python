import json
import logging
import boto3
# Define Input Parameters and Clients
region = 'us-east-1'
tag_user = []
non_tag_user = []
userlist = []

#Define Boto3 Clients
iam = boto3.client('iam', region_name=region)

#List Users
paginator = iam.get_paginator('list_users')
user_list = paginator.paginate()
for ulist in user_list:
    for user in ulist['Users']:
        x = user['UserName']
        userlist.append(x)
#print(userlist)        
# Fet User Tags
for uname in userlist:
    user_tags = iam.list_user_tags(UserName=uname)['Tags']
    for i in user_tags:
            if 'Manager' in i['Key']:
                tag_user.append(uname)
#print("Tagged Users:", tag_user)
non_tag_user = [item for item in userlist if item not in tag_user]
#print("Un-Tagged Users:", non_tag_user)

# Update Tags dor Untagged Users
with open('test.json', 'r') as content:
  data = content.readlines()
  for i in data:
    obj = json.loads(i)
    #print(obj)
    for u in non_tag_user:
        if obj['User'] == u:
            name = obj['User']
            #print(name)
            keyname = 'Manager'
            #print(keyname)
            tag_value = obj[keyname]
            #print(tag_value)
            user_template = [
                {'Key': 'Name', 'Value': name.lower()},
                {'Key': 'Manager', 'Value': tag_value.lower()}
            ]
            create_tag = iam.tag_user(UserName=name, Tags=user_template)
            print(create_tag)