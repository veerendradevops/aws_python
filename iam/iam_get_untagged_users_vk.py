import json
import logging
import boto3

profile = 'default'
region = 'us-east-1'
boto3.setup_default_session(profile_name=profile, region_name=region)

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

print(userlist)        

for uname in userlist:

    user_tags = iam.list_user_tags(UserName=uname)['Tags']

    for i in user_tags:

            if 'Manager' in i['Key']:

                tag_user.append(uname)

print("Tagged User List:", tag_user)

non_tag_user = [item for item in userlist if item not in tag_user]

print("Untagged User list :", non_tag_user)