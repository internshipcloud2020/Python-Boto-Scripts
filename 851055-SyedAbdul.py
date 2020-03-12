import boto3
resoType = boto3.resource('s3')
for everyBucket in resoType.buckets.all():
 print everyBucket.name
