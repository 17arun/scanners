#!/usr/bin/python3

import socket
from IPy import IP
import optparse
import threading
from array import *
from IPy import IP
from datetime import datetime

def portscan(tar,port):
    try:
        ip = checker(tar)
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ip, port))
        try:
            serv = socket.getservbyport(port)
            print(port,"\topen\t",serv)
        except:
            print(port,"\topen\tUnknown service!!")
    except:
        pass



#this is to checker is in ip or domain name
def checker(target):
    try:
        IP(target)
        return (target)
    except ValueError:
        return socket.gethostbyname(target)

def main():
    try:
         parser = optparse.OptionParser( 'Usage of program: '+ '-H <target host> \n EAMPLE : ./portscan.py -H 8.8.8.8  \n \t./portscan.py -H google.com ')
         parser.add_option('-H', dest='tgtHost', type='string', help= 'specify target host')
         (options, args) = parser.parse_args()
         tgtHost = options.tgtHost

         #this is for display options
         if (tgtHost) == None :
                print(parser.usage)
                exit(0)

         # Add Banner
         print("-" * 50)
         print("Scanning Target: " + socket.gethostbyname(tgtHost))
         print("Scanning started at:" + str(datetime.now()))
         print("-" * 50)
         print("""PORT\tSTATE\tSERVICE""")

         for port in range(0,1024):
             t= threading.Thread(target=portscan, args=(tgtHost,int(port)))
             t.start()

    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        exit(0)
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        exit(0)
    except socket.error:
        print("\ Server not responding !!!!")
        exit(0)


if __name__ == '__main__':
    main()