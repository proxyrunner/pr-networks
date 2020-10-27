# A Full Guide to BGP

Safari Books with Jeff Doyle

## Learn

* How BGP differs from IGPs
* Commands and procedures to configure and monitor BGP
* different configuration options and policies

What makes it challenging is that BGP is designed to adhere to many-many, and complex __policies__.

* PATH attributes
* tools and techniques for controlling large BGP domains

### Note

We're working on BGP version 4! That's what you should be working on.

### Basic Understandings (Prerequisites)

* IP routing
* IPv4 addressing
* Cisco IOS usage
* IP IGP configs
    + OSPF
    + EIGRP
    + Static routes

## Table of Contents

* [Basic BGP Concepts](./MOD1/1.1.md)
    + [Basic BGP Concepts Pt. II](./MOD1/1.2.md)
    + [Configuring EBGP](./MOD1/2.1.md)
    + [BGP Basic Show Commands](./MOD1/2.1.md)
    + [Configuring IBGP](./MOD1/3.1.md)
    + [Configuring IBGP Continued](./MOD1/3.2.md)
    + [Multihop EBGP](./MOD1/4.1.md)
    + [Multihop EBGP Security](./MOD1/4.2.md)
    + [Route Exchange over BGP](./MOD1/5.1.md)
    + [Routing Information Database (RIB)](./MOD1/5.2.md)
        - NEXT_HOP Attribute
        - ORIGIN Attribute
    + [Route Aggregation](./MOD1/6.1.md)
* [Routing Policies]
    + [BGP Policy]
    + [Route and Prefix Filters]
    + [AS_PATH filters]
    + [Route Maps]
    + [LOCAL_PREF]
    + [MED ATTRIBUTE]
    + [Prepend]
* [BGP Scaling]
    + [Basic Scaling]
    + [Manage Policy Changes]
    + [BGP Communities]
    + [Session and Policy Templates (Peer Groups)]
    + [Private AS Numbers]
    + [Route Reflectors]
    + [Confederations]
    + [Route Dampening]

