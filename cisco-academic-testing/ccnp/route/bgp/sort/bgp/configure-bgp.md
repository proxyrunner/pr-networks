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

The dotted line indicates configuration of external BGP, BGP timers, and MD5 authentication.

### Lets get started.

Start by configuring R2.

> R2(config)#router bgp 1
> R2(config-router)#neighbor 172.16.12.11 remote-as 100

Next we configure ISP_1

> ISP_1(config)#router bgp 100
> ISP_1(config-router)#neigh 172.16.12.2 remote-as 1

When the BGP session is finally established, you will see this output:

```
*Oct 22 14:45:03.583: %BGP-5-ADJCHANGE: neighbor 172.16.12.2 Up 
```

### Verification

> R2#sho ip bgp summary

```
BGP router identifier 10.0.0.2, local AS number 1
BGP table version is 1, main routing table version 1

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
172.16.12.11    4          100       4       4        1    0    0 00:00:12        0
```

> R2#show ip bgp neighbors 

```
BGP neighbor is 172.16.12.11,  remote AS 100, external link
  BGP version 4, remote router ID 10.0.1.1
  BGP state = Established, up for 00:00:33
  Last read 00:00:33, last write 00:00:33, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
```

#### Some example output when disabling a neighbor

```
R2(config-router)#neighbor 172.16.22.22 shutdown                       
*Oct 22 17:09:06.719: %BGP-5-ADJCHANGE: neighbor 172.16.22.22 Down Admin. shutdown
*Oct 22 17:09:06.719: %BGP_SESSION-5-ADJCHANGE: neighbor 172.16.22.22 IPv4 Unicast topology base removed from session  Admin. shutdown
R2(config-router)#no neighbor 172.16.22.22 shutdown
*Oct 22 17:10:21.211: %BGP-5-ADJCHANGE: neighbor 172.16.22.22 Up 
R2(config-router)#
```

## Configuring BGP Timers

Changing default holdtime and keepalive timers are typically not recommended. The defaults are:

* keepalive: 60 seconds
* holdtime: 180 seconds

These will work in most scenarios. If for any reason a faster BGP response to a peer down event is needed, the neighbor timers on the router can be reduced. Such as a scenario with multiple paths towards destinations are available.  The reduction will result ina faster detection of a lost peer and faster switching to the alternate path in the BGP table, improving convergence.

> router(config-router)# timers bgp keepalive holdtime

* Changes default values per BGP process
* Only holdtime value is communicated in BGP open message
* peers use the smallest configured holdtime value

> router(config-router)# neighbor ip-address timers keepalive holdtime

* changes default BGP timers per a specific neighbor
* overrides the BGP settings of timers

In this example we will configure R2's holdtime and keepalive where connected to ISP1

> R2(config-router)#neighbor 172.16.12.1 timers 10 30

> ISP_1(config-router)#timers bgp 10 30

#### Clear BGP Tables

```
ISP_1#clear ip bgp *
*Oct 22 17:28:00.571: %BGP-5-ADJCHANGE: neighbor 172.16.12.2 Down User reset
*Oct 22 17:28:00.571: %BGP_SESSION-5-ADJCHANGE: neighbor 172.16.12.2 IPv4 Unicast topology base removed from session  User reset
*Oct 22 17:28:01.499: %BGP-5-ADJCHANGE: neighbor 172.16.12.2 Up 
```

### Verification
```
R2#show ip bgp neighbors 
BGP neighbor is 172.16.12.1,  remote AS 100, external link
 Description: CONNECTION-TO-ISP-1
  BGP version 4, remote router ID 10.0.1.1
  BGP state = Established, up for 00:02:20
  Last read 00:00:03, last write 00:00:04, hold time is 30, keepalive interval is 10 seconds
  Configured hold time is 30, keepalive interval is 10 seconds
```

## MD5 Authentication

We will now configure MD5 authentication on a TCP connection. Here is the template configuration:

> router(config-router)# neighbor ip-address password string

* Enables MD5 authetication on a specific BGP session
* Password string on both routers must match

If they __do not__ match, you will receive the following output:

```
*Oct 22 17:37:43.987: %TCP-6-BADAUTH: Invalid MD5 digest from 172.16.12.2(39656) to 172.16.12.1(179) tableid - 0
```
