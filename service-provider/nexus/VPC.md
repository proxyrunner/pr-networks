# Virtual Port Channels on NX-OS

The main limitation on classic port channel is that it only operates between two devices. The support for multiple devices is typically required in the event of hardware failure, which would require an alternate traffic path.

The alternate path is often connected in a way that would cause a loop. vPC technology solves this by acting as a peer endpoint that looks like a single logical entity, though the two endpoints are still separate devices.

The three main use cases for vPC are as follows:

1. Dual-uplink L2 access
    * an access switch N5k is dual-homed to a pair of distrubution N7k
2. Server dual-homing
    * a server is connected via two interfaces to two separate access switches
3. Active-active fabric extenders
    * a FEX is dual-homed to a pair of nexus switches

## vPC vs. Spanning Tree Protocol

vPC and STP can provide loop prevention mechanisms. STP allows only a single path to destination; vPC can leverage redunandant connections. Failed links resolve faster with vPC.

STP has improved over the years, but still has one suboptimal flaw: to correct a network loop, only one active path is allowed from one device to another.

## vPC Components and Architecture

A pair of Nexus switches that use vPC appear as a single L2 switch to other devices. However, the two switches are separately managed with independent management and control planes.

* vPC Peers
* vPC peer link
* Cisco Fabric Services (CFS)
* vPC peer keepalive link
* vPC
* vPC domain
* vPC member port
* Orphan device
* Orphan port

## vPC Control Plane

## vPC Peer-Link Restrictions

## vPC Data Plane for External Traffic

## vPC Guidelines

## Enhanced vPC




