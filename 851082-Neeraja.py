import json
import boto3

bucket_name = '851082'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{851082}/*'
    }]
}

bucket_policy = json.dumps(bucket_policy)
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket='851082', Policy=bucket_policy)
s3 = boto3.client('s3')
s3.delete_bucket_policy(Bucket='851082')
s3=boto3.client('s3')
s3.get_bucket_policy(Bucket='851082')

