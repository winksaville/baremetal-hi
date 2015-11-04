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

import utils
import installargs

import subprocess
import sys
import os
import traceback
import shutil

VER='1.6.0'
APP='ninja'
PREFIX='opt'

if __name__ == '__main__':

    args = installargs.InstallArgs(APP, VER, PREFIX)

    dst_dir = os.path.abspath(args.o.prefix + '/bin')
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.abspath(dst_dir + '/{app}'.format(app=APP))

    try:
        output = subprocess.check_output([dst, '--version'])
        if output is None:
            output = b''
    except BaseException as err:
        output = b''

    if bytes(args.o.ver, 'utf-8') in output:
        print('{app} {ver} is already installed'.format(app=APP, ver=args.o.ver))
        exit(0)
    else:
        print('compiling {app} {ver}'.format(app=APP, ver=args.o.ver))
        url = 'https://github.com/martine/ninja.git'
        os.makedirs(args.o.src, exist_ok=True)

        utils.git('clone', [url, args.o.src])
        os.chdir(args.o.src)

        try:
            subprocess.check_call(['./configure.py', '--bootstrap'])
        except:
            traceback.print_exc()
            exit(1)

        dst = os.path.abspath(args.o.prefix + '/bin')
        os.makedirs(dst, exist_ok=True)
        dst = os.path.abspath(dst + '/{app}'.format(app=APP))
        try:
            shutil.copy2('./{app}'.format(app=APP), dst)
        except OSError as err:
            traceback.print_exc()
            exit(1)
        exit(0)
