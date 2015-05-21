#process a filtered list of files by calling reapeatedly a 
#console app(no console opens) in two parallel threads with a timeout
#Antoni Gual May 2015

import os
import threading
import subprocess

def my_thread():
  global files,path,timeout,options
  myname= threading.currentThread().getName()
  while files:
     #create command to run
     nextfile=files.pop() 
     #print name of thread and command being run
     print('Thread {0} starts processing {1}'.format(myname,nextfile))
     f=path + nextfile + options
     try:
        #timeout interrupts frozen command, shell=True does'nt open a console
        subprocess.check_call(args= f , shell=True, timeout=timeout)
     except subprocess.TimeoutExpired:
        print('Thread {0} Processing {0} took too long' .format(myname,nextfile))
     except subprocess.CalledProcessError as e: 
        print ('Thread {0} Processing {1} returned error {2}:{3}'.format(myname,nextfile,e.returncode,e.output))
     except Exception as e:
        print ('Thread {0} Processing {1} returned error {2}'.format(myname,nextfile,type(e).__name__))
  print ('thread {0} stopped'.format(myname))
