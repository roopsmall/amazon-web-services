import boto3, credentials

# get access key id and secret access key
id, psswd = credentials.id_and_psswd('user')

#start session
client = boto3.client('iam', aws_access_key_id=id, aws_secret_access_key=psswd)

# create new user, print result
print client.create_user(Path='/Analyst/', UserName='new_user1')
