#Copying Buckets
import boto3
s3_client = boto3.client('s3')

def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)
#Removing the first bucket
s3_resource.Bucket(first_bucket_name).delete()
#Client version to remove the second bucket
s3_resource.meta.client.delete_bucket(Bucket=second_bucket_name)
