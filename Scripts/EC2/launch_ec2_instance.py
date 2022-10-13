import boto3


client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-026b57f3c383c2eec', InstanceType='t2.micro', MinCount=1, MaxCount=1)


for instance in resp['Instances']:
    print(instance['InstanceId'])
