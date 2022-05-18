#!/usr/bin/env python3
import shutil
import os

#force python to start in the home user directory
os.chdir('/home/student/mycode/')

#copy from raynor to ceph
shutil.move('raynor.obj', 'ceph_storage/')


xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

