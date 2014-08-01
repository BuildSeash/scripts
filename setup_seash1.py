
"""
# !/usr/bin/python

<Program>
  setup_seash.py 
  
<Date Started>
  July 5th, 2014

<Author>
  Chintan Choksi

<Purpose>
  This script does a git check-out of all the dependent repositories of Seash to the home directory.
  
<Usage>
  How to run this program:
  1. Clone the seash repository to local machine, and run this script
  2. Run this script: 
  seash user$ python setup_seash.py
   
"""


import commands
import subprocess
import os
import sys

"""
==========================================================================================
if not os.path.exists('target/'):
    os.makedirs('target/')
   
I have kept this in comment as it's still to be decided whether to create a new target 
folder or check-out the repositories in current working directories
==========================================================================================
"""    

"""
def find_command(cmd, paths=None, pathext=None):
    Searches the PATH for the given command and returns its path
    if paths is None:
        paths = os.environ.get('PATH', '').split(os.pathsep)
    if isinstance(paths, six.string_types):
        paths = [paths]
    # check if there are funny path extensions for executables, e.g. Windows
    if pathext is None:
        pathext = get_pathext()
    pathext = [ext for ext in pathext.lower().split(os.pathsep) if len(ext)]
    # don't use extensions if the command ends with one of them
    if os.path.splitext(cmd)[1].lower() in pathext:
        pathext = ['']
    # check if we find the command on PATH
    for path in paths:
        # try without extension first
        cmd_path = os.path.join(path, cmd)
        for ext in pathext:
            # then including the extension
            cmd_path_ext = cmd_path + ext
            if os.path.isfile(cmd_path_ext):
                return cmd_path_ext
        if os.path.isfile(cmd_path):
            return cmd_path
    raise BadCommand('Cannot find command %r' % cmd)




find_command("git")
"""

file = open('file1.txt', 'r')
line = file.readline().rstrip('\n')
#"line".rstrip()
#line1 = "git clone https://github.com/SeattleTestbed/seattlelib_v2"
#print line
#print line1

pr = subprocess.Popen( line , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr.communicate()
print str("Checking out seattlelib_v2")

line = file.readline().rstrip('\n')
#print line
pr1 = subprocess.Popen( line , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr1.communicate()
print str("Checking out clearinghouse")

line = file.readline().rstrip('\n')
pr2 = subprocess.Popen( line , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr2.communicate()
print str("Checking out portability")

line = file.readline().rstrip('\n')
pr3 = subprocess.Popen( line , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr3.communicate()
print str("Checking out repy_v2")

line = file.readline().rstrip('\n')
pr4 = subprocess.Popen( line , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr4.communicate()
print str("Checking out repy_v1")

line = file.readline().rstrip('\n')
pr5 = subprocess.Popen( line , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr5.communicate()
print str("Checking out dist")



