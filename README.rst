*****
hyver
*****

hyver - Manage xhyve instances.

http://mirrors.acm.wpi.edu/archlinux/iso/2017.04.01/archlinux-2017.04.01-x86_64.iso

iso=archlinux-2017.04.01-x86_64.iso
dd if=/dev/zero bs=2k count=1 of=tmp.iso
dd if=$iso bs=2k skip=1 >> tmp.iso

diskinfo=$(hdiutil attach tmp.iso)
disk=$(echo "$diskinfo" |  cut -d' ' -f1)
mnt=$(echo "$diskinfo" | perl -ne '/(\/Volumes.*)/ and print $1')

cp "$mnt/arch/boot/x86_64/vmlinuz" .
cp "$mnt/arch/boot/x86_64/archiso.img" .
diskutil eject "$disk"

dd if=/dev/zero of=hdd.img bs=100m count=1

Docs
====

.. code-block:: bash

    $ tox -e doc

License
=======

MIT
