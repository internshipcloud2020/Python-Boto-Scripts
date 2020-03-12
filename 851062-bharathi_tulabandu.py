	 # import required files
	import sys                        
	import boto3
	# specify the image I'd of the AMI
	ec2_connection.run_instances('<ami-id>') 
	# instance gets created for given AMI
	ec2.create_instances(ImageId='<ami-id>', MinCount=1, MaxCount=3)        
	# to stop the particular instance (instance I'd to be given)
	ec2_connection.stop_instances(instance_ids=ids)    
	# to terminate particular instance 
	ec2_connection.terminate_instances(instance_ids=ids)                          
	 # to create key_pair
	ec2 = boto3.client('ec2')
	response = ec2.create_key_pair(KeyName='Name')               
	print(response)
	# to count no:of running instances
	ec2 = boto3.client('ec2')
	if sys.argv[1] == 'ON':                                               
	    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
	else:
	    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
	print(response)
	
	
	
	
	

