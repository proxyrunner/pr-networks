# Announcing Networks in BGP

Before you can inject any routing information into BGP tables for advertising, some basic configuration is required. Only administratively defined networks are announced in BGP.

* Manually configure networks to be announced
* Use redistribution in IGP
* Use aggregation to announce summary prefixes

## There are two ways to accomplish network announcements:

1. Using the __network__ configuration command to list network numbers that are candidates to be advertised. If any of these listed are reachable by the local router, then the network is injected as a route into the BGP table.

2. Redistribute routing information that has been learned by other routing protocols into the BGP table. You can use the IGP that is used within the AS. Any route that is known by the local IGp can be injected into the BGP table by using route redistribution between the IGp and BGP on the local router.

## Auto-Summary

A router can also introduce routing information into the BGp table by summarizing the routes that are already there. This is called aggregation and also requires configuration. Any route that the router introduces into the BGP table will appear as a new route. The AS-path attribute for such a route will be empty, indicating a local route. The AS-path attribute changes after passing through AS-boundaries.

> router(config-router)# (no) auto-summary

* Enables or disables summarization of networks before insertion to BGP table.
    + Locally inserted networks (using _network_ command)
    + Redistributed routes
* Enabled by default

When the router is configured to announce routes into BGP locally, the behavior of the network command varies depending on whether automatic summarization is enabled or disabled. When auto-summarization is enabled, the command summarizes locally originated BGP networks to their classful boundaries. By default, automatic summarization is enabled for BGP.

When a subnet exists and these three conditions are satisfied, then any subnet (component route) of that classful network in the local routing table will prompt BGP to install the classful network into the BGP table: 

* A classful network statement for that network exists in the routing table.
* A classful mask has been configured on that network statement
* automatic summarization is enabled

When automatic summarization is disabled, the routes that are introduced locally into the BGP table are not summarized to their classful boundaries. The BGP __auto-summary__ comand is also responsible for the behavior of the redistribution procedure in BGP. When enabled, all redistributed subnets will be summarized to their classful boundaries in the BGP table. When disabled, all redistributed subnets will be present in their original form in the BGP table.

> router(config-router)# network _major-network-number_

* Allows advertising of major networks in BGP
* At least one of the subnets must be present in the routing table
* Behavior depends on the presence of the _auto-summary_ command
* The meaning of the _network_ command in BGP is completely different from other protocols

You can also use the _network_ command with _mask_ to distinguish the classful approach. At least one subnet of the specified major network needs to be present in the IP routing table to allow BGP to start announcing the najor network as a BGP route. If automatic summarization is disable, an exact match is required.

> router(config-router)# network _major-network-number_ route-map _route-map-name_

* The addition of the route-map option allows netowrk parameters to be modified before you enter them into the BGP table.
* The __route-map__ option can be used for the following:
    + Changing the weight value of a locally sourced route
    + Tagging sourced routes with BGP communities
    + Setting the local preference for a specific network
    + Changing the MED value for a specific network

The following route map can change the following attributes of locally sourced networks with the _network_ command:

* Weight(Default = 32768): Cisco special attribute that is used in path selection process when there is more than one route to the same destination. Because weight is considered before local preference in BGP route selection, locally sourced routes are always preferred, unless the weight value is modified.
* Community (No default): This attribute is used for tagging routes at their source
* Local Preference (default value = 100): AS-wide BGP best-path selection
* MED (default=0): Return-path selection within topologies where multiple exit points to the same neighbor AS exists

### Quick Example

A subnet existing in the routing table is 75.75.75.0/24, and the network 75.0.0.0 is configured under the _router bgp_ command (auto-summary enabled), BGP will introduce the classful network 75.0.0.0/8 in the BGP table. If the following conditions are not all met, then BGP will not install any entry in the BGP table unless there is an exact match in the IP routing table: 

* a classful network statement for the network exists in the routing table
* a classful mask has been configured on that network statement
* automatic summarization is enabled.

## Redistributing Routes into BGP

There are two alternatives for injecting local routes into the BGP table: list them by using the _network_ command or redistribute them. Listing the routes give you total control over networks that could possible be advertised by BGP. This option is very desirable for multihomed customers or ISPs. On the other hand, this approach requires many configurations and can be tedious to maintain.

* Easier than listing networks in BGP process in large networks
* Redistributed routes carry the origin attribute "incomplete"
* Always filter redistributed routes to prevent route leaking
* Avoid in service provider environments

If there are a lot of networks to be advertised, and BGP is used primarily to achieve scalability, not routing security (for example, in enterprise), it could be easier to let the local IGP find the routes and then redistribute them into BGP. However, this approach introduces the risk that the IGP may find some networks that are not supposed to be advertised. Private network numbers, such as 10.0.0.0/8, are often used within an AS for various reasons but must never be advertised out to the Internet. Careful filtering must be done to prevent unintentional advertising.

When a router injects a route that is listed with the __network__ command into its BGP table, the origin code is set to "IGP." If the route is injected into the BGP table through redistribution, the origin code is set to "unknown/incomplete."