
import pandas as pd 

import json

import azure.cosmos.cosmos_client as cosmos_client

import azure.cosmos.errors as errors

import azure.cosmos.documents as documents

import azure.cosmos.http_constants as http_constants

config = {

    "endpoint": "YOUR ENDPOINT HERE",

    "primarykey": "YOUR PRIMARY KEY HERe"


client = cosmos_client.CosmosClient(url_connection=config["endpoint"], auth={"masterKey":config["primarykey"]}

)
database_name = 'HDIdatabase'

try:

    database = client.CreateDatabase({'id': database_name})

except errors.HTTPFailure:

    database = client.ReadDatabase("dbs/" + database_name)