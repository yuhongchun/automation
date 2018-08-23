#!/bin/bash

CHROOT=`pwd`
if [ ! -d ${CHROOT}/bin ]; then mkdir ${CHROOT}/bin; fi
if [ ! -d ${CHROOT}/etc ]; then mkdir ${CHROOT}/etc; fi
if [ ! -d ${CHROOT}/usr ]; then mkdir ${CHROOT}/usr; fi
if [ ! -d ${CHROOT}/usr/bin ]; then mkdir ${CHROOT}/usr/bin; fi
if [ ! -d ${CHROOT}/usr/lib ]; then mkdir ${CHROOT}/usr/lib; fi
if [ ! -d ${CHROOT}/lib ]; then mkdir ${CHROOT}/lib; fi
if [ ! -d ${CHROOT}/lib64 ]; then mkdir ${CHROOT}/lib64; fi
if [ ! -d ${CHROOT}/dev ]; then mkdir ${CHROOT}/dev; fi
mkdir -p ${CHROOT}/tmp
chmod 0777 ${CHROOT}/tmp

cp /bin/ps ${CHROOT}/bin/
cp /bin/sh ${CHROOT}/bin/
cp /lib/libnss_* ${CHROOT}/lib/
cp /lib64/libnss_* ${CHROOT}/lib64/
cp /lib/x86_64-linux-gnu/libns* ${CHROOT}/lib/
cp /lib/x86_64-linux-gnu/libresolv* ${CHROOT}/lib/
cp /usr/lib/liblwres.so.80* ${CHROOT}/lib/
cp /usr/lib/libdns.so.88* ${CHROOT}/lib/
cp /usr/lib/libbind9.so.80* ${CHROOT}/lib/

if [ ! -d ${CHROOT}/usr/share ]; then
        mkdir ${CHROOT}/usr/share
        cp -rf /usr/share/zoneinfo ${CHROOT}/usr/share/
fi
cp /etc/resolv.conf ${CHROOT}/etc/resolv.conf
cp /etc/localtime ${CHROOT}/etc/localtime
#Copy librarys
ldd `which php5-fpm` | sed -e 's/[ \t]*//g' -e 's/^.*=>//' -e 's/(.*)$//' | xargs -i cp --parents {} ${CHROOT}/
ldd `which sh` | sed -e 's/[ \t]*//g' -e 's/^.*=>//' -e 's/(.*)$//' | xargs -i cp --parents {} ${CHROOT}/
grep -E 'www-data' /etc/passwd > ${CHROOT}/etc/passwd
grep -E 'www-data' /etc/group > ${CHROOT}/etc/group
if [ ! -e ${CHROOT}/dev/null ]; then
        mknod dev/null    c  1 3   # Linux?
        mknod dev/random  c  1 8
        mknod dev/urandom c  1 9
        mknod -m 666 dev/tty c 5 0
        mknod dev/zero    c 2 12   # FreeBSD,  OpenBSD
        mknod dev/stdin   c 22 0   # FreeBSD?, OpenBSD
        mknod dev/stdout  c 22 1   # FreeBSD?, OpenBSD
        mknod dev/stderr  c 22 2   # FreeBSD?, OpenBSD
        mkdir dev/pts
        mount -t devpts none "dev/pts" -o ptmxmode=0666,newinstance
        ln -fs "pts/ptmx" "dev/ptmx"
        mknod dev/pts/0 c 136 0
        mknod dev/pts/1 c 136 1
        mknod dev/pts/2 c 136 2
        mknod dev/pts/3 c 136 3
        mknod dev/pts/ptmx c 5 2
        chmod 0666 dev/* dev/pts/*
fi