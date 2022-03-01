import fullyproxy
from fullyproxy import*
import socket
import sys

import socketserver
import time
import logging


def start():
    FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(format=FORMAT, filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    print("Please enter ip address of proxy:")
    ipaddress = input()
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    fullyproxy.recordroute = recordroute
    fullyproxy.topvia = topvia
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    print("Proxy server started at <%s:%s>" % (ipaddress, PORT))
    server.serve_forever()
    pass


if __name__ == "__main__":
    start()




