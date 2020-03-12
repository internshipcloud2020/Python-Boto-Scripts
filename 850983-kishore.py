import boto3
import pandas as pd


client = boto3.client('s3') 

resource = boto3.resource('s3')
print("enter an not used bucket name")
bucket_name=input()
my_bucket = resource.Bucket(bucket_name)
obj = client.get_object(Bucket='my-bucket', Key='path/to/my/table.csv')
grid_sizes = pd.read_csv(obj['Body'])
obj = client.get_object(Bucket='my-bucket', Key='path/to/my/array.npy')
array = np.load(BytesIO(obj['Body'].read()))
my_bucket.upload_file('file',Key='path/to/my/file')
obj = files[0].get()
print(obj)
