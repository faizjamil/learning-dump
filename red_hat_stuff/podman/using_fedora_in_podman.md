# Using a disposable Fedora install in podman

## Obtain the latest Fedora v34 image from the official Fedora container registry

```sh
$ podman pull registry.fedoraproject.org/fedora:34
```

Then, run the `podman images` command to get the id of this container

Finally, execute the ``run`` command in podman with the -i and -t flags (both can be combined using one "-")

```sh
$ podman  run -it <Fedora image ID>
```

This will drop you into a shell on a Fedora 34 install.

From here, you can do whatever tyou need to.

Once you exit the shell (with the `exit` command) the Fedora container is destroyed.
