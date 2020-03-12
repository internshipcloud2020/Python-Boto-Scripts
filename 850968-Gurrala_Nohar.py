import os
import uuid
import sys
from azure.storage.blob import BlockBlobService, PublicAccess

# Block blobs let you upload large blobs efficiently

blob_service_client = BlockBlobService(account_name='accountname', account_key='accountkey')


# To create a container.

container_name = 'DemoContainer'

blob_service_client.create_container(container_name)



# Set the permission so the blobs are public.

blob_service_client.set_container_acl(container_name, public_access=PublicAccess.Container)



# Create Sample folder if it not exists, and create a file in folder Sample to test the upload and download.

local_path = os.path.expanduser("~/Sample")

# Check whether Directory exists or not. If not then Create new directory

if not os.path.exists(local_path):
	
	s.makedirs(os.path.expanduser("~/Sample"))



# Creating a file name

local_file_name = "QuickStart_" + str(uuid.uuid4()) + ".txt"



# Creating a Present working directory of file, including the file name

full_path_to_file = os.path.join(local_path, local_file_name)



# Upload the created file, use local_file_name for the blob name

blob_service_client.create_blob_from_path(container_name, local_file_name, full_path_to_file)



# List the blobs in the container

generator = blob_service_client.list_blobs(container_name)