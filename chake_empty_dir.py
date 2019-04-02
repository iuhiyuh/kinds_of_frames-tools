# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import subprocess

if __name__ == '__main__':
    root_path = sys.argv[1]
    remove = sys.argv[2]

    try:
        os.path.exists(root_path)
    except:
        print("目录不存在")
    for class_name in os.listdir(root_path):
        class_path = os.path.join(root_path, class_name)
        for file_name in os.listdir(class_path):
            file_name_path = os.path.join(class_path, file_name)
            if not os.listdir(file_name_path):
                print("空目录为: {}".format(file_name_path))
            try:
                if remove == 1 or remove == True:
                    cmd = "rm -rf {}".format(file_name_path)
                    subprocess.call(cmd, shell=True)
                elif remove == 0 or remove == False:
                    print("已列出所有")
            except:
                print("python chake_empty_file \"files root path\" 1(or 0)")
            pass
