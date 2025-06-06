Installing SimpleSAMLphp from the repository
============================================

These are some notes about running SimpleSAMLphp from the repository.

Prerequisites
-------------

Review the [prerequisites](simplesamlphp-install) from the main installation guide.

Installing from git
-------------------

Go to the directory where you want to install SimpleSAMLphp:

```bash
cd /var
```

The `master` branch is not stable and targets the next major release.
Pick a [tag](https://github.com/simplesamlphp/simplesamlphp/tags) to use.

Then do a git clone:

```bash
git clone --branch <tag_name> https://github.com/simplesamlphp/simplesamlphp.git simplesamlphp
```

Initialize configuration and metadata:

```bash
cd /var/simplesamlphp
cp config/config.php.dist config/config.php
cp config/authsources.php.dist config/authsources.php
cp metadata/saml20-idp-hosted.php.dist metadata/saml20-idp-hosted.php
cp metadata/saml20-idp-remote.php.dist metadata/saml20-idp-remote.php
cp metadata/saml20-sp-remote.php.dist metadata/saml20-sp-remote.php
```

The default config.php has a setting `cachedir` which defaults to
`/var/cache/simplesamlphp`. This directory should exist and be
writable by the web server user. You may like to consider something
like the ACL commands from the [Symfony
website](https://symfony.com/doc/current/setup/file_permissions.html#1-using-acl-on-a-system-that-supports-setfacl-linux-bsd)
to enable access to this cache directory.

Install the external dependencies with Composer (you can refer to
[getcomposer.org](https://getcomposer.org/) to get detailed
instructions on how to install Composer itself):

```bash
php composer.phar install
```

When installing on Windows, use:

```bash
php composer.phar install --ignore-platform-req=ext-posix
```

Upgrading
---------

Go to the root directory of your SimpleSAMLphp installation:

```bash
cd /var/simplesamlphp
```

Ask git to update to update the local repository information:

```bash
git fetch origin
```

If you installed as described above, you will be using a
[tag](https://github.com/simplesamlphp/simplesamlphp/tags) for a
specific release. You can see the current tag you are using and
checkout a newer one with the below commands:

```bash
git branch
* (HEAD detached at v2.2.1)
git checkout v2.2.2
```

Install or upgrade the external dependencies with Composer:

```bash
php composer.phar install
```

When using Windows see the additional options for this composer
command shown at the end of the installation step above.
