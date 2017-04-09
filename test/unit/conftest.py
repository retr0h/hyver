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

import os
import random
import shutil
import string

import pytest

from hyver import config


@pytest.fixture
def random_string(l=5):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(l))


@pytest.fixture
def temp_dir(tmpdir, random_string, request):
    directory = tmpdir.mkdir(random_string)
    os.chdir(directory.strpath)

    def cleanup():
        shutil.rmtree(directory.strpath)

    request.addfinalizer(cleanup)

    return directory


@pytest.fixture
def hyver_file():
    return os.path.join(os.path.dirname(__file__), 'resources', 'hyver.yml')


@pytest.fixture
def config_instance(hyver_file):
    return config.Config(hyver_file)


@pytest.fixture
def patched_logger_info(mocker):
    return mocker.patch('logging.Logger.info')


@pytest.fixture
def patched_logger_warn(mocker):
    return mocker.patch('logging.Logger.warn')


@pytest.fixture
def patched_logger_error(mocker):
    return mocker.patch('logging.Logger.error')


@pytest.fixture
def patched_logger_critical(mocker):
    return mocker.patch('logging.Logger.critical')


@pytest.fixture
def patched_print_debug(mocker):
    return mocker.patch('hyver.util.print_debug')
