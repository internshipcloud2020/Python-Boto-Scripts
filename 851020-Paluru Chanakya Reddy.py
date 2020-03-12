#create a container

from azure.storage.blob import ContainerClient
from azure.storage.blob.aio import ContainerClient


container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="my_container")

container_client.create_container()


container_client = ContainerClient.from_connection_string(conn_str="<connection_string>", container_name="my_container")

await container_client.create_container()

# uploading a blob to your container


from azure.storage.blob import BlobClient
from azure.storage.blob.aio import BlobClient

blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    blob.upload_blob(data)


blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

with open("./SampleSource.txt", "rb") as data:
    await blob.upload_blob(data)

#Downloading a blob

from azure.storage.blob import BlobClient

from azure.storage.blob.aio import BlobClient

blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

with open("./BlockDestination.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)



blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

with open("./BlockDestination.txt", "wb") as my_blob:
    stream = await blob.download_blob()
    data = await stream.readall()
    my_blob.write(data)


