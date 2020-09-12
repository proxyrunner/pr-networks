# Introduction to Fabric Path

Fabric Path is a proprietary Cisco feature set that can be implemented on Nexus switches.

* superset of [TRILL](https://en.wikipedia.org/wiki/TRILL_(computing))
* It brings the performance and stability of routing to a layer 2 network
* high scalable and resilient 
* allows multipath networking at L2 level
* no STP needed

Similar to spine-leaf, allows multipath networking at the L2 level. Therefore the shortest path is any-to-any. Single address lookup at the ingress edge indentifies the exit port across the fabric.

Traffic is switched using the shortest path that is available. Reliable Layer 2 and Layer 3 connectivity is provided using any-to-any. __Equal cost multi-pathing [ECMP]__ across up to 16 links between devices. If you think about portchannel, it can become highly efficient and stable.

## FabricPath Swich IDs and Trees

### Switch ID

* Switch ID is used to identify switches 
* automatically or manually assigned
* FabricPath creates a tree topology that is used for:
    + unknown unicasts
    + broadcast
    + multicast
* you can have more than one tree

We use conversational MAC address learning, not MAC learning, meaning each interface only learns that MAC addres for interested ports. Rather than all MAC addresses in the domain, only ones that are actively talking.

This method consists of a 3-way handshake. 

As example, lets say we have a device wanting to talk to an unknown address. It will first speak up to it's unicast root switch, then the unknown unicast wil be sent out to all of the other leafs that have devices attached to it. When it finds the device they will begin the initial conversation, and our original switch will now know the best path.

