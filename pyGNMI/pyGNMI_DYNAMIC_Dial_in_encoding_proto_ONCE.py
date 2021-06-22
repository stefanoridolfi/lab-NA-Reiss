#!/usr/bin/env python

## Subscription request

subscribe = {

                'subscription': [

                    {

                        'path': 'openconfig-interfaces:interfaces/interface[name=GigabitEthernet0/0/0/0]/state/counters/',

                        'mode': 'sample',

                        'sample_interval': 10000000000,

                        'heartbeat_interval': 30000000000

                    }

                ],

                'use_aliases': False,

                'mode': 'once',

                'encoding': 'proto'

            }


# Modules

from pygnmi.client import gNMIclient, telemetryParser

# Variables

host = ('1.1.1.1',57502)

# Body

if __name__ == '__main__':

    with gNMIclient(target=host, username='admin', password='admin', insecure=True) as gc:

        response = gc.subscribe(subscribe=subscribe)
        for telemetry_entry in response:
            res=telemetryParser(telemetry_entry)
            print(res)
