from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient

# Set your Azure subscription ID and resource group name
subscription_id = '2377021f-391b-4f19-b40a-422041e73bce'
resource_group_name = 'cloud-shell-storage-centralindia'

# Authenticate using default credentials
credential = DefaultAzureCredential()

# Create the Monitor Management Client
monitor_client = MonitorManagementClient(credential, subscription_id)

# Get a list of Azure resources in the specified resource group
resources = monitor_client.resources.list_by_resource_group(resource_group_name)

# Iterate through the resources and display relevant information
for resource in resources:
    print("Resource ID: {}".format(resource.id))
    print("Resource Name: {}".format(resource.name))
    print("Resource Type: {}".format(resource.type))
    print("Resource Location: {}".format(resource.location))
    print("")

# Add additional monitoring logic as needed
# For example, you can use monitor_client.alerts.list_by_resource() to retrieve alerts for a specific resource
