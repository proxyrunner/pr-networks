# Using IP SLA for Path Control

To achieve dynamic path control, you can couple IP SLA with the following:

## Static routes

RTR(config)# ip route 192.168.100.0 255.255.255.0 10.1.1.1 track 1

## Policy-based routing

RTR(config-route-map)# set ip next-hop verify-availability 10.1.1.1 10 track 1

To achieve dynamic path control, you need to use IP SLA with either static routes or PBR. This action is the final step of the IP SLA configuration.

When you use IP SLA with static routes, you basically control whether the route in question will be active, based on the status of the tracked object.

In this example, SLA object 1 is verifying the state of ISP #1. If you want to use the primary uplink, if the router at ISP #1 premises is alive, you need to use the ip route 0.0.0.0 0.0.0.0 10.1.1.1 track 1 command.

If you want to use IP SLA with PBR, you have to use the verify-availability keywords when you set the next hop within a route map. The full command would be set ip next-hop verify-availability 10.1.1.1 10 track 1. If the status of the tracked object is up, the set ip next-hop command is used and the traffic is redirected. If, on the other hand, the status of the tracked object is down, the set ip next-hop command is bypassed, and destination-based routing is used to forward a packet. Notice also the use of the sequence number parameter after the verify-availability command, which enables you to conditionally specify several different next hops. In this example, the sequence number 10 is used.