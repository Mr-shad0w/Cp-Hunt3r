#!/usr/bin/env python

#Import Libraries d
import sys
import urllib
import urllib2
from sys import stdout
from platform import system as system_name
from os import system as system_call   

#We need this class to print Colored text!
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    command = "-cls" if system_name().lower()=="windows" else "clear"
    system_call(command)

def error(num):
    erdic = {1:"[!] Error (0x01): Invalid Argument", 2:"[!] Error (0x02): Invalid URL", 3:"[!] Error (0x03): Invalid Switch", 4:"[!] Error (0x04): Unknown Platform"}
    print bcolors.FAIL + erdic[num] + bcolors.ENDC
    print 'Here are some examples to use Cp-Hunt3r:'
    print './Cp-Hunt3r.py -h http://www.target.com'
    print './Cp-Hunt3r.py -i --version'

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def banner():
    clear_screen()
    banner= """                                             
 #####               #     #                      #####         
#     # #####        #     # #    # #    # ##### #     # #####  
#       #    #       #     # #    # ##   #   #         # #    # 
#       #    # ##### ####### #    # # #  #   #    #####  #    # 
#       #####        #     # #    # #  # #   #         # #####  
#     # #            #     # #    # #   ##   #   #     # #   #  
 #####  #            #     #  ####  #    #   #    #####  #    # 
--------------------------------------------------------------------- 
"""
    print banner
    print  bcolors.OKGREEN + '[*] Welcome to Cp-Hunt3r :)' + bcolors.ENDC


#check system args
if len(sys.argv) < 3:
    error(1)
    exit()

#check commands
if sys.argv[1] == '-h':
    target_utl = sys.argv[2]
    try:
        test = urllib.urlopen(target_utl)
    except:
        error(2)
        exit()
    
    banner()
    print bcolors.OKGREEN + '[*] URL Validated' + bcolors.ENDC
    print bcolors.OKGREEN + '[*] Scanning ' + target_utl + ' for admin page.....' + bcolors.ENDC
    req = urllib2.Request(target_utl)
    res = urllib2.urlopen(req)
    print bcolors.OKGREEN + str(res.info()) + bcolors.ENDC
    res.close();
    f = open('wordlist','r')
    leng = file_len('wordlist')
    for i in range(leng):
        temppage = f.readline()
        page_name = temppage.strip()
        page_name = '/' + page_name
        temptarget = target_utl + page_name
        print '[.] Scanned ' + str(i) + ' of ' + str(leng) + ' Pages' + '\r' ,
        stdout.flush()
        try:
            tester = urllib.urlopen(temptarget)
            if tester.code == 200:
                print '-------------------------------------------------------- '
                print bcolors.BOLD + 'Discovered admin page on: ' + temptarget + bcolors.ENDC
            else:
                pass
        except:
            pass

elif sys.argv[1] == '-i':
    print "Cp-Hunt3r.py Verison 1.1"
    
else:
    error(3)
    exit()
