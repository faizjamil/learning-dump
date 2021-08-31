# What is Ansible?

Ansible is a tool which allows you to automate the following IT tasks
* Configuration Management
* Orchestration
* Deployment

A Playbook is a blueprint of automation tasks (Complex IT actions executed with limited or no human involvement). Playbooks are written in YAML.
Playbooks are essentially frameworks, prewritten code developers can use ad-hoc or as a starting template

WIth Ansible, you can control a variety of systems (or managed nodes, can be thought of as clients) with a sort of parent (or control, or server) node.  

Ansible is a push type of configuration management tool. Meaning that on the parent (or server) node is where you write your configurations and push those files to your managed (or client) nodes.

# How to install general guidelines and procedures

To install ansible for your specific distro, go to the official site for installation instructions.

After installing ansible you must add at least one host in the /etc/ansible/hosts file (also known as the Inventory)

In this file we can simply add a single host to the group "ansible client", the lines you add will look something like this:

```
[ansible_client]
192.168.1.2 ansible_ssh_user=root ansible_ssh_private_key= ~/.ssh/id_ed25519
```
The general syntax for listing multiple hosts per group is something like this

```
[group_name]
<IP of host 1> ansible_ssh_user=<username> ansible_ssh_pass=hunter2
<IP of host 2> ansible_ssh_user=<username> ansible_ssh_pass=*******
...
```

Couple things to note from the above examples.
Next to the IP address of a host we must specify the user name that ansible can log in as through ssh.

Now for the password, you can specify that using ``ansible_ssh_pass=<your password>`` however it is better security practice to use ssh keys and disabling logins with passwords.
To specify a private ssh key file, set the value of the ``ansible_private_key_file`` variable to the path of your private key file.


The examples above are written in an INI style, you can use INI, YAML or JSON in the inventory file.

Note: To prevent the "ssh-key is too open error" assign perms of 600 to your private key, this makes your private key read and writable only to you.



[More information on how to manage your inventory (hosts file)](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters)

How that we have our managed nodes setup, let's write a playbook.
