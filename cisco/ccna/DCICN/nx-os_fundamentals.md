# NX-OS Neighbor Discovery Tools

This sections will be subject to updates as there are many components to this course.

## Cisco NX-OS Virtual Routing and Forwarding

NX-OS VRF process, defaults, and basic operation.

Device virtualization is one of the main features of Nexus. A VRF is a virtual N5k Series switch running in isolotaion on a physical switch. There are only two possible VRFs of the N5k switch: management and default. The mgmt0 interface is permanently part of the management VRF, while other interfaces are permanently part of the default VRF.

The N5k platform permits the creation of additional VRFs. Again, the mgmt 0 interface permanently part of management VRF. All other interfaces are in the default VRF until those interfaces are reassigned to another VRF by the administrator.

To display the IP-related parameters of an interface in a nondefault VRF, the:

> show ip interface brief vrf _vrf-name_

command is used. If the VRF name is not specified, the default behavior of the Cisco NX-OS software is to treat the command as belonging to the default VRF.

### Management VRF

The mgmt 0 interface permanently resides in the management VRF.

> N5K-1# conf

> N5K-1(config)# interface mgmt 0

> N5K-1(config-if)# ip address 10.10.10.1/24

> N5K-1(config)# show ip interface brief vrf management

```
IP Interface Status for VRF "management"(2)
Interface            IP Address      Interface Status
mgmt0                10.10.10.1      protocol-up/link-up/admin-up 
```

> N5K-1# ping 192.168.0.68 vrf management count 1

```
PING 192.168.0.68 (192.168.0.68): 56 data bytes
64 bytes from 192.168.0.68: icmp_seq=0 ttl=254 time=4.537 ms
--- 192.168.0.68 ping statistics ---
1 packets transmitted, 1 packets received, 0.00% packet loss
round-trip min/avg/max = 4.537/4.536/4.537 ms
```

In the example output _show ip interface brief vrf managemnet_ command is used to display IP-related parameeters of the mgmt 0 interface, which are part of the management VRF.

The ping command therefore must specify the _vrf management_.

### Default VRF

> N5K-1(config)# show ip interface brief

```
IP Interface Status for VRF "default"(1)
Interface            IP Address      Interface Status
```

> N5K-1# ping 192.168.0.68 count 1

```
PING 192.168.0.68 (192.168.0.68): 56 data bytes
ping: sendto 192.168.0.68 64 chars, No route to host
Request 0 timed out

--- 192.168.0.68 ping statistics ---
1 packets transmitted, 0 packets received, 100.00% packet loss
```
