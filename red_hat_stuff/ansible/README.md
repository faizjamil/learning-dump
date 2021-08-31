# How to install ansible 

This is assuming an Ubuntu installation

## 1. First, ensure that python3 and pip3 are installed
```sh

$ python3 --version
```

If this doesn't return a version number, install python3 and pip

```sh 
$ sudo apt-get update && sudo apt-get install python3 python3-pip
```

To verify that python3 is installed, run the command shown above again

```sh
$ python3 --version
```

To verify that pip3 is installed, check if this works
```sh
pip3 --version
```
## 2. Install ansible using pip3
```sh
$ python3 -m pip3 install --user ansible
```

Once this installation completes, we need to do one more step to ensure we can use ansible.
If you try the `ansible` command now, you will get a `command not found` error. Ansible is installed, however it is not installed globally, it's only installed for this one user.
You might find somewhere along the installation you get a warning that you need to add `./local/bin` to your `PATH`.

## 3. Add install location of ansible to PATH
This assumes `zsh` instead of bash, but the general steps are the name

1. Open your `.zshrc` file located in your home directory in your text editer of choice.
```sh
$ nano ~/.zshrc
```

Add the following **exactly** to the end of your `.zshrc` file
```sh
# Adds .local/bin to path
export PATH="$HOME/.local/bin:$PATH"
```

Exit and Save (CTRL + X, then hit ENTER)

Restart your shell, if you get some error about your .zshrc file, navigate to `/bin` then use `nano` and any other commands from there as **most commands will not work as those programs are stored in /bin**
```sh
$ cd /bin
$ nano ~/.zshrc
```

From here, revert the changes you made and continue troubleshooting.

## 4. Verify ansible is installed
Run the following command to verify ansible is installed and what version is installed.

```sh
$ ansible --version
```
You should get something like this as your output
```sh
ansible [core 2.11.4]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/faizan/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/faizan/.local/lib/python3.8/site-packages/ansible
  ansible collection location = /home/faizan/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/faizan/.local/bin/ansible
  python version = 3.8.10 (default, Jun  2 2021, 10:49:15) [GCC 9.4.0]
  jinja version = 2.10.1
  libyaml = True
```

Congratulations, you have installed ansible!
