import boto3, credentials

id, psswd = credentials.id_and_psswd('username')

resource = boto3.resource('s3', aws_access_key_id=id, aws_secret_access_key=psswd)
s3 = resource.meta.client

# list buckets
print s3.list_buckets()

# list bucket policies if exist
try:
    print s3.get_bucket_policy(Bucket='bucket_1')
except:
    pass

# update bucket policy
new_policy = open('bucket_policy_1').readlines()

# get policy object for bucket
policy = resource.BucketPolicy('bucket_1')
# write new policy
policy.put(Policy=new_policy)

# list the bucket policies again
try:
    print s3.get_bucket_policy(Bucket='bucket_1')
except:
    pass
