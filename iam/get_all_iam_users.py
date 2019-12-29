import boto3
iam = boto3.client('iam')
count = 1
for user in iam.list_users()['Users']:
    print("Users:= {0}\nUserID: {1}\n ARN: {2}".format(user['UserName'],user['UserId'],user['Arn']))
    print count
    count = count+1
    