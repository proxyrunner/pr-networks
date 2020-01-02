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

## Link State Advertisements

* Type 1: Router LSA
* Type 2: Network LSA
* Type 3: Network Summary LSA
* Type 4: ASBR Summary LSA
* Type 5: AS External LSA
* Type 6: Group Membership LSA
* Type 7: NSSA External LSA
* Type 8: External Attributes LSA
* Type 9-11: Opaque LSA

We're covering types 1,2,3,4,5, and 7

## OSPF Type 1 LSA - Router LSA

Every router creates one for itself and floods it throughout the same OSPF area. This LSA identifies an OSPF router based on its OSPF router-id.

All type 1 LSAs, for the same area, are listed under 'Router Link States (Area x)' in the output of the __show ip ospf database__ command. To verify the information that each Type 1 LSA carries, use the __show ip ospf database router x.x.x.x__ command.

### Example output:

Here is output from a router an ABR:

> show ip ospf database

```
R3#show ip ospf database

            OSPF Router with ID (3.3.3.3) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
3.3.3.3         3.3.3.3         83          0x80000002 0x0004B6 4
4.4.4.4         4.4.4.4         1     (DNA) 0x80000002 0x000D5B 1

                Summary Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
4.4.4.4         3.3.3.3         94          0x80000001 0x00E431
4.4.4.4         4.4.4.4         9     (DNA) 0x80000001 0x0062B9
5.5.1.1         4.4.4.4         9     (DNA) 0x80000001 0x00EC29
5.5.2.1         4.4.4.4         9     (DNA) 0x80000001 0x00E133
5.5.3.1         4.4.4.4         9     (DNA) 0x80000001 0x00D63D
5.5.4.1         4.4.4.4         9     (DNA) 0x80000001 0x00CB47
5.5.5.5         4.4.4.4         9     (DNA) 0x80000001 0x009875
6.6.6.6         4.4.4.4         9     (DNA) 0x80000001 0x006A9F
192.168.34.0    3.3.3.3         129         0x80000001 0x006A31
192.168.34.0    4.4.4.4         9     (DNA) 0x80000001 0x004C4B
192.168.45.0    4.4.4.4         9     (DNA) 0x80000001 0x00D2B9
192.168.46.0    4.4.4.4         9     (DNA) 0x80000001 0x00C7C3

                Summary ASB Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
4.4.4.4         3.3.3.3         84          0x80000001 0x00CC49

                Router Link States (Area 1)

Link ID         ADV Router      Age         Seq#       Checksum Link count
3.3.3.3         3.3.3.3         83          0x80000003 0x00B03C 1
4.4.4.4         4.4.4.4         84          0x80000004 0x00625D 2

                Net Link States (Area 1)

Link ID         ADV Router      Age         Seq#       Checksum
192.168.34.4    4.4.4.4         100         0x80000001 0x00F489

                Summary Net Link States (Area 1)

Link ID         ADV Router      Age         Seq#       Checksum
3.3.3.3         3.3.3.3         129         0x80000001 0x00AE75
5.5.1.1         4.4.4.4         93          0x80000001 0x00EC29
5.5.2.1         4.4.4.4         93          0x80000001 0x00E133
5.5.3.1         4.4.4.4         93          0x80000001 0x00D63D
5.5.4.1         4.4.4.4         93          0x80000001 0x00CB47
5.5.5.5         4.4.4.4         93          0x80000001 0x009875
6.6.6.6         4.4.4.4         93          0x80000001 0x006A9F
192.168.13.0    3.3.3.3         129         0x80000001 0x00700A
192.168.23.0    3.3.3.3         129         0x80000001 0x00026E
192.168.45.0    4.4.4.4         93          0x80000001 0x00D2B9
192.168.46.0    4.4.4.4         93          0x80000001 0x00C7C3

                Summary ASB Link States (Area 1)

Link ID         ADV Router      Age         Seq#       Checksum
4.4.4.4         3.3.3.3         79          0x80000001 0x00CC49
```

> show ip ospf database router 3.3.3.3

```
R3#show ip ospf database router 3.3.3.3

            OSPF Router with ID (3.3.3.3) (Process ID 1)

                Router Link States (Area 0)

  LS age: 143
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 3.3.3.3
  Advertising Router: 3.3.3.3
  LS Seq Number: 80000002
  Checksum: 0x4B6
  Length: 72
  Area Border Router
  Number of Links: 4

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 3.3.3.3
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 192.168.23.0
     (Link Data) Network Mask: 255.255.255.0
      Number of MTID metrics: 0
       TOS 0 Metrics: 64

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 192.168.13.0
     (Link Data) Network Mask: 255.255.255.0
      Number of MTID metrics: 0
       TOS 0 Metrics: 64

    Link connected to: a Virtual Link
     (Link ID) Neighboring Router ID: 4.4.4.4
     (Link Data) Router Interface address: 192.168.34.3
      Number of MTID metrics: 0
       TOS 0 Metrics: 10



                Router Link States (Area 1)

  LS age: 143
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 3.3.3.3
  Advertising Router: 3.3.3.3
  LS Seq Number: 80000003
  Checksum: 0xB03C
  Length: 36
  Area Border Router
  Virtual Link Endpoint
  Number of Links: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.34.4
     (Link Data) Router Interface address: 192.168.34.3
      Number of MTID metrics: 0
       TOS 0 Metrics: 10
```