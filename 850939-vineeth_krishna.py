#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instance(
 ImageId='ami-1e299d7e',
 InstanceType='t2.micro')
print instance[0].id

#!/usr/bin/env python
import sys
import boto3
ec2 = boto3.resource('ec2')
 instance = ec2.Instance(instance_id)
 response = instance.terminate()
 print response

