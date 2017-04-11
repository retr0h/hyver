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

import click
import os
import sh

from hyver import config
from hyver import logger
from hyver import util

LOG = logger.get_logger(__name__)


class Create(object):
    def __init__(self, config):
        self._config = config
        self._cmd = None
        self._env = os.environ.copy()

    def bake(self):
        """
        Bake a `xyhve` command so it's ready to execute and returns
        None.

        :return: None
        """
        self._cmd = sh.xhyve.bake(
            self._get_cmd(),
            _cwd='../../vms/centos7/',
            _env=self._env,
            _out=LOG.out,
            _err=LOG.error, )

    def execute(self):
        """
        Execute the actions necessary to perform a `hyver create` and
        returns None.

        >>> hyver create

        Executing with `debug`:

        >>> hyver --debug create

        :return: None
        """
        msg = 'Creating instances'
        LOG.info(msg)

        if self._cmd is None:
            self.bake()

        try:
            with sh.contrib.sudo:
                util.run_command(
                    self._cmd, debug=self._config.args.get('debug'))
        except sh.ErrorReturnCode as e:
            util.sysexit(e.exit_code)

    def _get_cmd(self):
        c = self._config
        l = [
            c.acpi,
            '-m {}'.format(c.mem),
            '-c {}'.format(c.cpus),
            '-s {}'.format(c.pci_dev),
            '-l {}'.format(c.lpc_dev),
            '-s {}'.format(c.net),
            '-s {}'.format(c.img_cd),
            '-s {}'.format(c.img_hdd),
            '-f kexec,{},{},"{}"'.format(c.kernel, c.initrd, c.cmdline),
        ]
        return ([x for x in l if x is not None])


@click.command()
@click.pass_context
def create(ctx):  # pragma: no cover
    """ Start instances. """
    args = ctx.obj.get('args')
    command_args = {'subcommand': __name__}

    c = config.Config(config.hyver_file(), args, command_args)
    Create(c).execute()
