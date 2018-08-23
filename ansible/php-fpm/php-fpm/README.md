[![Build Status](https://travis-ci.org/NBZ4live/ansible-php-fpm.png?branch=master)](https://travis-ci.org/NBZ4live/ansible-php-fpm)

php-fpm
========

This role installs and configures the php-fpm interpreter.

Requirements
------------

This role requires Ansible 1.4 or higher and tested platforms are listed in the metadata file.

Role Variables
--------------

The variables that can be passed to this role and a brief description about
them are as follows.

    # A list of packages to be installed by the apt module
    apt_packages:
     - php5-cli
     - php5-fpm
     
    # A list of the php.ini directives with values and sections.
    # Note that any valid php.ini directive can be added here.
    # (see the http://php.net documentation for details.)
    # 
    php_config:
      # PHP section directives
      - option: "engine"
        section: "PHP"
        value: "1"
      - option: "error_reporting"
        section: "PHP"
        value: "E_ALL & ~E_DEPRECATED & ~E_STRICT"
      - option: "date.timezone"
        section: "PHP"
        value: "Europe/Berlin"
      # soap section directives
      - option: "soap.wsdl_cache_dir"
        section: "soap"
        value: "/tmp"
      # Pdo_mysql section directives
      - option: "pdo_mysql.cache_size"
        section: "Pdo_mysql"
        value: "2000"
      ...

    # A list of hashs that define fpm configuration
    fpm_config:
     - option: "log_level"
       section: "global"
       value: "notice"
     - option: "syslog.facility"
       section: "global"
       value: "daemon"

    # A list of hashs that define the pools for php-fpm,
    # as with the php.ini directives. Any valid server parameters
    # can be defined here.
    fpm_pools:
      - pool:
          name: foo
          vars:
            - user = www-data
            - group = www-data
            - listen = 8000
            - pm = dynamic
            - pm.max_children = 5
            - pm.start_servers = 2
            - pm.min_spare_servers = 1
            - pm.max_spare_servers = 3
            - chdir = /

Dependencies
------------

None

License
-------

BSD

Author Information
------------------

Sergey Fayngold


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/NBZ4live/ansible-php-fpm/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

