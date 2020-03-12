import json
import boto3

#Using client for AWS service access
s3 = boto3.client('s3')

#Method to read object from s3 bucket 
def lambda_handler(event, context):
       print("Started Execution of lanmba_handler for reading object and downloading file from s3 bucket')

       bucket = 'sample_bucket'
       new_bucket= 'new_sample'
       key = 'content/file1.json'

       #Downloading file/image from s3 bucket to local machine
       s3.download_file('sample_bucket', 'sea.png', 'Users/RR/Desktop/sea.png')
       
       #uploading downloaded file/image to another bucket
       response = s3.upload_file('Users/RR/Desktop/sea.png', new_bucket, 'saved_seaImage.png' )
    
       
       #Placing code within try block to handle run time exceptions
       try:
           #get_object method to return dictionary
           data = s3.get_object(Bucket=bucket, Key=key)
           #Store Body which holds streamingBody in output variable
           output = data['Body'].read()
           
           #return output values from lamba_handler
           return output
       #Handling exception and printing exception details

       except Exception as e:
           print(e)
           raise e

       