# OSPF Lab

In this document we're going to review the configurations to operate a fully functional OSPF lab on GNS3 with various features being explored. If you're new to networking, please checkout my introductory tutorial to the [__dynamic routing protocol, OSPF!__](https://github.com/gil-ryan/grs-networking-public/blob/master/network-utilities/routing-protocols/OSPF/OSPF.md)

## Topology

![OSPF Topology](https://raw.githubusercontent.com/gil-ryan/grs-networking-public/master/cisco-academic-testing/ccnp/route/labs/ospf-simulation.png)

## Features

* [Authentication](https://github.com/gil-ryan/grs-networking-public/blob/master/network-utilities/routing-protocols/OSPF/OSPF-authentication.md)

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

```
!
interface Loopback0
 ip address 3.3.3.3 255.255.255.255
!
interface Serial5/0
 ip address 192.168.23.3 255.255.255.0
 ip ospf network non-broadcast
 serial restart-delay 0
!
interface Serial5/1
 ip address 192.168.13.3 255.255.255.0
 ip ospf network non-broadcast
 serial restart-delay 0
!
interface Ethernet6/0
 ip address 192.168.34.3 255.255.255.0
 duplex half
!
router ospf 1
 area 1 virtual-link 4.4.4.4
 network 3.3.3.3 0.0.0.0 area 0
 network 192.168.13.0 0.0.0.255 area 0
 network 192.168.23.0 0.0.0.255 area 0
 network 192.168.34.0 0.0.0.255 area 1
 neighbor 192.168.23.2
!
```

## R4

```
!
interface Loopback0
 ip address 4.4.4.4 255.255.255.255
!
interface Ethernet6/0
 ip address 192.168.34.4 255.255.255.0
 duplex half
!
interface Ethernet6/1
 ip address 192.168.45.4 255.255.255.0
 duplex half
!
interface Ethernet6/2
 ip address 192.168.46.4 255.255.255.0
 duplex half
!
router ospf 1
 area 1 virtual-link 3.3.3.3
 area 2 nssa
 area 3 stub no-summary
 network 4.4.4.4 0.0.0.0 area 1
 network 192.168.34.0 0.0.0.255 area 1
 network 192.168.45.0 0.0.0.255 area 2
 network 192.168.46.0 0.0.0.255 area 3
!
```

## R5

```
!
interface Loopback0
 ip address 5.5.5.5 255.255.255.255
!
interface Loopback1
 ip address 5.5.1.1 255.255.255.255
!
interface Loopback2
 ip address 5.5.2.1 255.255.255.255
!         
interface Loopback3
 ip address 5.5.3.1 255.255.255.255
!
interface Loopback4
 ip address 5.5.4.1 255.255.255.255
!
interface Ethernet6/1
 ip address 192.168.45.5 255.255.255.0
 duplex half
!
router ospf 1
 area 2 nssa
 network 5.5.0.0 0.0.255.255 area 2
 network 192.168.45.0 0.0.0.255 area 2
!
```

## R6

```
!
interface Loopback0
 ip address 6.6.6.6 255.255.255.255
!
interface Ethernet6/2
 ip address 192.168.46.6 255.255.255.0
 duplex half
!
router ospf 1
 area 3 stub
 network 6.6.6.6 0.0.0.0 area 3
 network 192.168.46.0 0.0.0.255 area 3
!
```