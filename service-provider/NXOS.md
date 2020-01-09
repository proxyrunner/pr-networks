# Cisco's Nexus Platform

Cisco Nexus Operating System (NX-OS) does not support PAgP for port channels.

## LAN Port Channel Modes

Several port channel modes are available that must be configured to correspond between devices. Some combinations of port modes are supported; others are not. The following table lists the channel modes.

* Passive (LACP)
    *  Responds to LACP packets that it receives
    * Does not initiate LACP negotiation
* Active (LACP)
    * Initiates negotiations with other ports by sending LACP packets
* On (Static)
    * Does not send any LACP packets
    * Does not join any LACP channel groups
    * Becomes an individual link with that interface

Note: You must enable the LACP feature before you can configure and use LACP functions.

| Channel Mode | Passive | Active | On |
|:-:|:-:|:-:|:-:|
|Passive|—|OK|—|
|Active|OK|OK|—|
|On|—|—|OK|

Port channel configurations that are invalid will not result in a creation of a PC. Ports in a port channel are operational when port status is __channeling__.

## Port Channel Load Balancing

![Port-Channel Load Balancing](https://raw.githubusercontent.com/gil-ryan/grs-networking-public/master/img/pc-load-balancing.png)

The Cisco Nexus Series switches support the bundling of up to 16 ports into a port channel.

The Cisco Nexus Series switch load-balances all traffic that is switched or routed to a port channel interface across all operational individual physical links by hashing the various header fields in a frame into a numerical value that selects one of the links in the channel. Lad-balancing is performed in the hardware and is enabled by default. The load-balancing method can be applied to all port channels on a specified module. If a per-module load-balancing method is configured, it takes precedence over the switchwide setting.

You can configure the switch to use one of the following load-balancing methods:

    * Destination MAC address
    * Source MAC address
    * Source and destination MAC addresses
    * Destination IP address
    * Source IP address
    * Source and destination IP addresses
    * Source TCP or UDP port number
    * Destination TCP or UDP port number
    * Source and destination TCP or UDP port numbers

The goal of load balancing is not only to utilize all available links, but also to ensure that packets with the same header will be forwarded on the same physical link in order to prevent packet reordering.

## Port Channel Layer 2 and Layer 3 Interfaces

A PC configuration can run on OSI Layer 2 or Layer 3. Interface classification can be chosen by the administrator.

The figure shows the difference between Layer 2 and Layer 3 PC configuration.

![Layer 3 Routing](https://raw.githubusercontent.com/gil-ryan/grs-networking-public/master/img/pc-l3-routing.png)

You can classify port channel interfaces as Layer 2 or Layer 3 interfaces. In addition, you can configure Layer 2 port channels in either access or trunk mode. Layer 3 port channel interfaces have routed ports as channel members and may have subinterfaces.

You can configure a Layer 3 port channel with a static MAC address. If you do not configure this value, the Layer 3 port channel then uses the router MAC of the first channel member to come up.

On the Cisco Nexus 7000 Series Switches, all ports in a port channel must be in the same VDC.