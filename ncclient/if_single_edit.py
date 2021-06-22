#! /usr/bin/env python3
from ncclient import manager
from  lxml import etree
import datetime
import sys

if len(sys.argv) <2:
    print("usage: ",sys.argv[0],"running/candidate")
    sys.exit()
db=sys.argv[1]
host='1.1.1.1'
datetime=datetime.datetime.strftime(datetime.datetime.now(),'%y-%m-%d %H:%M:%S')
print("edit_config di:"+host)

config_if4='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
  
       <active>act</active>
    <interface-name>GigabitEthernet0/0/0/2.13</interface-name>
 <shutdown/>
    <description>Giga  edit by nccclient: data time (config_if3) '''+datetime+'''</description>
    <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
 <addresses>
 <primary>
 <address>8.9.9.9</address>
 <netmask>255.255.255.0</netmask>
 </primary>
 </addresses>
    </ipv4-network>
      </interface-configuration>
  </interface-configurations></config>
'''
with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c1=m.locked(target='candidate')
    c2=m.edit_config(target="candidate",config=config_if4,default_operation='merge')
    c3=m.validate()

    if db=="running":
        print(" edit in running")
        c4=m.commit()

print("edit candidate ",c2)
print("validate ",c3)
if db=="running":
    print("commit ",c4)
else:
    print("Not commited")

