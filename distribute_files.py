import os
import sys

import shutil

class copy_package(object):
    def __init__(self, srcroot, destroot, excl_list):
        self.srcroot = srcroot
        self.destroot = destroot
        self.excl_list = excl_list
        self.to_be_copied = {}

    def in_excl_list(self, f):
        if f in self.excl_list:
            return True
        if f.startswith(r'.'):
            return True
        return False

    def get_files_to_copy(self):
        os.chdir(self.srcroot)

        for root, dirs, files in os.walk("."):
            if self.in_excl_list(os.path.basename(root)) : continue
            print(root, os.path.relpath(root), dirs, files)
            self.to_be_copied[root] = files
        return self.to_be_copied

    def check_src_files(self):
        for k,v in self.to_be_copied.