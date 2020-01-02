# Link State Advertisements

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

### More Information

OSPF identifies Type 1 LSA using 32-bit linkstate identifier (LSID), and every router uses its own OSPF router-id as the LSID. ABRs create multiple Type 1 LSAs for themselve, one per hour. OSPF speakers will generate Type 1 LSAs by default.

Type 1 LSAs also include information about its attached links, as such:

* Interface with no neighbors:
    + its subnet number/mask is advertised
    + link connected to a 'stub network'
* Interface with DR:
    + the IP address of the DR
    + link connected to a transit network
* Interface with no DR:
    + it lists the neighbor's RID
    + link connected to 'another router (point-to-point)'

## OSPF Type 2 LSA - Network LSA

* Network LSAs are generated for multi-access networks. They are required for OSPF to properly map routers to single multi-access network, like LANs. Generation of Type 2 LSAs depend on the existence of a DR.

* Some OSPF network types require a DR, the network type tells the router's interface whether a DR should be elected. OSPF uses DR for two purposes:
    + Create and flood a Type 2 network LSA for that subnet
    + To aid in the detailed process of database exchange over that subnet

* OSPF elects a DR and a BDR, based on the information in a OSPF Hello packet.
* The hello packet lists each router's RID and a priority value.
* Routers use the following election rules to decide on a DR:
    + Choose router with highest priority value (default 1, max is 255)
    + If priority is tied, choose the router with highest RID
    + Choose a BDR, based on next-best priority, or if a tie, next highest RID.

* To change a default priority:

> ip ospf priority _value_ (interface command)

* When a DR or BDR fails, or a new OSPF neighbor comes up with a higher priority:
    + When DR fails, current BDR becomes the new DR.
    + Election is held only for BDR, __not__ the DR.
    + If DR and BDR have been elected, no new OSPF neighbor with higher priority can take over the DR or BDR role until DR or BDR fails.
    + The DR's interface IP address is used as the LSID for Type 2 LSA.

* Type 2 LSA also list the RIDs of the OSPF neighbors connected/attached to that multi-access network
* Type 2 LSA is listed under "Net Link State (Area x)" in the output of __show ip ospf database__
* To get detailed output of type 2 LSAs, use the __show ip ospf database network x.x.x.x__

### Example output

> show ip ospf database network 3.3.3.3

## OSPF Type 3 LSA - Network Summary LSA

* OSPF uses the concept of areas to reduces memory and compute resource consumption.
* ABRs are used to connect different OSPF areas together.
* Type 1 and Type 2 LSAs are not advertised from one area to another via ABR

* Not advertising Type 1 and 2 LSAa across areas saves memory and reduces the complexity for each run of the SPF algorithm
* This saves CPU and convergence time
* ABRs generate a Type 3 LSA for each subnet in an area, and advertise each Type 3 LSA into the other area.

* Type 3 LSA does not contain all the detailed topology information.
* Type 3 LSA, created by ABR, consists of each subnet and a cost to reach that subnet from that ABR.
* It summarizes the information from Type 1 & 2 LSAs
* Known as the Network Summary LSA.
* Type 3 LSA appears to be another subnet connected to the ABR that created and advertised the Type 3 LSA.

