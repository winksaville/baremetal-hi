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
import shutil
import multiprocessing

VER='2.25.1'
APP='binutils-gdb'
PREFIX='opt/cross'
AN_APP='ld'
TARGET='arm-eabi'
TARGET_DASH='-'


if __name__ == '__main__':

    args = installargs.InstallArgs(APP, VER, PREFIX)

    dst_dir = os.path.abspath(args.o.prefix)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.abspath(dst_dir + '/bin/{target}{target_dash}{an_app}'
            .format(target=TARGET, target_dash=TARGET_DASH, an_app=AN_APP))

    try:
        output = subprocess.check_output([dst, '--version'])
        if output is None:
            output = b''
    except BaseException as err:
        output = b''

    if bytes(args.o.ver, 'utf-8') in output:
        print('{app} {ver} is already installed'.format(app=APP, ver=VER))
        exit(0)
    else:
        print('compiling {app} {ver}'.format(app=APP, ver=VER))
        os.makedirs(args.o.src, exist_ok=True)

        try:
            url = 'git://sourceware.org/git/binutils-gdb.git'
            utils.git('clone', [url, args.o.src])
            os.chdir(args.o.src)
            version = VER.replace('.','_')
            utils.git('checkout', ['binutils-{ver}'.format(ver=version)])
            os.mkdir('build')
            os.chdir('build')
        except BaseException as ex:
            print(sys.exc_info()[0])
            print('Unable to get {app} Exception: {ex}'.format(app=APP, ex=ex))
            exit(1)

        print('configure')
        utils.bash('../configure --prefix={0} --target={1} --disable-nls'
                .format(args.o.prefix, TARGET))
        utils.bash('make all -j {}'.format(1))
        utils.bash('make install')

        exit(0)
