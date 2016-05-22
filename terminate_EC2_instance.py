import boto3, credentials

id, psswd = credentials.id_and_psswd('username')

ec2 = boto3.resource('ec2',
                     region_name='us-west-2',
                     aws_access_key_id=id,
                     aws_secret_access_key=psswd)

ids = [list_of_instance_ids_to_terminate]

ec2.instances.filter(InstanceIds=ids).terminate()
