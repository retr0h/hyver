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

import sys

import colorama
import ruamel.yaml

from hyver import logger

LOG = logger.get_logger(__name__)


def safe_dump(data, f=None):
    """
    Dump the provided data to a YAML document and returns a string.

    :param data: A dict containing the data to dump.
    :param f: A file-like object to operate on.
    :return: str
    """
    return ruamel.yaml.safe_dump(
        data,
        default_flow_style=False,
        default_style=None,
        explicit_start=True)


def safe_load(stream):
    """
    Parse the provided string returns a dict.

    :param stream: A string to be parsed.
    :return: dict
    """
    return ruamel.yaml.safe_load(stream) or {}


def safe_load_file(filename):
    """
    Parse the provided YAML file and returns a dict.

    :param filename: A string containing an absolute path to the file to parse.
    :return: dict
    """
    with open(filename, 'r') as stream:
        return safe_load(stream)


def write_file(filename, content):
    """
      Writes a file with the given filename and content and returns None.

      :param filename: A string containing the target filename.
      :param content: A string containing the data to be written.
      :return: None
      """
    with open(filename, 'w') as f:
        f.write(content)


def run_command(cmd, debug=False):
    """
    Execute the given command and returns None.
    :param cmd: A `sh.Command` object to execute.
    :param debug: An optional bool to toggle debug output.
    :return: ``sh`` object
    """
    if debug:
        print_debug('COMMAND', str(cmd))
    return cmd()


def sysexit(code=1):
    sys.exit(code)


def sysexit_with_message(msg, code=1):
    LOG.critical(msg)
    sysexit(code)


def print_debug(title, data):
    print(''.join([
        colorama.Back.WHITE, colorama.Style.BRIGHT, colorama.Fore.BLACK,
        'DEBUG: ' + title, colorama.Fore.RESET, colorama.Back.RESET,
        colorama.Style.RESET_ALL
    ]))
    print(''.join([
        colorama.Fore.BLACK, colorama.Style.BRIGHT, data,
        colorama.Style.RESET_ALL, colorama.Fore.RESET
    ]))
