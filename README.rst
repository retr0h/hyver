*****
hyver
*****

hyver - Manage xhyve instances.

$ mkdir -p vms/centos7 && cd vms/centos7

$ wget http://centos.mirror.lstn.net/7/isos/x86_64/CentOS-7-x86_64-Minimal-1611.iso
$ dd if=/dev/zero bs=2k count=1 of=/tmp/tmp.iso
$ dd if=CentOS-7-x86_64-Minimal-1611.iso bs=2k skip=1 >> /tmp/tmp.iso
$ hdiutil attach /tmp/tmp.iso

$ cp /Volumes/CentOS\ 7\ x86_64/isolinux/vmlinuz .
$ cp /Volumes/CentOS\ 7\ x86_64/isolinux/initrd.img .

$ dd if=/dev/zero of=hdd.img bs=1g count=8

Docs
====

.. code-block:: bash

    $ tox -e doc

License
=======

MIT
