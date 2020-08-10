import json
import boto3
from botocore.exceptions import ClientError
# from configuration import s3_bucketName

def lambda_handler(event, context):
    s3_bucketName = {"testvktest": {'b_name': 'testvktest', 'expiration_days': 21, 'prefix': 'logs', 'ID': 'Id'},
    "vklogvk": {'b_name': 'vklogvk', 'expiration_days': 21, 'prefix': 'logs', 'ID': 'logid'}}
    storage_class = 'GLACIER'
    s3_client = boto3.client('s3')
    for bucket in s3_bucketName.values():
        target_bucket = bucket.get("b_name")
        try:
            policy = s3_client.get_bucket_lifecycle(Bucket=target_bucket)
        except ClientError as ce:
            policy_status = s3_client.put_bucket_lifecycle_configuration(
            Bucket=bucket.get("b_name"),
            LifecycleConfiguration={
                    'Rules': [
                        {
                            'Expiration': {
                                'Days': bucket.get("expiration_days"),
                            },
                            'ID': bucket.get("ID"),
                            'Prefix': bucket.get("prefix"),
                            'Status': 'Enabled',
                            'Transitions': [
                                {
                                    'Days': 12,
                                    'StorageClass': storage_class
                                },

                            ],
                            'NoncurrentVersionTransitions': [
                                {
                                    'NoncurrentDays': 22,
                                    'StorageClass': storage_class
                                },

                            ],
                            'NoncurrentVersionExpiration': {
                                'NoncurrentDays': 24
                            }
                        },
                    ]
                }
            )
        # print("Lifecycle policy is applied for the bucket{}".format(target_bucket))
