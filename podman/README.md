# Podman Documentation

This folder contains any notes I make when learning how to use podman, a Red Hat tool.

[Getting Started with podman](https://podman.io/getting-started/)



[Link to official documentation](http://docs.podman.io/en/latest/)


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
