import boto3
import credentials

id, psswd = credentials.id_and_psswd('user')

client = boto3.client('iam', aws_access_key_id=id, aws_secret_access_key=psswd)
response = client.create_user(Path='/Analyst/', UserName='new_user1')

print response
