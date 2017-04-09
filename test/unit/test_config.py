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

import uuid

import pytest

from hyver import config


@pytest.fixture
def empty_config_instance(config_instance):
    config_instance.config = {}

    return config_instance


def test_hyver_file_member(hyver_file, config_instance):
    assert hyver_file == config_instance.hyver_file


def test_args_member(config_instance):
    assert {} == config_instance.args


def test_command_args_member(config_instance):
    assert {} == config_instance.command_args


def test_config_member(config_instance):
    assert isinstance(config_instance, config.Config)


def test_acpi_property(config_instance):
    assert config_instance.acpi is None


def test_kernel_property(config_instance):
    assert './vmlinuz' == config_instance.kernel


def test_initrd_property(config_instance):
    assert './initrd.img' == config_instance.initrd


def test_cmdline_property(config_instance):
    assert 'earlyprintk=serial console=ttyS0' == config_instance.cmdline


def test_mem_property(config_instance):
    assert 'mem-override' == config_instance.mem


def test_mem_property_default(empty_config_instance):
    assert 1024 == empty_config_instance.mem


def test_cpus_property(config_instance):
    assert 'cpus-override' == config_instance.cpus


def test_cpus_property_default(empty_config_instance):
    assert 1 == empty_config_instance.cpus


def test_net_property(config_instance):
    assert '2:0,virtio-net' == config_instance.net


def test_img_cd_property(config_instance):
    x = '3,ahci-cd,./CentOS-7-x86_64-Minimal-1611.iso'
    assert x == config_instance.img_cd


def test_img_hdd_property(config_instance):
    assert '4,virtio-blk,./hdd.img' == config_instance.img_hdd


# Test that it doesn't change on each call
def validate_uuid4(uuid_string):
    try:
        return uuid.UUID(uuid_string, version=4)
    except:
        return False


def test_uuid_property(config_instance):
    assert validate_uuid4(config_instance.uuid)


def test_pci_dev_property(config_instance):
    assert '0:0,hostbridge -s 31,lpc' == config_instance.pci_dev


def test_lpc_dev_property(config_instance):
    assert 'com1,stdio' == config_instance.lpc_dev


def test_get_config(config_instance):
    assert isinstance(config_instance._get_config(), dict)


def test_get_config_exits_when_missing_config():
    with pytest.raises(SystemExit) as e:
        config.Config('missing-file')

    assert 1 == e.value.code


def test_hyver_file():
    assert 'hyver.yml' == config.hyver_file()
