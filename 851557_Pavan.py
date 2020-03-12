from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient


SUBSCRIPTION_ID = 'subscription-id'
GROUP_NAME = 'myResourceGroup'
LOCATION = 'westus'
VM_NAME = 'myVM'


#to get Active directory credentials
def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = 'application-id',
        secret = 'authentication-key',
        tenant = 'tenant-id'
    )

    return credentials

#To create a Resource group
def create_resource_group(rg_client):
    rg_params = { 'location':LOCATION }
    rg_result = rg_client.resource_groups.create_or_update(GROUP_NAME, rg_params)
    
#To create a public ip address   
def create_public_ip_address(network_client):
    pip_params = {
        'location': LOCATION,
        'public_ip_allocation_method': 'Dynamic'
    }
    pip_result = network_client.public_ip_addresses.create_or_update(GROUP_NAME,'myIPAddress',p_params)

    return pip_result.result()

#To create Virtual Network
def create_vnet(network_client):
    vnet_params = {
        'location': LOCATION,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
    vnet_result = network_client.virtual_networks.create_or_update(GROUP_NAME,'myVNet',vnet_params)
    
    return vnet_result.result()

#To create subnets in the vnet
def create_subnet(network_client):
    subnet_params = {
        'address_prefix': '10.0.0.0/24'
    }
    subnet_result = network_client.subnets.create_or_update(GROUP_NAME,'myVNet','mySubnet',subnet_params)

    return subnet_result.result()

#To create network interface 
def create_nic(network_client):
    subnet_info = network_client.subnets.get(GROUP_NAME, 'myVNet', 'mySubnet')
    publicIPAddress = network_client.public_ip_addresses.get(GROUP_NAME,'myIPAddress')
    nic_params = {
        'location': LOCATION,
        'ip_configurations': [{
            'name': 'myIPConfig',
            'public_ip_address': publicIPAddress,
            'subnet': {
                'id': subnet_info.id
                }
        }]
    }
    nic_result = network_client.network_interfaces.create_or_update(GROUP_NAME, 'myNic', nic_params)

    return nic_result.result()

# To create the virtual machine
def create_vm(network_client, compute_client):  
    nic = network_client.network_interfaces.get(GROUP_NAME, 'myNic')
    vm_params = {
        'location': LOCATION,
        'os_profile': {
            'computer_name': VM_NAME,
            'admin_username': 'azureuser',
            'admin_password': 'Azure12345678'
        },
        'hardware_profile': {
            'vm_size': 'Standard_DS1'
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'MicrosoftWindowsServer',
                'offer': 'WindowsServer',
                'sku': '2012-R2-Datacenter',
                'version': 'latest'
            }
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic.id
            }]
        }
        
    }
    vm_result = compute_client.virtual_machines.create_or_update(GROUP_NAME, VM_NAME, vm_params)

    return vm_result.result()

#To stop the virtual machine
def stop_vm(compute_client):
    compute_client.virtual_machines.power_off(GROUP_NAME, VM_NAME)


    
#Main function

if __name__ == "__main__":
    
    credentials = get_credentials()
    
    rg_client = ResourceManagementClient(credentials,SUBSCRIPTION_ID)
    network_client = NetworkManagementClient(credentials,SUBSCRIPTION_ID)
    compute_client = ComputeManagementClient(credentials,SUBSCRIPTION_ID)
    
    create_resource_group(resource_group_client)
    
    pip_result = create_public_ip_address(network_client)
    print(pip_result)
    
    vnet_result = create_vnet(network_client)
    print(vnet_result)
    
    subn_result = create_subnet(network_client)
    print(subn_result)
    
    nic_result = create_nic(network_client)
    print(nic_result)
    
    vm_result = create_vm(network_client, compute_client)
    print(vm_result)
    
    # To stop the virtual machine
    #stop_vm(compute_client)

    
    
    