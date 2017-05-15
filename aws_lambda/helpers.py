# -*- coding: utf-8 -*-
import os
import shutil


def read(path, loader=None):
    with open(path) as fh:
        if not loader:
            return fh.read()
        return loader(fh.read())


def custom_copytree(src, dst, minimal, symlinks=False, ignore=None):
    for item in os.listdir(src):
        if (minimal and item == 'event.json') or item.endswith('.pyc') or item == '__pycache__':
            continue
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy(s, d)
