#!/usr/bin/env python

## Subscription request

subscribe = {

                'subscription': [

                    {

                        'path': 'Cisco-IOS-XR-infra-statsd-oper:infra-statistics/interfaces/interface[interface-name=GigabitEthernet0/0/0/2]/latest/generic-counters',

                        'mode': 'sample',

                        'sample_interval': 10000000000,

                        'heartbeat_interval': 30000000000

                    }

                ],

                'use_aliases': False,

                'mode': 'stream',

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

#            print("telemetry_entry raw",telemetry_entry)
            print(telemetryParser(telemetry_entry))
