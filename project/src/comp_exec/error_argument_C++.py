import subproces
import os
import sys

p = subprocess.Popen([r"/usr/bin/g++", "-Wall", "-o", "test", 'test.cpp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,error = p.communicate()

if p.returncode:
	raise Exception(error)
	print "Error>>>> ",p.returncode

else:
   print "Execution Success>>>> ",output
 
try:
    p = subprocess.Popen([r"/usr/bin/g++", "-Wall", "-o", "test", 'test.cpp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,error = p.communicate()
	if output:
        print "Execution Success>>>> ",output
    if error:
        print "Error > ",error.strip()

except CalledProcessError as e:
	print "CalledError > ",e.returncode
	print "CalledError > ",e.output

except OSError as e:
    print "OSError > ",e.errno
    print "OSError > ",e.strerror
    print "OSError > ",e.filename

except:
    print "Error > ",sys.exc_info()[0]