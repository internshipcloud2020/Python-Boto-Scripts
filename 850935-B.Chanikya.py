#To create an EC2 Instance
import sys				# import required files
import boto3
ec2_connection.run_instances('<ami-id>')					# specify the image I'd of the AMI
ec2.create_instances(ImageId='<ami-id>', MinCount=1, MaxCount=5)		# instance gets created for given AMI

#To Stop and Terminate Instances
ec2_connection.stop_instances(instance_ids=ids)				# to stop the particular instance (instance I'd to be given)
ec2_connection.terminate_instances(instance_ids=ids)				# to terminate particular instance 

#To Monitor and Unmonitor Instances
ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':							# to count no:of instances ON 
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)


#To create key_value pair
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='key_value_name')			# to create key_pair
print(response)

#To download file from S3 bucket
bucketname = 'bucket-name' 						#  your bucket name
filename = 'file.png' 							#  your object key
s3 = boto3.resource('s3')
s3.Bucket(bucketname).download_file(filename, 'file.png')			# file name to download


