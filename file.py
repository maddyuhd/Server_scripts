import sys
import os


def readtxt(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def readfolder(src_path):
    name = sorted(os.listdir(src_path))
    return name
