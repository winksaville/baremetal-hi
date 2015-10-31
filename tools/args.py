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

def installargs(defaultVer):
    __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--tmp',
                help='Temporary for source, default="."',
                nargs='?',
                default=os.path.abspath('.'));
        parser.add_argument('--prefix',
                help='Prefix for bin/',
                nargs='?',
                default=os.path.abspath(os.environ['HOME'] + '/opt/'))
        parser.add_argument('--ver',
                help='version to install',nargs='?',
                default=VER);
        o = parser.parse_args()
