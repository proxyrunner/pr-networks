# Introduction to OSPF 

* OSPF is a link state routing protocol 
* OSPF uses a link state logic, which can be broken into three branches: 
    + Neighbor discovery 
        * OSPF neighbors are discovered using hello packets, just like EIGRP 
        * OSPF Hello packets are sent using multicast address __224.0.05__
        * OSPF does not use TCP or UDP for its transport; it uses IP protocol 89 
        * OSPF uses the concept of areas 
        * OSPF routers can be in multiple areas 
        *  Known as ABR (Area Border Router) 
    + Topology database exchange 
        * OSPF topology database, commonly known as link state database, is exchanged inside an area only 
        * This detailed topology information is not exchanged between different areas 
        * OSPF has a hierarchical design 
        * All areas must connnect in the backbone (area 0) 
        * Prevents routing loops 
    + Route computation 
        * ABRs connect non-backbone areas to the backbone area 
        * Instead of exchanging detailed topology information between areas, ABRs only advertise the subnets between areas 
        * Inside an area, all internal routers must have the same image of the network; that is, their link state databases must be the same 
        * After the link state database is populated, shortest path first (SPF) is run on the link state database (LSDB) to find the best, lowest cost, paths to all destinations 

* To configure OSPF on any router, we first enable OSPF process using the command  

```  
(conf)# router ospf <process-id> 
```

* Process ID is locally significant 
* To advertise any particular subnet or to enable any interface for OSPF to discover neighbors on that interface, the network command is used. 

```
network [ip subnet][wildcard-mask] area <area-number> 
```

* OSPF uses the same concept as EIGRP to assign a router-ID for OSPF processes 
    * manually configured router-ID is preferred over.. 
    * highest IP address of any up/up loopback interface, which is preferred over.. 
    * highest IP address of any up/up non-lookupback interface 
*  OSPF also uses the concept of DR and BDR, which will be discussed in detail later 


## OSPF Neighbor Discovery on LAN

* More complex than EIGRP
* To become neighbors, you send hello packets and match parameters, if they match properly you become neighbors.
* There are two neighborship classes:
    + 2-way neighbors
    + fully adjacent neighbors

* OSPF uses finite state machine with eight neighbor states that describe the current state of each OSPF neighbor.
* The difference between the two classes:
    + 2-way neighbor - OSPF is in the two-way state
    + Fully Adjacent Neighbor - OSPF is in the full state

OSPF will send multicast hello messages on LAN when the folowing requirements are met:

1. OSPF has been enabled on the interface using the __network__ or __ip ospf area__ interface command.
2.  The interface has not been made passive using the __passive-interface__ router ospf subcommand.


### Hello Message Parameters

* __ip ospf__ _<process-id>_ __area__ _<area-number>_ is an alternative to __network__ command.
* In hello message/packet, the following parameters must match:
    + Hello Interval
    + Dead Interval
    + Area ID
    + subnet mask
    + Stub area flag
    + Authentication

* Additional parameters that may be present in the hello packet depends on network conditions
    + OSPF router ID
    + List of neighbors reachable on the interface
    + Router priority
    + Designated router (DR) IP address
    + Backup DR IP address

* OSPF Router IP is the parameter that can cause problems; more on this later.
* If a hello is not received from a neighbor for a particular period of time  it is considered down.
* This is known as the dead interval
* By default 4x (Hello Interval)

* On a LAN the default hello interval is 10
* if the hello interval is changed, the dead interval will automatically change too (4 x hello interval)
* both sides __must__ have same hello interval or neighborship will go down

## Change hello and dead intervals

> ip ospf hello-interval <value>

> ip ospf dead-interval <value>

### To verify

> show ip ospf interface <interface>

## Final Notes

* Intervals can be modified to have faster convergence
* If OSPF neighbors are down it can be discovered in a second, the hello interval can be changed to subsecond value and the dead interval can be made 1 second:

> ip ospf dead-interval minimum hello-multiplier _multiplier_

* BFD can also be used for fast convergence.
