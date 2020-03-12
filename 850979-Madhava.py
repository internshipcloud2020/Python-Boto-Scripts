##for creating an instancew 

#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(

 ImageId='ami-******',

 MinCount=1,

 MaxCount=1,

 InstanceType='t2.micro')

print instance.id

##for terminating the instance

#!/usr/bin/env python

import sys

import boto3

ec2 = boto3.resource('ec2')

for i in sys.argv[1:]:

 instance = ec2.Instance(i)

 output = instance.terminate()

 print output
