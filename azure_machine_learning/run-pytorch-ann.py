# 04-run-pytorch.py
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core import Dataset
from azureml.core.runconfig import DEFAULT_GPU_IMAGE
from azureml.core.conda_dependencies import CondaDependencies
if __name__ == "__main__":
    conda_dep = CondaDependencies(conda_dependencies_file_path="./curated_env.yml")
    ws = Workspace.from_config()
    datastore = ws.get_default_datastore()
    checkpoint_save_location = Dataset.File.from_files(path=(datastore, 'datasets'))
    dataset = Dataset.File.from_files(path=(datastore, 'datasets/categories'))
    experiment = Experiment(workspace=ws, name='ann-train-test')
    config = ScriptRunConfig(source_directory='./src',
                             arguments=[
                             '--dir',dataset.as_named_input('input').as_mount(),
                             '--save_dir',checkpoint_save_location.as_named_input('ann').as_mount(),
                             '--learning_rate', str(0.005)
                             ],
                             script='ann_train.py',
                             compute_target='cpu-cluster')

    # set up pytorch environment
    curated_env = Environment.get(workspace=ws, name="AzureML-PyTorch-1.6-GPU")
    env = curated_env.clone("ANN")
    # Installs pillow package-
    # print(env)
    # print("Name",env)
    print("packages", env.python.conda_dependencies.serialize_to_string())
    
    # conda_dep.add_conda_package("python=3.6.2")
    # conda_dep.add_conda_package("pip=20.2.4")
    # conda_dep.add_conda_package("matplotlib")
    # conda_dep.add_pip_package("torch==1.6.0")
    # conda_dep.add_pip_package("torchvision==0.5.0")
    
    
    # Adds dependencies to PythonSection of myenv
    
    env.python.conda_dependencies=conda_dep    # conda_dep.save('./new_packages.yml')
    print("packages", env.python.conda_dependencies.serialize_to_string())
    
    # env = Environment.from_conda_specification(
    #     name='ann-pytorch-gpu-env',
    #     file_path='./.azureml/ann-pytorch-gpu-env.yml'
    # )
    #env.docker.enabled = True
    #env.docker.base_image = 'mcr.microsoft.com/azureml/openmpi3.1.2-cuda10.2-cudnn7-ubuntu18.04'
    config.run_config.environment = env
    run = experiment.submit(config)

    aml_url = run.get_portal_url()
    print(aml_url)