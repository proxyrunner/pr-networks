# Border Gateway Protocol

BGP provides an interdomai routing system that guarantees a loop-free exchange of routing information between autonmous systems. 

* Interdomain
* EGP
* policy-based
* controlled via multiple attributes

## Vector Functionality

Network reachability information are also called path vectors, made up of path attributes. Path vector information includes a list of the complete path, hop by hop, of BGP AS numbers required to reach a destination network.

The AS path is always loop-free. A routing running BGP will not accept a routing update that includes its AS number in the path list.

## Routing Policy

* BGP can control the traffic path to a neighboring AS
* BGP cannot control how a neighboring AS routes traffic.

BGP stats that a router can advertise to neighboring autonomous systems only those routes that it uses itself. This rule reflects the hop-by-hop routing paradigm that the Internet generally uses.
