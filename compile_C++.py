from subprocess import *
p = subprocess.Popen([r"/usr/bin/g++", "-Wall", "-o", "test", 'test.cpp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate()
p = subprocess.Popen(["./test"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate()