import json

import logging

import boto3

 

#profile = 'mycloud'

region = 'us-east-1'

#boto3.setup_default_session(profile_name=profile, region_name=region)

file_1 = 'test.json'

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

for uname in userlist:

    user_tags = iam.list_user_tags(UserName=uname)['Tags']

    for i in user_tags:

            if 'Manager' in i['Key']:

                tag_user.append(uname)

print("Tagged Users:", tag_user)

#non_tag_user = [item for item in userlist if item not in tag_user]
non_tag_user = [user_list] - [tag_user]

print("Un-Tagged Users:", non_tag_user)

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

            create_tag = iam.tag_user(UserName=name, Tags=[{'Key':keyname,'Value':tag_value},])

            print(create_tag)

 