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

VER='1.6.0'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tmp', help='Temporary for source, default="."', nargs='?', default=os.path.abspath('.'));
    parser.add_argument('--prefix', help='Prefix for bin/', nargs='?', default=os.path.abspath(os.environ['HOME'] + '/opt/'))
    parser.add_argument('--ver', help='version to install', nargs='?', default=VER);
    args = parser.parse_args()

    dst_dir = os.path.abspath(args.prefix + '/bin')
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.abspath(dst_dir + '/ninja')

    try:
        output = subprocess.check_output([dst, '--version'])
        if output is None:
            output = ''
    except BaseException as err:
        output = ''

    if bytes(args.ver, 'utf-8') in output:
        print('ninja {} is already installed'.format(VER))
        exit(0)
    else:
        print('compiling ninja {}', VER)
        url = 'https://github.com/martine/ninja.git'
        os.makedirs(args.tmp, exist_ok=True)
        os.chdir(args.tmp)

        try:
            subprocess.check_call(['git', 'clone', url, '.'])
        except:
            print('Unable to git clone ninja', url)
            exit(1)

        try:
            subprocess.check_call(['./configure.py', '--bootstrap'])
        except:
            print('Unable to compile ninja')
            exit(1)

        dst = os.path.abspath(args.prefix + '/bin')
        os.makedirs(dst, exist_ok=True)
        dst = os.path.abspath(dst + '/ninja')
        try:
            shutil.copy2('./ninja', dst)
        except OSError as err:
            print('Unable to copy ninja to', dst)
            print('Error:', err);
            exit(1)
        exit(0)
