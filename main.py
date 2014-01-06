#!/usr/bin/env python
import BaseHTTPServer
import os
import shutil
import sys
import ntpath
import socket
import argparse
from urlparse import urlparse
import threading
import time
import signal
import urllib




class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
   
    def do_GET(self):
        global downloads
        downloads = downloads+1
        query = urlparse(self.path)
        password = query.path
        if(args['password']):
            if args['password'] != password[1:]:
                return False
        #query_components = dict(qc.split("=") for qc in query.split("&"))
        
        with open(args['file'], 'rb') as f:
            name  =  ntpath.basename(args['file'])
            self.send_response(200)
            self.send_header("Content-Type", 'application/octet-stream')
            self.send_header("Content-Disposition", 'attachment; filename="'+name+'"')
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs.st_size))
            self.end_headers()
            shutil.copyfileobj(f, self.wfile)


def signal_handler(signal, frame):
    print 7777   
            
    
def gg(httpd):
    
    while True:
        #time.sleep(100)
        if(args['downloads'] != -1 and downloads >=  args['downloads']):
            break
        if(interrupted):
            break    
        httpd.handle_request()
                       
        
def create_dummy_request(url):
    urllib.urlopen("http://"+url)
        
def start_file_server(HandlerClass=SimpleHTTPRequestHandler,
         ServerClass=BaseHTTPServer.HTTPServer,
         protocol="HTTP/1.0"):
    
    global httpd
    global interrupted
    interrupted = False
    port = args['port']
    server_address = ('', port)

    HandlerClass.protocol_version = protocol
    httpd = BaseHTTPServer.HTTPServer(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    ip = get_lan_ip()
    print "Serving HTTP on", ip, "port", sa[1], "...", args['file']
    link = str(ip)+":"+str(port)+"/"+args['password']
    print "Please open     ",link,"            in your browser to download ",args['file'] ,'file'
    background_thread = threading.Thread(target=gg,args=(httpd,))
    background_thread.start()
    #signal.signal(signal.SIGINT, signal_handler)
    while True:
        if(args['downloads'] != -1 and downloads >=  args['downloads']):
            break
        try:
            time.sleep(1)
        except:
            print 55 
            interrupted = True
            create_dummy_request(link)
            break   
        
           
        

    
    
if os.name != "nt":

    import fcntl

    import struct

    def get_interface_ip(ifname):

    	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    	return socket.inet_ntoa(fcntl.ioctl(

    			s.fileno(),

    			0x8915,  # SIOCGIFADDR

    			struct.pack('256s', ifname[:15])

    		)[20:24])



def get_lan_ip():

    ip = socket.gethostbyname(socket.gethostname())

    if ip.startswith("127.") and os.name != "nt":

    	interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]

    	for ifname in interfaces:

    		try:

    			ip = get_interface_ip(ifname)

    			break;

    		except IOError:

    			pass

    return ip

def parse_arguments():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='--port pass required port numper as arguiment default port is 8000',default=8000,type=int)
    parser.add_argument('--downloads', help='--downloads used to restrict number of downloads',default=-1,type=int)
    parser.add_argument('--file', help='-- pass path to file here to make downlodable in you network', default='')
    parser.add_argument('--password', help='-- enter password to protect files from anothorized download', default='')
    args = parser.parse_args()
    args = vars(args)
def check_file(fname):
    return os.path.isfile(fname)
def main():
    parse_arguments()
    if not check_file(args['file']):
        print args['file'],'not found'
        sys.exit()

    start_file_server()
if __name__ == '__main__':
    global args
    global downloads
    global httpd
    global interrupted

    downloads = 0
    main()
    
