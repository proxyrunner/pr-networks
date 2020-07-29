# Spanning Tree Protocol

* Spanning Tree Protocol Fundamentals

How do switches become aware of other swiches and prevent L2 loops.

* Rapid Spanning Tree Protocol

Improvements made to Spanning-Tree for faster convergence.

## What's the issue?

Problems occur when connecting a second link between switches. Connecting a second link is vital because many network devices require redundancy. Or when three switches are essentially connected to each other.  The problems occur because switches must forward broadcasts or when unknown unicast flooding occurs.

Broadcasts forward in a continuous loop until the link becomes saturated, and the switch is forced to drop packets. The MAC address table must constantly change ports as the packets make loops. Due to the Layer-2 mechanism, there is no time-to-live (TTL) that will end the forwarding. Eventually the CPU utilizationg will increase as well as memory consumption, which crashes the switch.

