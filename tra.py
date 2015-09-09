#!/usr/bin/env python
import multiprocessing
import subprocess
import os,sys,re
print (sys.getdefaultencoding())
INPUT_IP = os.path.join(os.getcwd(),"IP.txt")
OUTPUT_IP = os.path.join(os.getcwd(),"RESULT.txt")
INPUT_IP_LINES = sum(1 for line in open(INPUT_IP))

OPEN_INPUT_IP = open(INPUT_IP)
OPEN_OUTPUT_RESULT = open(OUTPUT_IP,'w')

if INPUT_IP_LINES > 30:
    process_number = 30
else:
    process_number = INPUT_IP_LINES
global hh
def TRACERT_HOST(ipaddr):
        PROC = subprocess.Popen('traceroute -d -w 1 %s' % ipaddr,
                        stdin = subprocess.PIPE,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        shell = True)
        PROC = PROC.stdout.read()
        if re.search("30\.250\.1",PROC) != None:
                print ('%s tracker is OK' % ipaddr)
                hh += '%s tracker is OK' % ipaddr
                print hh
        else:
                print ('%s tracker is FAIL' % ipaddr)
                hh += '%s tracker is FAIL' % ipaddr
                print hh
if __name__ == "__main__":
        pool = multiprocessing.Pool(processes=process_number)
        for IP in OPEN_INPUT_IP.readlines():
                IP = IP.strip('\n')
                pool.apply_async(TRACERT_HOST,(IP,))
        pool.close()
        pool.join()

