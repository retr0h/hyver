# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2017 John Dewey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import uuid

from hyver import logger
from hyver import util

HYVER_FILE = 'hyver.yml'
LOG = logger.get_logger(__name__)


class Config(object):
    def __init__(self, hyver_file, args={}, command_args={}):
        """
        Initialize a new config version one class and returns None.

        :param hyver_file: A string containing the path to the Hyver file
         to be parsed.
        :param args: A dict of options, arguments and commands from the CLI.
        :param command_args: A dict of options passed to the subcommand from
         the CLI.
        :returns: None
        """
        self.hyver_file = hyver_file
        self.args = args
        self.command_args = command_args
        self.config = self._get_config()

    @property
    def acpi(self):
        return self.config.get('acpi')

    @property
    def kernel(self):
        return self.config['kernel']

    @property
    def initrd(self):
        return self.config['initrd']

    @property
    def cmdline(self):
        return self.config.get('cmdline')

    @property
    def mem(self):
        return self.config.get('mem', 1024)

    @property
    def cpus(self):
        return self.config.get('cpus', 1)

    @property
    def net(self):
        return '2:0,virtio-net'

    @property
    def cd(self):
        return self.config['cd']

    @property
    def img_cd(self):
        return '3,ahci-cd,{}'.format(self.cd)

    @property
    def hdd(self):
        return self.config['hdd']

    @property
    def img_hdd(self):
        return '4,virtio-blk,{}'.format(self.hdd)

    @property
    def uuid(self):
        return str(uuid.uuid4())

    @property
    def pci_dev(self):
        return '0:0,hostbridge -s 31,lpc'

    @property
    def lpc_dev(self):
        return 'com1,stdio'

    def _get_config(self):
        try:
            return util.safe_load_file(self.hyver_file)
        except IOError:
            msg = 'Unable to find {}.  Exiting.'.format(hyver_file())
            util.sysexit_with_message(msg)


def hyver_file():
    return HYVER_FILE
