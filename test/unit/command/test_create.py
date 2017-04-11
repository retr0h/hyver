# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2017 John Dewey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import pytest
import sh

from hyver import config
from hyver.command import create


@pytest.fixture
def create_instance(config_instance, mocker):
    m = mocker.patch(
        'hyver.config.Config.uuid', new_callable=mocker.PropertyMock)
    m.return_value = 'patched-uuid'

    return create.Create(config_instance)


def test_config_member(create_instance):
    assert isinstance(create_instance._config, config.Config)


def test_cmd_member(create_instance):
    assert create_instance._cmd is None


def test_env_member(create_instance):
    assert isinstance(create_instance._env, dict)


def test_bake(create_instance):
    x = [
        str(sh.xhyve),
        '-m mem-override',
        '-c cpus-override',
        '-s 0:0,hostbridge -s 31,lpc',
        '-l com1,stdio',
        '-s 2:0,virtio-net',
        '-s 3,ahci-cd,./CentOS-7-x86_64-Minimal-1611.iso',
        '-s 4,virtio-blk,./hdd.img',
        '-f kexec,vms/centos7/vmlinuz,vms/centos7/initrd.img,"earlyprintk=serial console=ttyS0"',
    ]
    create_instance.bake()

    print str(create_instance._cmd)
    assert ' '.join(x) == str(create_instance._cmd)


def test_execute(config_instance):
    pass


def test_get_cmd(config_instance):
    # NOTE(retr0h): Tested indirectly through bake()
    pass
