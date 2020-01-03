# OSPF Lab

In this document we're going to review the configurations to operate a fully functional OSPF lab on GNS3 with various features being explored.

## Topology

![OSPF Topology](https://raw.githubusercontent.com/gil-ryan/grs-networking-public/master/cisco-academic-testing/ccnp/route/labs/ospf-simulation.png)

## Basic Configurations

### IOS Version

Cisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)XB10, RELEASE SOFTWARE (fc1)

## R1

```
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!         
!         
interface Serial5/0
 ip address 192.168.13.1 255.255.255.0
 ip ospf network non-broadcast
 serial restart-delay 0
!         
router ospf 1
 network 1.1.1.1 0.0.0.0 area 0
 network 192.168.13.0 0.0.0.255 area 0
!     
```

## R2

```
!
interface Loopback0
 ip address 2.2.2.2 255.255.255.255
!

interface Serial5/1
 ip address 192.168.23.2 255.255.255.0
 ip ospf network non-broadcast
 serial restart-delay 0
!
router ospf 1
 network 2.2.2.2 0.0.0.0 area 0
 network 192.168.23.0 0.0.0.255 area 0
 neighbor 192.168.23.3
! 
```

## R3
## R4
## R5
## R6