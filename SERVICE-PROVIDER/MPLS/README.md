# MPLS Fundamentals

[Back](../../README.md) to my repository!

## Table of Contents

### Introduction and Architecture

* [Introduction to MPLS Fundamentals](./1_introduction.md)
* [MPLS Architecture](./MOD1/1.0.md)
* [MPLS Labels, LSPs, and FECs](./MOD1/2.1.md)
* [Label Distribution Protocols](./MOD1/2.2.md)
* [Label Distribution Modes](./#)
* [Label Forwarding Instance Base (LFIB)](./#)

### Forwarding Labels

* [Label Stack](./#)
* [Forwarding with Labels](./#)
* [Reserved Labels: Range and Values](./#)
* [Reserved Labels: Demonstrations](./#)
* [TTL Handling](./#)

### Label Distribution Protcol

* [LDP Operation: Basics, Building Blocks, and Messages](./#)
* [LDP Operation: Creating LFIB Entries, Creating LSPS, and Targeted LDP Sessions](./#)
* [LDP Operation: Demonstration](./#)
* [Label Advertisement Control](./#)
* [LDP Session Protection](./#)


### MPLS VPN Layer 3

* [Introduction to MPLS VPN](./#)
* [Virtual Routing and Forwarding (VRF)](./#)
* [Route Advertisement: Building Blocks](./#)
* [Route Advertisement: Route Propagation and VPN Extranet](./#)
* [Route Advertisement: Demonstration](./#)
* [Packet Forwarding](./#)
* [PE-CE Routing Protocols](./#)
* [PE-CE Routing Protocols: Demo](./#)
* [Internet Access and Multi-VRF CE (VRF Light)](./#)
* [6PE](./#)
* [6VPE](./#)

### Inter-Autonomous MPLS VPN

* [Inter-AS MPLS VPN Option A](./#)
* [Inter-AS MPLS VPN Option B: Mechanics](./#)
* [Inter-AS MPLS VPN Option B: Demo](./#)
* [Inter-AS MPLS VPN Option C: Mechanics](./#)
* [Inter-AS MPLS VPN Option C: Demo](./#)
* [Inter-AS MPLS VPN Carrier's Carrier](./#)

### MPLS VPN Layer 2

* [MPLS VPN Layer 2: Architecture and Fundamental Concepts](./#)
* [MPLS VPN Layer 2: Point-to-Point Services Demo](./#)
* [Point-to-Point vs Point-to-Multipoint](./#)
* [MPLS VPN Layer 2: Point-to-Multipoint Services Demo](./#)

### Traffic Engineering

* [Why Traffic Engineering](./#)
* [Distribution of TE Information (IGP): Fundamental Concepts](./#)
* [Distribution of TE Information (IGP): Demonstration](./#)
* [RSVP: PATH and Resv Messages](./#)
* [RSVP: Signaling and Special Messages](./#)
* [RSVP: Demonstation](./#)
* [Routing and Cost of TE LSP](./#)
* [Forwarding onto TE LSPs](./#)
* [Fast ReRoute (FRR)](./#)
* [FRR Link Protection](./#)
* [FRR Path Protection](./#)
* [MPLS TE and MPLS VPN](./#)

### MPLS Segment Routing

* [Overview of Segment Routing](./#)
* [IGP and Label Distribution: Fundamental Concepts](./#)
* [IGP and Label Distribution: Demonstration](./#)
* [Traffic Engineering with Segment Routing](./#)
* [Controllers](./#)

### MPLS QoS Modes

* [Uniform, Short Pipe, Pipe Modes](./#)

### Troubleshooting MPLS Networks

* [Ping and Traceroute in MPLS Network](./#)
* [Applying Traceroute in MPLS Network](./#)

## Fast Start

So you just want to get started and move on, yeah? No problem. Lets get you going.

```
# ---------- [ START SCRIPT ] ---------- #
# Requires configuration mode privileges.
#
!
# Globally enable hop-by-hop forwarding
!
mpls ip 
!
# Specify LDP as the default label distribution protocol
!
mpls label protocol ldp 
!
# create and enable a routing protocol to use MPLS
!
router ospf 1
!
# advertise
!
network 10.1.1.0 255.255.255.0 area 0
!
# MPLS LDP Autoconfig for interfaces belonging to 
# OSPF process.
# If no area is specified, the command applies to 
# all interfaces in the OSPF process.
!
mpls ldp autoconfig
!
# VERIFICATION COMMANDS:
#
# show mpls ldp discovery 
# show mpls interfaces
# ---------- [ END SCRIPT ] ---------- #
```

```
*Oct 31 01:14:12.671: %SYS-5-CONFIG_I: Configured from console by consoleshow mpls interfaces
Interface              IP            Tunnel   BGP Static Operational
GigabitEthernet0/0     Yes (ldp)     No       No  No     Yes        
GigabitEthernet1/0     Yes (ldp)     No       No  No     Yes        

*Oct 31 01:14:45.039: %OSPF-5-ADJCHG: Process 1, Nbr 10.2.255.3 on GigabitEthernet1/0 from LOADING to FULL, Loading Doneshow mpls lpd discovery

LR2#show mpls ldp discovery
 Local LDP Identifier:
    10.2.255.2:0
    Discovery Sources:
    Interfaces:
        GigabitEthernet0/0 (ldp): xmit
        GigabitEthernet1/0 (ldp): xmit/recv
            LDP Id: 10.2.255.3:0; no route
LR2#
``` 