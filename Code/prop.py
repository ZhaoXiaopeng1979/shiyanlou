#!/usr/bin/env python3

def connect(ipaddress, *ports, **kw):
    print("IP: ", ipaddress)

    for port in ports:
        print("Port: ", port)
    
    for key, value in kw.items():
        print("{}: {}".format(key, value))

ipaddress = "192.168.1.1"
params = (25, 26, 27)
prop = {'device': 'eth0', 'proto': 'static'}

connect(ipaddress, *params, **prop)

