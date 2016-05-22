import boto3, credentials

id, psswd = credentials.id_and_psswd('username')

ec2 = boto3.resource('ec2',
                          region_name='us-west-2',
                          aws_access_key_id=id,
                          aws_secret_access_key=psswd)

instance = ec2.create_instances(
    ImageId='ami-d0f506b0',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    BlockDeviceMappings = [
        {
            'VirtualName': 'ephemeral0',
            'DeviceName': '/dev/sdh',
            'Ebs':
                {
                    'VolumeSize':10,
                    'DeleteOnTermination':True,
                    'VolumeType':'standard',
                    'Encrypted':False
                },
        },
    ],
    Monitoring={'Enabled':True},
    InstanceInitiateShutdownBehaviour='terminate'
)

print instance
