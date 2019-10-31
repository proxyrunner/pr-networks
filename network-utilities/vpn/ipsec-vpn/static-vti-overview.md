# Statis VTI Overview

## Virtual Tunneled Interfaces

* While GRE interfaces can interoperate with IPsec, they are not "native" IPsec interfaces and have a number of issues:
    + Line protocol is up when route to tunnel destination is in RIB. [Not IPsec state aware]
    + Tunnel interface MTU is disconnected from actual MTU. [Tunnel MTU != usable MTU]
* Virtual Tunneled Interfaces (VTI) are a native IPsec interface types:
    + Line protocol up only after phase 2 negotiation is completed. [IPsec "stateful"]
    + VTI MTU = usable MTU
* Two flavors;
    1. Dynamic: client access VPNs
    2. Static: site to site VPN

## Static VTI Configuration Sample

### Configuration Tasks

* Phase 1: parameters, basically the same:
    1. ISAKMP policy
    2. ISAKMP key, assuming pre-shared key
* Phase 2:
    1. IPsec ISAKMP transform set
    2. IPsec profile
    3. Change tunnel mode to "ipsec ipv4"
