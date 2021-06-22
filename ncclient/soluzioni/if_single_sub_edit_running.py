#! /usr/bin/env python3
from ncclient import manager
host='1.1.1.1'
config_if='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
         <active>act</active>
    <interface-name>GigabitEthernet0/0/0/2.1</interface-name>
        <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
 <addresses>
 <primary>
 <address>1.2.3.11</address>
 <netmask>255.255.255.0</netmask>
 </primary>
 </addresses>
    </ipv4-network>
      </interface-configuration>
  </interface-configurations></config>
'''
with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
  #  c1=m.locked(target='candidate')
    c2=m.edit_config(target="candidate",config=config_if,default_operation='merge')
    c3=m.validate()
    c4=m.commit()
print("result:  ",c4)

