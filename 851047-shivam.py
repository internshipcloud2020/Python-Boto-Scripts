#/usr/bin/python
import boto.ec2
conn = boto.ec2.connect_to_region(“us-east-1”)
conn.run_instances(
    ‘ami-6ac2a85a’,
    key_name=‘shivam-instance’,
    instance_type=‘t2.micro’,
    security_groups=[‘shivam-ssh’]
)
