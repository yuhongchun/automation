#!/bin/bash
work="$(dirname $0)/.."

role_name=$1
work_path=$work/$role_name
roles_path=$work_path/roles/$role_name

mkdir -p $work_path
mkdir -p $work_path/group_vars
mkdir -p $roles_path/defaults
mkdir -p $roles_path/tasks
mkdir -p $roles_path/handlers
mkdir -p $roles_path/templates
mkdir -p $roles_path/files
mkdir -p $roles_path/vars
mkdir -p $roles_path/meta

touch $roles_path/defaults/main.yml
touch $roles_path/tasks/main.yml
touch $roles_path/handlers/main.yml
touch $roles_path/vars/main.yml
touch $roles_path/meta/main.yml
touch $work_path/group_vars/all

cat > $work_path/site.yml << _addroleyml
---
- hosts: all
  gather_facts: True

  roles:
    - { role: common , tags: "common"}
    - { role: collectd , tags: "collectd"}
    - { role: zabbix , tags: "zabbix"}
    - { role: $role_name , tags: "$role_name"}
_addroleyml

