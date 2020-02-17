import json
import logging
import boto3


#Define Boto3 Clients
profile = 'mfa'

region = 'eu-central-1'

boto3.setup_default_session(profile_name=profile, region_name=region)
kms = boto3.client('kms', region_name=region)

response = kms.get_key_rotation_status(
    KeyId='22d10f9d-d700-40d3-8950-e807efc27af8'
)

print(response)