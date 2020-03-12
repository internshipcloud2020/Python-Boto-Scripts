import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '11111111-1111-1111-1111-111111111111') # your Azure Subscription Id
credentials = ServicePrincipalCredentials(
    client_id=os.environ['AZURE_CLIENT_ID'],
    secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant=os.environ['AZURE_TENANT_ID']
)
resource_client = ResourceManagementClient(credentials, subscription_id)
storage_client = StorageManagementClient(credentials, subscription_id)

resource_group_params = {'location':'westus'}
#Check storage account name availability
bad_account_name = 'invalid-or-used-name'
availability = storage_client.storage_accounts.check_name_availability(bad_account_name)
print('The account {} is available: {}'.format(bad_account_name, availability.name_available))
print('Reason: {}'.format(availability.reason))
print('Detailed message: {}'.format(availability.message))

#Create a new storage account
storage_async_operation = storage_client.storage_accounts.create(
    GROUP_NAME,
    STORAGE_ACCOUNT_NAME,
    StorageAccountCreateParameters(
        sku=Sku(name=SkuName.standard_ragrs),
        kind=Kind.storage,
        location='westus'
    )
)
storage_account = storage_async_operation.result()

#List storage accounts
for item in storage_client.storage_accounts.list():
    print_item(item)

#List storage accounts by resource group
for item in storage_client.storage_accounts.list_by_resource_group(GROUP_NAME):
    print_item(item)

#Get the storage account keys
storage_keys = storage_client.storage_accounts.list_keys(GROUP_NAME, STORAGE_ACCOUNT_NAME)
storage_keys = {v.key_name: v.value for v in storage_keys.keys}
print('\tKey 1: {}'.format(storage_keys['key1']))
print('\tKey 2: {}'.format(storage_keys['key2']))

#Regenerate a storage account key
storage_keys = storage_client.storage_accounts.regenerate_key(
    GROUP_NAME,
    STORAGE_ACCOUNT_NAME,
    'key1')
storage_keys = {v.key_name: v.value for v in storage_keys.keys}
print('\tNew key 1: {}'.format(storage_keys['key1']))

#Delete a storage account
storage_client.storage_accounts.delete(GROUP_NAME, STORAGE_ACCOUNT_NAME)
