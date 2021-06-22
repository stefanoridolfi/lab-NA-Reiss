#!/usr/bin/python3
import os
import re
print("nome del file: "+__file__)

from ncclient import manager
from  lxml import etree
import  xml.etree.ElementTree as ET
import xmltodict
host='2.2.2.2'
#filter = "native/hostname"
#filter = "native/counters"
#filter = "interfaces/interface"
filter = "interfaces/interface[name='GigabitEthernet1']"
#filter = "interfaces/interface[name='GigabitEthernet1']/description"

print("get_config di:"+host)

with manager.connect(host=host, port=830, username='cisco', password='cisco',hostkey_verify=False,device_params={'name':'csr'}) as m:
    c2=m.get_config(source='running', filter=('xpath', filter))
c2_data=c2.data_xml

print("c2_data\n",c2_data)
