# Building packages in RPM

You will need to know how to use a text editor and how to run commands in the terminal to build, sign, and distribute an RPM.
You will need basic knowledge about the Linux terminal.

## WHy should you learn this?

You can:

* Include metadata describing its components, version, size, package group, url, etc.
* Add the project to a `yum` repo to facilitate distribution
* Allow users to use tools such as `yum`, `rpm`, and `PackageKit` to find, install, remove, and otherwise manage your software
* Easily deploy and manage your software using those same tools


## The `SPEC` file

Most of the work to build a package involves creating a `SPEC` file

A `SPEC` file allows you to do the following

* Identify components, config files, docs, and other items in your package
* Define where to install components on the target Linux system
* Set perms and ownership of each file
* List dependecies (aka, note when your package depends on certain components being available)
* Tag files as config or doc files
* Run extra commands that execute on the target system when package is installed or removed
* Add `changelog` entries to document changes that have been made in each versioin of your software


## Rebuilding an existing source code package into an RPM

A good way to learn RPM is using an exiting source code RPM package and rebuild it. As an example we are rebuilding the `tree` package from an existing source code package

Note: DO NOT use this RPM in production as it conflicts with one already in your RHEL software channels
For the purposes of this example I am using a Fedora container while the documentation for this is using RHEL. Any distro based on RHEL such as Fedora and CentOS should in theory work with the steps outlined below.

1. Log into your Fedora system as a regular user
2. Download the source code package for `tree` using the following command
```sh 
$ wget http://ftp.redhat.com/pub/redhat/linux/enterprise/6Workstation/en/os/SRPMS/tree-1.5.3-2.el6.src.rpm
```
3. Install the source code package, creates a new `rpmbuild` directory in your current working directory
```sh
$ rpm -ihv tree-1.5.3-2.el6.src.rpm
```

Check your current working directory with the `pwd` command
If you are at `/` then change your directory to your home directory `cd ~`

You should now find an `rpmbuild` folder in your home directory 

Your `rpmbuild` directory structure should look something like this
```
~/SPECS
~/SPECS/tree.spec
~/BUILDROOT
~/SOURCES
~/SOURCES/tree-1.5.3.tgz
~/SOURCES/tree-1.2-no-strip.patch
~/SOURCES/tree-no-color-by-default.patch
~/SOURCES/tree-1.2-carrot.patch
~/SOURCES/tree-preserve-timestamps.patch
```
Note that the `rpmbuild` directory includes a `SPEC` directory which contains the `tree.spec` file.
The `SOURCES` directory includes the `tree` tarball of the code and patch files

4. Open and inspect (and optionally change) the tree.spec file in any text editor (note that if you are using the  Fedora 34 container image, use `cat` to show the contents of the file)
It should look something like this
```sh
Summary: File system tree viewer
Name: tree
Version: 1.5.3
Release: 2%{?dist}
Group: Applications/File
License: GPLv2+
Url: http://mama.indstate.edu/users/ice/tree/
Source: ftp://mama.indstate.edu/linux/tree/tree-%{version}.tgz
Patch1: tree-1.2-carrot.patch
Patch2: tree-1.2-no-strip.patch
Patch3: tree-preserve-timestamps.patch
Patch4: tree-no-color-by-default.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%description
The tree utility recursively displays the contents of directories in a treelike format. Tree is basically a UNIX port of the DOS tree utility.%prep
%setup -q
# Fixed spelling mistake in man page.
%patch1 -p1 -b .carrot
# Don't strip binary in the Makefile -- let rpmbuild do it.
%patch2 -p1 -b .no-strip
# Preserve timestamp on man page.
%patch3 -p1 -b .preserve-timestamps
# Disable color output by default.
%patch4 -p1 -b .no-color-by-default
%build
make CFLAGS="$RPM_OPT_FLAGS" "CPPFLAGS=$(getconf LFS_CFLAGS)" %{?_smp_mlags}
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make BINDIR=$RPM_BUILD_ROOT%{_bindir} \
 MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
 install
chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/tree.1
%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(-,root,root)
%{_bindir}/tree
%{_mandir}/man1/tree.1*
%doc README LICENSE
%changelog
 ...

```

SOme fields here are self-explanatory such as name and summary
`URL` points to the site of the project that produced the source code.

`Source` points to where the original source code used to makew the package came from
`BuildRoot` is where the temp directory the RPM will be built in is located

5. Build the RPM
Run the `rpmbuild` command to turn your spec file and content into an RPM package for distribution

You can also package the source into a separate source RPM package.

Install the `rpm-build` package as root and run `rpmbuild` as a non-root user.
```sh
# yum install rpm-build - Run as root
$ rpmbuild -ba ~/rpmbuild/SPECS/tree.spec # Run as regular user account
```

This creates a binary RPM and a source RPM in the RPMS and SRPMS directories.
6. Sign the RPM

This requires you generate a public and private key pair. Use the private key for signing the RPM then give the public key to clients for them to check your signed package

```sh
$ gpg --gen-key #Generate public/private keys
```
You can use most of the defaults when generating a keypair

You will get an output similar to the following
```
pub 2048R/99A9CF07 2011-09-16 
Key fingerprint = 90BF B5DC 628E C9E0 88D0 E5D1 E828 4641 99A9 CF07 
uid Chris Negus (My own build of the tree package.) <cnegus@redhat.com> 
sub 2048R/48E60E56 2011-09-16 
```

Use the key ID generated (99A9CF07) to export your private key to a public key.

```sh
$ gpg -a -o RPM-GPG-KEY-ABC –-export 99A9CF07 #Export public key
```

To ensure the key ID is used to sign your package, open the `.rpmmacros` file in your home directory and add a `__gpg__` name line with your private key

```sh
$ vi ~/.rpmmacros #Add _gpg_name keyID to your .rpmmacros file
%_gpg_name 99A9CF07
```
To sign the package run this command:
```sh
$ rpm –-resign ~/rpmbuild/RPMS/x86_64/tree-1.5.3-2.el6.x86_64.rpm #Sign pkg
```
7. Publish the RPM in a `yum` repo
One way to do so is creating a `yum` repo accessible from a web server.
The following commands assume that you runnning a web server on the system you are running these commands on.

```sh
$ mkdir /var/www/html/abc 
$ cp ~/RPM-GPG-KEY-ABC /var/www/html/abc/ #Make the public key available
$ cp ~/rpmbuild/RPMS/x86_84/tree-1.5.3-2.el6.x86_64.rpm /var/www/html/abc/
$ createrepo /var/www/html/abc #Create the repository
```
8. Create a Repository (`.repo`) file

A `.repo` file identifies the URL to the repo.
Clients who want to install the package can copy the `abc.repo` file (in the commands below) to their `/etc/yum.repos.d` directory to enable it.

```sh
$ vim abc.repo
    [abc-repo]
    name=My ABC yum repository
    baseurl=http://whatever.example.com/abc
    gpgkey= http://whatever.example.com/RPM-GPG-KEY-ABC
$ cp abc.repo /var/www/html/abc
```
8. Prepare clients to install the RPM.

As stated above, clients need to copy a `.repo` file to their `/etc/yum.repos.d` directory, then use the `yum` commands to install the package.

```sh
$ wget http://whatever.example.com/abc/abc.repo -O /etc/yum.repos.d/abc.repo
$ yum install tree
```

To update the RPM, rebuild it, copy latest version to your `yum` repo and rerun the `createrepo` command. Clients will get the package next time they install or update the package.

## Checking your RPM package

