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

* [Basic BGP Concepts](./PART1/)
    + [Configuring EBGP](./PART1/1.1.md)
    + [Configuring IBGP](./PART1/1.1.md)
    + [Multihop EBGP](./PART1/1.1.md)
    + [Route Exchange over BGP](./PART1/1.1.md)
    + [Route Aggregation](./PART1/1.1.md)
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

