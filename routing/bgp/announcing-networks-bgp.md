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
