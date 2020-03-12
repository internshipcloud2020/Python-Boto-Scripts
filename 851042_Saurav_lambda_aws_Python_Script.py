import boto3
import os

#Adding the aws key and instance from cli using os library

ami_aws = os.environ['AMI']
aws_instance_type= os.environ['INSTANCE_TYPE']
aws_key = os.environ['KEY_NAME']
aws_subnet = os.environ['SUBNET_ID']

ec2_instance = boto3.resource('ec2')

def lambda_handler(event, context):
    #creating the ec2 instance 
    instance = ec2.create_instances(
        ImageId=ami_aws,
        InstanceType=aws_instance_type,
        KeyName=aws_key,
        SubnetId=aws_subnet,
        MaxCount=1,
        MinCount=1
    )

    print("Creating a New Instance:", instance[0].id)
