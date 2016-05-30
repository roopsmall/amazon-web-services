import boto3, credentials

id, psswd = credentials.id_and_psswd('username')
client = boto3.client('iam',aws_access_key_id=id, aws_secret_access_key=psswd)
policy_statement = open('policy_statement_1.txt').readlines()
print client_put_user_policy(UserName='user_name_1',
                                  PolicyName='EC2_Allow_All',
                                  Policy_Document=policy_statment)

