#!/usr/bin/python

import socket
import concurrent.futures


TIMEOUT = 2.0  # You can change the duratoin 

def isHTTPsAlive(childId, host):

    try:
        isHTTP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        isHTTP.settimeout(TIMEOUT)
        isHTTPS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        isHTTPS.settimeout(TIMEOUT)
        http = isHTTP.connect_ex((host, 80)) == 0
        https = isHTTPS.connect_ex((host, 443)) == 0
        isHTTP.close()
        isHTTPS.close()
        
    except:
        (http, https) = (False, False)
    if http or https:
        print (host)
    else:
        pass


if __name__ == '__main__':
    hostFile = str(input('List of Hosts [ex: hosts.txt] : '))
    threads = int(input('Threads [ex: 30] : '))
    Hosts = open(hostFile, 'r').read().splitlines()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as \
        pool_executor:
        for host in Hosts:
            pool_executor.submit(isHTTPsAlive, 0, host)
