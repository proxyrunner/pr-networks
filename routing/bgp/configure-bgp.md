# BGP Routing Process

## Introductions

> (config)# __router bgp__ _as-number_

* Start BGP Routing
* Get you AS number from American Registry for Internet Numbers or Réseaux IP Européens.
* Use private AS numbers (between 64,512 and 65,534 or between 4,200,000,000 and 4,294,967,294) if you run BGP in a private network.
* Only one BGP routing process per router is allowed.

The AS number is a 16-bit or 32-bit integer. New 32-bit AS numbers were created when the AS number pool from the IANA approached exhaustion. The AS number pool was extended from 16 to 32 bits. It must uniquely identify the AS among all routers that are exchanging BGP routing information, either directly or indirectly. This requirement means that the AS numbers must be unique when BGP information is exchanged with the Internet.

The AS number can be public or private. Public AS numbers range from 1 to 64,511 or 131,072 to 4,199,999,999. An Internet registry (ARIN: http://www.arin.net or RIPE: http://www.ripe.net) assigns public AS numbers. Private AS numbers range from 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. Private AS numbers are never propagated onto the public Internet.

## Configuring External Neighbors

Defines an external neighbor:

> (config-router)# neighbor _ip\_address_ remote-as _as-number_

Assigns a description to an external neighbor:

> (config-router)# neighbor _ip\_address_ description _neighbor description_

Disables a BGP Neighbor:

> (config-router)# neighbor _ip\_address_ shutdown

## Configure Basic BGP

![AS-BUILT1](https://github.com/gil-ryan/grs-networking-public/blob/master/img/as-built1.png)

Test
