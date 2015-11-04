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
import multiprocessing

VER='5.2.0'
CHECKOUT_LABEL='gcc_{}_release'.format(VER.replace('.','_'))
#GCC_GIT_REPO_URL = 'https://github.com/gcc-mirror/gcc.git'
GCC_GIT_REPO_URL = 'https://github.com/winksaville/gcc-5.2.0.git'
GCC_URL = 'http://ftp.gnu.org/gnu/gcc/gcc-{0}/gcc-{0}.tar.bz2'
GMP_URL = 'https://gmplib.org/download/gmp/gmp-6.0.0a.tar.xz'
MPFR_URL = 'http://www.mpfr.org/mpfr-current/mpfr-3.1.3.tar.xz'
MPC_URL = 'ftp://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz'
APP='gcc'
AN_APP='gcc'
PREFIX='opt/cross'
TARGET='arm-eabi'
TARGET_DASH='-'


if __name__ == '__main__':

    args = installargs.InstallArgs(APP, VER, PREFIX)

    dst_dir = os.path.abspath(args.o.prefix)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.abspath(dst_dir + '/bin/{target}{target_dash}{an_app}'
            .format(target=TARGET, target_dash=TARGET_DASH, an_app=AN_APP))
    print('gcc-install: dst=', dst)
    print('gcc-install: args.o.src=', args.o.src)
    print('gcc-install: args.o.ver=', args.o.ver)
    print('gcc-install: args.o.prefix=', args.o.prefix)

    try:
        output = subprocess.check_output([dst, '--version'])
        if output is None:
            output = b''
    except BaseException as err:
        output = b''

    if False: #bytes(args.o.ver, 'utf-8') in output:
        print('gcc-install: {app} {ver} is already installed'.format(app=APP, ver=args.o.ver))
        exit(0)
    else:
        print('gcc-install:  compiling {app} {ver}'.format(app=APP, ver=args.o.ver))

        gmp_path = os.path.join(os.path.dirname(args.o.src), 'gmp')
        print('gcc-install: gmp_path=', gmp_path)
        mpfr_path = os.path.join(os.path.dirname(args.o.src), 'mpfr')
        print('gcc-install: mpfr_path=', mpfr_path)
        mpc_path = os.path.join(os.path.dirname(args.o.src), 'mpc')
        print('gcc-install: mpc_path=', mpc_path)

        try:
            utils.wget_extract(GMP_URL, dst_path=gmp_path)
            utils.wget_extract(MPFR_URL, dst_path=mpfr_path)
            utils.wget_extract(MPC_URL, dst_path=mpc_path)
            #utils.wget_extract(GCC_URL.format(args.o.ver), dst_path=args.o.src)
            os.makedirs(args.o.src, exist_ok=True)
            utils.git('clone', [GCC_GIT_REPO_URL, args.o.src])
            os.chdir(args.o.src)
            #utils.git('checkout', [CHECKOUT_LABEL])
            os.mkdir('build')
            os.chdir('build')
        except BaseException as ex:
            traceback.print_exc()
            exit(1)

        #Seeing if installing the gmp, mpfr and mpc packages workes
        #utils.bash('cd {0} && ./configure'.format(gmp_path))
        #utils.bash(('cd {0} && ./configure' +
        #            ' --with-gmp-include={gmp}' +
        #            ' --with-gmp-lib={gmp} && make').format(mpfr_path, gmp=gmp_path))
        #utils.bash(('cd {0} && ./configure' +
        #            ' --with-gmp-include={gmp}' +
        #            ' --with-gmp-lib={gmp} && make').format(mpc_path, gmp=gmp_path))
        utils.bash('ls -al {}'.format(os.path.dirname(args.o.src)))
        print('gcc-install: configure')
        utils.bash(('../configure --prefix={0} --target={1}' +
               ' --with-gmp={gmp}' +
               ' --with-gmp-include={gmp}' +
               ' --with-mpfr={mpfr}' +
               ' --with-mpfr-include={mpfr}/src' +
               ' --with-mpc={mpc}' +
               ' --with-mpc-include={mpc}/src' +
               ' --disable-nls ' +
               ' --enable-languages=c,c++' +
               ' --without-headers')
                .format(args.o.prefix, TARGET, gmp=gmp_path, mpfr=mpfr_path, mpc=mpc_path))
        # Set stdout to DEVNULL so the travis log file doesn't grow beyond 4MB. locally
        # the log file become 5.4MB and travis-ci aborts if its > 4MB.
        try:
            print('gcc-install: make all-gcc')
            subprocess.run('make all-gcc -j {}'.format(multiprocessing.cpu_count()),
                    shell=True,
                    stdout=subprocess.DEVNULL)
            print('gcc-install: make all-gcc DONE')
        except:
            traceback.print_exc()
            exit(1)
        #utils.bash('make all-gcc -j {}'.format(multiprocessing.cpu_count()))

        utils.bash('make install-gcc')
        utils.bash('make all-target-libgcc')
        utils.bash('make install-target-libgcc')

        exit(0)
