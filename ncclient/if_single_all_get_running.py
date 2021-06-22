#! /usr/bin/env python3
from ncclient import manager
from  lxml import etree
host='1.1.1.1'
interface='GigabitEthernet0/0/0/0'
all_if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
      </interface-configuration>
   </interface-configurations> '''

with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c2=m.get_config(source='running', filter=('subtree', all_if_filter))
print(c2)
