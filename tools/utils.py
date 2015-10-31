#!/usr/bin/env python3

# Copyright 2015 wink saville
#
# licensed under the apache license, version 2.0 (the "license");
# you may not use this file except in compliance with the license.
# you may obtain a copy of the license at
#
#     http://www.apache.org/licenses/license-2.0
#
# unless required by applicable law or agreed to in writing, software
# distributed under the license is distributed on an "as is" basis,
# without warranties or conditions of any kind, either express or implied.
# see the license for the specific language governing permissions and
# limitations under the license.

import subprocess

def git(cmd, params):
    try:
        if cmd is None:
            return
        cmds = ['git', cmd]
        if not params is None:
            cmds.extend(params)
        subprocess.check_call(cmds)
    except BaseException as ex:
        print('Exception: {}'.format(ex))
        exit(1)

def bash(cmd):
    try:
        if cmd is None:
            return
        subprocess.check_call(['bash', '-c', cmd])
    except BaseException as ex:
        print('Exception: {}'.format(ex))
        exit(1)

def bashPython2(cmd):
    bash('[ ! -d venv2 ] && virtualenv --python=python2 venv2; ' +
         'source venv2/bin/activate;' +
         cmd)

