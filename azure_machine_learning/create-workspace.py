# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='ann-training', # provide a name for your workspace
                      subscription_id='<azure-subscription-id>', # provide your subscription ID
                      resource_group='s21-ann', # provide a resource group name
                      create_resource_group=True,
                      location='useast1') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')