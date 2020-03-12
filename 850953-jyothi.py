import boto3

import sys

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():

   print instance.id, instance.state

instance = ec2.create_instances(

 ImageId='ami-1e299d7e',

 MinCount=1,

 MaxCount=1,

 InstanceType='t2.micro')

print instance[0].id 
ec2_console_resource=session.resource(service_name="ec2",region_nmae="us-east-1")

my_instance_state=ec2.console_resource.Instance(id=instance[0].id)
print(my_instance.state)