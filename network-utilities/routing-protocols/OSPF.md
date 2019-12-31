# Introduction to OSPF 

* OSPF is a link state routing protocol 
* OSPF uses a link state logic, which can be broken into three branches: 
    + Neighbor discovery 
        * OSPF neighbors are discovered using hello packets, just like EIGRP 
        * OSPF Hello packets are sent using multicast address 224.0.05 
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