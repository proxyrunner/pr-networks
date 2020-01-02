# OSPF Router-ID & MTU Mismatch

Every router has a router-ID, and each should be unique. If two routers have the same router-ID, OSPF will prevent any kind of neighborship. Other routers that form neighbors with routers using the same router-ID will have a problem with the topology flooding process.

If you do have two of the same:


* Two in the same aread will cause Router to generate a message saying there's a duplicate router-ID.
* Two routers with the same router-ID in different areas will flush each others LSAs and declare an OSPF _Flood War_.
* The Router-ID will only change when the process is cleared, or a device is reloaded.

## Router-ID Selection

* Generally configured by the engineer.
* Highest logical loopback IP address configured on router.
* Highest IP address configured on its active interfaces
* Not preemptive

### Configurations

* To change the router-ID, use the following:

> router-id x.x.x.x (OSPF mode command)

* To verify the OSPF router-id:

> show ip ospf

> show ip ospf database

> show ip protocols


## MTU Issues

* Typical default to an IP MTU of 1500
* Router needs to forward a packet larger than the outgoing interface's MTU, it either fragments the packet or discards it.
* It dependso nthe setting of the Don't Fragment (DF) bit in the IP header: if it is SET, the packet is dropped, otherwise, it is fragmented

* The value of MTU should be the  same on the devices attached to the same data link
* If there is an MTU mismatch, they will not be able to exchange topology information

* The neighbors will get to __EXSTART__ state and then go down.
* A log message will be generated reporting "too many retransmissions"

