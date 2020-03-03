#!/usr/bin/env python3

import gevent
from gevent.subprocess import PIPE,Popen,spawn
import time
from dataclasses import dataclass

@dataclass
class BluetoothObject:
    addr: str
    rssi: int
    cnt: int


result = {} 

def read_proc(stream):
    while not stream.closed:
        l = stream.readline().rstrip()
        data = l.decode('ascii').split('|')
        addr = data[0]
        key = addr
        val = int(data[1])
        if key in result:
            result[key].rssi = val
            result[key].cnt+=1
        else:
            obj = BluetoothObject(addr=addr,rssi=val,cnt=1)
            result[addr] = obj
        print("\r",end='')
        for k in result:
            obj = result[k]
            print("%s %s(%s)   " % (k,obj.rssi,obj.cnt),end='')

def run():
    proc = Popen('bt-rssi',stdout=PIPE,shell=False)
    spawn(read_proc,proc.stdout)
    proc.wait()

if __name__ == '__main__':
    spawn(run)
    try:
        while 1:
            gevent.sleep(1)
    except KeyboardInterrupt:
        print("\nBye")
