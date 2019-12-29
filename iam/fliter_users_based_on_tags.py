import boto3
iam = boto3.client('iam')

for user_detail in iam.get_account_authorization_details(Filter=['User'])['UserDetailList']:
 tagname = []
 tagvalue = []
 # find each policy attached to the user
 for user in user_detail['Tags']:
  tagname.append(user['Key'])
  tagvalue.append(user['Value'])

 # print user details 
  print("User: {0}\nUserID: {1}\nKey: {2}\nValue: {3}\n".format(
  user_detail['UserName'],
  user_detail['UserId'],
  tagname,
  tagvalue
  )
  )