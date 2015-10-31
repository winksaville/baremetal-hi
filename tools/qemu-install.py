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

VER='2.4.0.1'
APP='qemu-system-arm'


if __name__ == '__main__':

    args = installargs.InstallArgs(APP, VER)

    dst_dir = os.path.abspath(args.o.prefix)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.abspath(dst_dir + '/bin/{app}'.format(app=APP))

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
            url = 'git://git.qemu.org/qemu.git'
            utils.git('clone', [url, args.o.src])
            os.chdir(args.o.src)
            utils.git('checkout', ['v{ver}'.format(ver=VER)])
            utils.git('submodule', ['update', '--init', 'dtc'])
            os.mkdir('build')
            os.chdir('build')
        except BaseException as ex:
            print(sys.exc_info()[0])
            print('Unable to get {app} Exception: {ex}'.format(app=APP, ex=ex))
            exit(1)

        print('configure')
        utils.bashPython2(
                '../configure --prefix={} --target-list=arm-softmmu,arm-linux-user'
                .format(args.o.prefix))
        utils.bashPython2('make -j {}'.format(multiprocessing.cpu_count()))
        utils.bashPython2('make install')

        exit(0)
