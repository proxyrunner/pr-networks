# 1.1 Identify Cisco Express Forwarding concepts

Cisco Express Forwarding is a proprietary

## "Switching" within Routers

* Process-Based Switching

> show processes ?

* Fast Switching
* CEF

## Forwarding Information Base (FIB)

* CEF Components (FIB)
    + Forwarding Information Base
    + Copy of IP Routing Table

```
# show ip cef
# show ip cef <ip addr> <mask> detail
```
    
## Adjacency Table

* CEF Components (Adjacecny Table)
    + Populated with L2 Adjacency information 
    + Populated by L2 ttables such as:
        ARP Table
        Frame-Relay Mapping Table

```
# show adjacency <intf type/number> [summary|detail]
# show adjacency vlan <vlan-id> detail
```

### Adjacency Types

* Some adjacency types can't be CEF switched and must be dropped, or sent to CPU for processing:
    + Glean
    + Null
    + Drop
    + Discard
    + Punt

### CEF on Multilayer Switches

* CEF is enabled by default on Multilayer switches
* Because switches have specialized hardware ASICs and memory, CEF cannot be disable

### Non-CEF-Switched Packets

* Some packets on switches can't be CEF-switched;
    + ARP Requests
    + Packets requiring response from router CPU
    + Routing Protocol Traffic
    + CDP
    + Packets needing encryption

```
# show cef drop
```
