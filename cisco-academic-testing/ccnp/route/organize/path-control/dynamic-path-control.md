# Dynamic Path Control
    
* PBR is a static path control mechanism.
* PBR cannot respond to changes in the network.
* Cisco IP SLA can be used to complement PBR to achieve dynamic path control.

However, a dynamic response is exactly what is commonly needed in modern networks. For example, you have two uplinks to two different ISPs in your enterprise network. Instead of BGP, you are using static default routes to ISPs, and the route to ISP #2 has a higher administrative distance, so only the primary uplink is used.

You want to be able to switch over to the backup uplink when packet loss exceeds 5 percent on the primary uplink. You cannot accomplish this type of configuration with PBR alone. Cisco IP SLA can be used to complement PBR to achieve this goal.

End-to-end network performance tests are based on clear measurement metrics.

Cisco IOS IP SLA can be used for path control.

Configuration:
    Define one or more probes.
    Define one or more tracking objects.
    Define the action for each tracking object.

Cisco IOS IP SLAs perform network performance measurement within Cisco devices. The IP SLAs use active traffic monitoring (generation of traffic in a continuous, reliable, and predictable manner) for measuring network performance. Cisco IOS IP SLAs actively send data across the network to measure performance between multiple network locations or across multiple network paths. They use time-stamp information to calculate performance metrics, such as jitter, latency, network and server response times, packet loss, and mean opinion score.

Cisco IP SLA can be coupled with PBR or with static routes to achieve dynamic path control.

The following steps are required to configure Cisco IOS IP SLA functionality:

    Define one or more probes.
    Define one or more tracking objects.
    Define the action for each tracking object.