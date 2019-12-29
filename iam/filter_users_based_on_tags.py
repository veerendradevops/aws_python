import boto3
iam = boto3.client('iam')
#print(dir(iam))-
#for user_detail in iam.get_account_authorization_details(Filter=['User'])['UserDetails']:


for user_detail in iam.get_account_authorization_details():
    print(dir(user_detail))
