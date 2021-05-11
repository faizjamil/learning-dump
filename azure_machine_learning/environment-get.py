from azureml.core import Workspace, Environment
from azureml.core.conda_dependencies import CondaDependencies

ws = Workspace.from_config()
env = Environment.get(workspace=ws, name="AzureML-Minimal")
# Installs pillow package
envs = Environment.list(workspace=ws)
for env in envs:
    if env.startswith("AzureML"):
        print("Name",env)
        print("packages", envs[env].python.conda_dependencies.serialize_to_string())