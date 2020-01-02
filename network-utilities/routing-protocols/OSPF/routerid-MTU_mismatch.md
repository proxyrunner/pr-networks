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
