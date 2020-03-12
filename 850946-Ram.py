
import boto3

h= boto3.resource('ec2')
instance = h.Instance('id')

response = instance.attach_volume(
    Device='string',
    VolumeId='string',
    DryRun=True|False
)
response = instance.start(
    AdditionalInfo='string',
    DryRun=True|False
)
response = instance.stop(
    
    DryRun=True|False,
    Force=True|False
)
response = instance.terminate(
    DryRun=True|False
)