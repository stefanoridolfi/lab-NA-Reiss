#! /usr/bin/env python3
host='1.1.1.1'
from ncclient import manager
with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m2:
    c2=m2.server_capabilities
for elem in c2:
    print(elem)
