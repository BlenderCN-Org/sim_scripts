#!/usr/bin/env python
# Author: Benjamin Brieber

import subject
from xsens_data import xsens_header

import socket
import threading
import signal
import sys
#from struct import *

class mvn_listener():
#(Subject, threading.Thread):
    

    def __init__(self,output, ip='127.0.0.1',port=9763):
        #Subject.__init__(self)
        #threading.Thread.__init_(self)
        self._udp_ip = ip
        self._udp_port = port
        self._output = output
        self.count = 0


    def connect(self):
        print('binding socket')
        self._sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self._sock.bind((self._udp_ip,self._udp_port))
        print('done')

#    def run(self):
#

    def read_data(self):
        self.count = self.count + 1
        recv_data = self._sock.recv(4096)
        header = xsens_header(recv_data)
        if header.isQuaternion():
            if len(recv_data) != 760:
                print("wtf")
            self._output.write(recv_data)
        else:
            print("FATAL ERROR: this should never happen\n continue anyway :P")
        #print(self.count)
        #print(len(recv_data))
        #if len(recv_data) != 760:
        #    print('fuck')
        #    print(len(recv_data))

    def handle_quaternion(self,data):
        return

    def handle_euler(self,data):
        return

    def handle_pointData(self,data):
        return

    def handle_motionGridData(self,data):
        return

    def handle_scaleInfo(self,data):
        return

    def handle_propInfo(self,data):
        return

    def handle_metaData(self,data):
        return

    def handle_quaternion(self,data):
        return



    def clean_up(self):
        print("count: "+self.count)

running = 1


def main():
    with open("xsens.xcap",'wb') as output:
        client = mvn_listener(output=output, ip='192.168.100.212',port=9763)
        client.connect()
        while 1:
            client.read_data()
        client.clean_up()
    

#client.connect()
#  threads.append(client)
#  client.start()

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!\nterminating'
        running = 0
#        for t in threads:
#	  t.join()
#        sys.exit(0)

if __name__ == "__main__":
  #signal.signal(signal.SIGINT, signal_handler)
    try:
        main()
    except KeyboardInterrupt:
        running = 0
