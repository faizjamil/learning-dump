# What is Ansible?

Ansible is a tool which allows you to automate the following IT tasks
* Configuration Management (Consistency of all systems in the infrastructure is maintained)
* Orchestration (Integration of multiple applications and executing them in a specific order)
* Deployment (Applications are deployed automatically on a variety of environments)

A Playbook is a blueprint of automation tasks (Complex IT actions executed with limited or no human involvement). Playbooks are written in YAML.
Playbooks are essentially frameworks, prewritten code developers can use ad-hoc or as a starting template

WIth Ansible, you can control a variety of systems (or managed nodes, can be thought of as clients) with a sort of parent (or control, or server) node.  

A code is written once for the installation and deployed multiple times, allows for deployment of services consistently.


Pull configuration: Nodes check with the server periodically and fetch the configurations from it. Need to install some sort of client on each node. (Examples: Chef and Puppet)

Push configuration: Server pushes configuration to the nodes.

Ansible is a push type of configuration management tool. Meaning that on the parent (or server) node is where you write your configurations and push those files to your managed (or client) nodes.

# Architecture
Local machine: Where you install Ansible
Node: A system to be controlledd by the local machine
Module: A collection of config files
Inventory: A document that groups the nodes under specific labels. The path to your inventory (also called hosts) file is commonly `/etc/ansible/hosts`


Local machine is where your module and inventory are stored.

Local machine connects to the nodes via an SSH client.

# How to install general guidelines and procedures

[Here is a set of instructions](README.md) which should work on Ubuntu or any distro that uses `apt`. However the steps using `pip` can be applied to any distro.

In general it is recommended by the official Ansible site to install Ansible through `pip3` (Referred to as such on Ubuntu. might be called `pip` if Python 3 is the only version of Python you have installed)

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

# Working with playbooks


Playbooks are instructions to configure the nodes, written in `YAML`.

Generally, a playbook looks something like this:
```YAML
---
- name: sample book
# hosts = managed nodes = clients
  hosts: ansible_client

# I'm not going to assign a user in a playbook for security reasons
#  remote_user: root
  become: true
# the above are all at one level of indentation
  
  tasks:
# the below config is meant to be used on an RHEL distro of some sort, such as Fedora or Oracle Linux

    - name: install httpd
      yum: 
          name: httpd
          state: latest
    - name: run httpd
      service:
          name: httpd
          state: started
    - name: create content
      copy:
          content: "congrats on installing ansible"
          dest: /var/www/html/index.html

```

Here, we give this playbook a name and then add tasks, each with its own name, followed by instructions to execute the task.

[List of collections you can use when defining tasks](https://docs.ansible.com/ansible/latest/collections/index.html#list-of-collections)

Before we execute a playbook, we can pass the `--syntax-check` flag to the `ansible-playbook` command like so:

```sh
$ ansible-playbook sample_playbook.yml --syntax-check
```
If your output looks something like this:
```sh
$ ansible-playbook sample_playbook.yml --syntax-check

playbook: sample_playbook.yml
```
It means there were no syntax errors found.

To push a playbook to a client machine, use the `ansible-playbook` command like so.


```sh
ansible-playbook sample_playbook.yml --ask-become-pass
```

We need to pass that --ask-become-pass flag in order to run the tasks in the playbook as the root user (essentially running `sudo <command>`
[Here's more information about that](https://www.middlewareinventory.com/blog/ansible-sudo-ansible-become-example/)


If the commands succeeds you will get an output similar to the following
```sh
PLAY [sample book] *************************************************************

TASK [Gathering Facts] *********************************************************
[DEPRECATION WARNING]: Distribution fedora 34 on host 192.168.1.204 should use
/usr/bin/python3, but is using /usr/bin/python for backward compatibility with
prior Ansible releases. A future Ansible release will default to using the
discovered platform python for this host. See https://docs.ansible.com/ansible/
2.11/reference_appendices/interpreter_discovery.html for more information. This
 feature will be removed in version 2.12. Deprecation warnings can be disabled
by setting deprecation_warnings=False in ansible.cfg.
ok: [192.168.1.204]

TASK [install httpd] ***********************************************************
ok: [192.168.1.204]

TASK [run httpd] ***************************************************************
ok: [192.168.1.204]

TASK [create content] **********************************************************
ok: [192.168.1.204]

PLAY RECAP *********************************************************************
192.168.1.204              : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

The "Gathering facts" task fetches the state of the client machine to see what needs to be changed and what is already present. On each subsequent task, if that task does not need to be run for some reason (if you already have `httpd` installed for example), you will get an output of "ok" from that task. If you get "changed" as your output from a task, it means that task was executed.

The recap section lists the results of executing the playbook, lists the number of errors, changes, tasks that went ok, were ignored, etc.




# Ansible Tower
A framework for Ansible which uses a GUI created by Red Hat. More approachable to those who don't like the command line.

[Source of most of the info above](https://youtu.be/EcnqJbxBcM0)