#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "Scott Reese"

def pattern_check(files):
    pat = r'__(\w+)__'
    result = []
    for __file__ in files:
        match = re.search(pat, str(__file__))
        if match: result.append(__file__)
    return result

def stdout_files(from_dir): 
    for __file__ in pattern_check(os.listdir(from_dir)):
        print((os.path.abspath(__file__)))

def copy_files(path, from_dir):
    files = pattern_check(os.listdir(from_dir))
    if not os.path.exists(path):
        os.makedirs(path)
    for __file__ in files:
        shutil.copyfile(__file__, './' + str(path) + "/" + __file__)

def zip_files(path, from_dir):
    sys.tracebacklimit = 0
    try:
        files = pattern_check(os.listdir(from_dir))
        zip_cmd = "zip -j tmp.zip " + " ".join(files)
        os.system(zip_cmd)
    except OSError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        print("zip error: Could not create output file: ({0})".format(from_dir))

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', nargs='?', default='.', help='source dir of special files')

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    args = parser.parse_args()
    if args.todir:
        copy_files(args.todir, args.from_dir)
    elif args.tozip:
        zip_files(args.tozip, args.from_dir)
    else: stdout_files(args.from_dir)    
    


if __name__ == "__main__":
    main()
