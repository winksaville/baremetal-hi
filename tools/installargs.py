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

import os

class InstallArgs:
    def __init__(self, app, defaultVer):
        parser = argparse.ArgumentParser()
        dflt=os.path.abspath('./' + app)
        parser.add_argument('--src',
                help='Source dir (default: {})'.format(dflt),
                nargs='?',
                default=dflt)
        dflt=os.path.abspath(os.environ['HOME'] + '/opt/')
        parser.add_argument('--prefix',
                help='Prefix for bin/ (default: {})'.format(dflt),
                nargs='?',
                default=dflt)
        dflt = defaultVer
        parser.add_argument('--ver',
                help='version to install (default: {})'.format(dflt),
                nargs='?',
                default=dflt);
        self.o = parser.parse_args()
