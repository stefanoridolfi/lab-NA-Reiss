#! /usr/bin/env python3
from ncclient import manager
import sys

db='running'
host='1.1.1.1'
interface='GigabitEthernet0/0/0/2.1'

if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
   <interface-name>'''+interface+'''</interface-name>
   </interface-configuration>
   </interface-configurations>
                                '''


with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c2=m.get_config(source=db, filter=('subtree', if_filter))
print(c2)
