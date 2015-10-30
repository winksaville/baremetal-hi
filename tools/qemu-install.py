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

import argparse
import subprocess
import sys
import os
import shutil
import multiprocessing

VER='2.4.0.1'
APP='qemu-system-arm'

def git(cmd, params):
    try:
        cmds = ['git', cmd]
        cmds.extend(params)
        subprocess.check_call(cmds)
    except BaseException as ex:
        print('Exception: {}'.format(ex))
        exit(1)

def bash(cmd):
    try:
        subprocess.check_call(['bash', '-c', cmd])
    except BaseException as ex:
        print('Exception: {}'.format(ex))
        exit(1)

def bashPython2(cmd):
    bash('virtualenv --python=python2.7 venv; . venv/bin/activate ; {}'.format(cmd))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tmp', help='Temporary for source, default="."', nargs='?', default=os.path.abspath('.'));
    parser.add_argument('--prefix', help='Prefix for bin/', nargs='?', default=os.path.abspath(os.environ['HOME'] + '/opt/'))
    parser.add_argument('--ver', help='version to install', nargs='?', default=VER);
    args = parser.parse_args()

    dst_dir = os.path.abspath(args.prefix)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.abspath(dst_dir + '/bin/{}'.format(APP))

    try:
        output = subprocess.check_output([dst, '--version'])
        if output is None:
            output = b''
    except BaseException as err:
        output = b''

    if bytes(args.ver, 'utf-8') in output:
        print('{app} {ver} is already installed'.format(app=APP, ver=VER))
        exit(0)
    else:
        print('compiling {app} {ver}'.format(app=APP, ver=VER))
        os.makedirs(args.tmp, exist_ok=True)
        os.chdir(args.tmp)

        try:
            url = 'git://git.qemu.org/qemu.git'
            git('clone', [url, '.'])
            git('checkout', ['v{ver}'.format(ver=VER)])
            git('submodule', ['update', '--init', 'dtc'])
            os.mkdir('build')
            os.chdir('build')
        except BaseException as ex:
            print(sys.exc_info()[0])
            print('Unable to get {app} Exception: {ex}'.format(app=APP, ex=ex))
            exit(1)

        bashPython2('../configure --prefix={} --target-list=arm-softmmu,arm-linux-user'.format(args.prefix))
        bashPython2('make -j {}'.format(multiprocessing.cpu_count()))
        bashPython2('make install')

        exit(0)
