# Policy-Based Routing (PBR)

## What is PBR

* Enable you to implement policies that selectively cause packets to take different paths:
   +  IP routing is destination-based.
   +  PBR overrides destination-based routing.

* Applied to incoming or locally generated packets
* Require a route map to implement the policy:
   + Interesting traffic is defined with the match command.
   + Destination for interesting traffic is defined with the set command.

PBR offers significant benefits in terms of implementing user-defined policies to control traffic in the internetwork. It provides solutions in cases where legal, contractual, or political constraints dictate that traffic is routed through specific paths.

PBR adds flexibility in a difficult-to-manage environment by route traffic that is based on network needs. For network managers who implement routing policies in their networks, PBR provides a powerful, simple, and flexible tool.

PBR is used to bypass the routing table. It enables you to configure different routing rules beyond the original IP routing table. One of the ways that it can be used is to route packets that are based on the source IP address instead of the destination IP address. PBR is applied to incoming or locally generated packets that are sent by the router itself. PBR is implemented using route maps, for which match commands are used to match the incoming packets, and a subset of the set commands is used to change the default destination-based routing.