import boto3, credentials

id, psswd = credentials.id_and_pssw('username')

s3 = resource('s3', aws_access_key_id=id, aws_secret_access_key=psswd)

bucket = s3.create_bucket(Bucket='bucket_1')

print bucket
