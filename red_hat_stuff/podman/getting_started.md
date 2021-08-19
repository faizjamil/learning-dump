
# Getting Started
First you install podman, follow the instructions for your distro linked above.

To search for images use the following command
```sh
posmon search <search term, such as a package or base image>
```

For example searching for "nginx" yields the following

```sh
$ podman search nginx

INDEX       NAME                                                                  DESCRIPTION                                      STARS       OFFICIAL    AUTOMATED
docker.io   docker.io/library/nginx                                               Official build of Nginx.                         15297       [OK]
docker.io   docker.io/jwilder/nginx-proxy                                         Automated Nginx reverse proxy for docker con...  2058                    [OK]
docker.io   docker.io/nginxinc/nginx-unprivileged                                 Unprivileged NGINX Dockerfiles                   46
docker.io   docker.io/nginx/nginx-ingress                                         NGINX and  NGINX Plus Ingress Controllers fo...  55
docker.io   docker.io/nginxdemos/hello                                            NGINX webserver that serves a simple page co...  70                      [OK]
docker.io   docker.io/privatebin/nginx-fpm-alpine                                 PrivateBin running on an Nginx, php-fpm & Al...  56                      [OK]
docker.io   docker.io/richarvey/nginx-php-fpm                                     Container running Nginx + PHP-FPM capable of...  815                     [OK]
docker.io   docker.io/mailu/nginx                                                 Mailu nginx frontend
                    9                       [OK]
docker.io   docker.io/nginx/nginx-prometheus-exporter                             NGINX Prometheus Exporter for NGINX and NGIN...  19
docker.io   docker.io/jlesage/nginx-proxy-manager                                 Docker container for Nginx Proxy Manager         130                     [OK]
docker.io   docker.io/wodby/nginx                                                 Generic nginx
                    1                       [OK]
docker.io   docker.io/linuxserver/nginx                                           An Nginx container, brought to you by LinuxS...  150
docker.io   docker.io/jc21/nginx-proxy-manager                                    Docker container for managing Nginx proxy ho...  228
docker.io   docker.io/ansibleplaybookbundle/nginx-apb                             An APB to deploy NGINX                           2                       [OK]
docker.io   docker.io/staticfloat/nginx-certbot                                   Opinionated setup for automatic TLS certs lo...  24                      [OK]
docker.io   docker.io/tiangolo/nginx-rtmp                                         Docker image with Nginx using the nginx-rtmp...  138                     [OK]
docker.io   docker.io/centos/nginx-112-centos7                                    Platform for running nginx 1.12 or building ...  15
docker.io   docker.io/schmunk42/nginx-redirect                                    A very simple container to redirect HTTP tra...  19                      [OK]
docker.io   docker.io/centos/nginx-18-centos7                                     Platform for running nginx 1.8 or building n...  13
docker.io   docker.io/sophos/nginx-vts-exporter                                   Simple server that scrapes Nginx vts stats a...  7                       [OK]
docker.io   docker.io/alfg/nginx-rtmp                                             NGINX, nginx-rtmp-module and FFmpeg from sou...  105                     [OK]
docker.io   docker.io/bitwarden/nginx                                             The Bitwarden nginx web server acting as a r...  11
docker.io   docker.io/nginxproxy/nginx-proxy                                      Automated Nginx reverse proxy for docker con...  16
docker.io   docker.io/jasonrivers/nginx-rtmp                                      Docker images to host RTMP streams using NGI...  92                      [OK]
docker.io   docker.io/raulr/nginx-wordpress                                       Nginx front-end for the official wordpress:f...  13                      [OK]
quay.io     quay.io/kubernetes-ingress-controller/nginx-ingress-controller        NGINX Ingress controller built around the [K...  0
quay.io     quay.io/opencloudio/ibm-ingress-nginx-operator                        # IBM Ingress Nginx Operator  **Important:**...  0
quay.io     quay.io/ukhomeofficedigital/nginx-proxy                               # OpenResty Docker Container  [![Build Statu...  0
quay.io     quay.io/bitnami/nginx                                                 Official build of [Bitnami nginx](https://gi...  0
quay.io     quay.io/ocsci/nginx
                    0
quay.io     quay.io/jitesoft/nginx                                                # Nginx  [![Docker Pulls](https://img.shield...  0
quay.io     quay.io/redhattraining/hello-world-nginx
                    0
quay.io     quay.io/openshift-scale/nginx
                    0
quay.io     quay.io/dtan4/nginx-basic-auth-proxy
                    0
quay.io     quay.io/kubernetes-ingress-controller/nginx-ingress-controller-amd64  NGINX Ingress controller built around the [K...  0
quay.io     quay.io/sjenning/nginx
                    0
quay.io     quay.io/opencloudio/nginx-ingress-controller
                    0
quay.io     quay.io/aptible/nginx                                                 ![](https://quay.io/repository/aptible/nginx...  0
quay.io     quay.io/opencloudio/ibm-management-ingress-operator                   # IBM Management Ingress Operator  **Importa...  0
quay.io     quay.io/centos7/nginx-116-centos7                                     Nginx is a web server and a reverse proxy se...  0
quay.io     quay.io/opencloudio/icp4data-nginx-repo
                    0
quay.io     quay.io/domino/model-api-nginx
                    0
quay.io     quay.io/rebuy/nginx-exporter
                    0
quay.io     quay.io/openshifttest/nginx-alpine
                    0
quay.io     quay.io/bitnami/nginx-ingress-controller                              Official build of [Bitnami CONTAINERNAME](ht...  0
quay.io     quay.io/testing-farm/nginx                                            Mirror of `docker.io/nginx/nginx` images, to...  0
quay.io     quay.io/opencloudio/ibm-ingress-nginx-operator-bundle
                    0
quay.io     quay.io/bitnami/nginx-exporter
                    0
quay.io     quay.io/bedrock/nginx
                    0
quay.io     quay.io/evanshortiss/s2i-nodejs-nginx                                 Build static sites using Node.js, and packag...  0
```

Now considering this is a lot of results we want to filter our search, one such filter we can use is to check if the image is marked as official

We simply add the "--filters=" flag with the filer "is-official"

Searching for official nginx images now gives us fewer results

```sh
$ podman search nginx --filter=is-official
INDEX       NAME                     DESCRIPTION               STARS       OFFICIAL    AUTOMATED
docker.io   docker.io/library/nginx  Official build of Nginx.  15297       [OK]
```

Note that the image names we get are prefixed with what looks like a url such as "docker.io" or "quay.io"
These are package registeries, from learning Docker we know that these are repositories used to store container images.

We have to keep in mind that podman searches across a number of registeries if we simply search a name such as "nginx".

When pulling an image we need to include it's registry to make sure we are using the correct image.

If we wanted to pull the official nginx image which is on the docker.io registery, we would use this command/

```sh
$ podman pull docker.io/library/nginx 
```

The syntax of the pull command therefore is
```sh
$ podman pull <image_name>
```

To view the images present on your machine, run
```sh
$ podman images
```
You will get something like this as output, one line per image on your machine

```sh
REPOSITORY                         TAG         IMAGE ID      CREATED      SIZE
registry.fedoraproject.org/fedora  34          37e5619f4a8c  2 days ago   184 MB
```

If we want to pull and run an httpd image, we perform the following commands
```sh
$ podman pull docker.io/library/httpd
$ podman run -dt -p 8080:80/tcp docker.io/library/httpd
```

Let's go through the flags of the run command one by one

[To Be completed after consulting docs]

## List running containers
To list created and running containers use the ps command
```sh
$ postman ps
```
Adding the -a flag lists all containers (created, exited, running, etc.)

## testing the httpd container
To test that httpd image we loaded earlier, we use curl to ping the site on port 8080

```sh
$ curl http://localhost:8080
```

This should return the following HTML, indicating that the httpd container works ok.


```html
<html><body><h1>It works!</h1></body></html>
```
## Inspect a running container

Use the `podman inspect` command to get metadata and other information about a running container

Note that the `-l` flag = **latest container**

You can also specify a container ID or name or the long argument `--latest`

Ex:
```sh
$ podman inspect -l | grep IPAddress
``` 
gives us this output
```sh
            "IPAddress": "",
```

Since the container is running in **rootless** mode no IP Address is assigned.

## Viewing container's logs

Use the `podman logs` command

Can use either the `-l` flag or the ID of a container

Ex: (Note: Do not copy the container ID as it is unique)

```sh
$ podman logs cc1a216f29fd
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 10.0.2.100. Set the 'ServerName' directive globally to suppress this message
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 10.0.2.100. Set the 'ServerName' directive globally to suppress this message
[Wed Aug 11 19:44:47.791011 2021] [mpm_event:notice] [pid 1:tid 140643870925952] AH00489: Apache/2.4.48 (Unix) configured -- resuming normal operations
[Wed Aug 11 19:44:47.792638 2021] [core:notice] [pid 1:tid 140643870925952] AH00094: Command line: 'httpd -D FOREGROUND'
10.0.2.100 - - [11/Aug/2021:19:48:50 +0000] "GET / HTTP/1.1" 200 45
```

## Viewing a container's pids (running processes)
In this httpd container you can observe httpd running with the `podman top` command, specify latest container or a container ID as above
`podman top <-l or container ID>`

```sh
$ podman top -l
USER        PID         PPID        %CPU        ELAPSED          TTY         TIME        COMMAND
root        1           0           0.000       41m7.125023007s  pts/0       0s          httpd -DFOREGROUND
daemon      3           1           0.000       41m7.125447448s  pts/0       0s          httpd -DFOREGROUND
daemon      4           1           0.000       41m7.125816383s  pts/0       0s          httpd -DFOREGROUND
daemon      5           1           0.000       41m7.126158757s  pts/0       0s          httpd -DFOREGROUND
```

## Stopping a container

Use the `podman stop` command with the following syntax
`podman stop <-l or container ID>`

verify the container has stopped by checking it's status. Include the -a flag in the `ps` command

```sh
podman stop -l
cc1a216f29fd3057aef7c353fce67911cdb22b3e72e503fc90906eb2e10c532f

podman ps -a                                                     

CONTAINER ID  IMAGE                           COMMAND           CREATED         STATUS                    PORTS                 NAMES
cc1a216f29fd  docker.io/library/httpd:latest  httpd-foreground  42 minutes ago  Exited (0) 5 seconds ago  0.0.0.0:8080->80/tcp  busy_nightingale
```
## Removing a container

Use the ``rm`` command specifying either the latest or a specific container by ID.

```
$ podman rm -l
```
