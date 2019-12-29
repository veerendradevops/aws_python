import boto3
iam = boto3.client('iam')
#print(dir(iam))-
for user_detail in iam.get_account_authorization_details(Filter=['User'])['UserDetails']:
policyname = []
policyarn = []

#find each policy attached to the user

print("***********")