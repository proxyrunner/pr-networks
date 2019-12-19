# ISP IP Address Assignment

The IANA is the organization responsible for coordinating some of the key elements that keep the Internet running smoothly.

IANA:
Responsible for allocation of these globally unique elements:

* IP addresses
* AS number allocation
* DNS root zone management
* Protocol parameters

IANA is operated by ICANN

* RIRs
* Manage IP address allocation within world regions

IANA allocates and maintains unique codes and numbering systems that are used in the technical standards (“protocols”) that drive the Internet:

Coordinates the global pool of IP addresses and provides them to RIRs
Coordinates the global pool of AS numbers and provides them to RIRs
Manages the DNS root zone
Manages the Internet protocol numbering system (with standards bodies)

IANA describes their role as follows: “The IANA team is responsible for the operational aspects of coordinating the Internet’s unique identifiers and maintaining the trust of the community to provide these services in an unbiased, responsible, and effective manner.”

IANA is operated by ICANN, formed in 1998 as a not-for-profit, public-benefit corporation with participants from all over the world that is dedicated to keeping the Internet secure, stable, and interoperable.

Both IPv4 and IPv6 addresses are generally assigned in a hierarchical structure. IP addresses and IP address space ranges are assigned to subscribers by their ISP. ISPs obtain allocations of IP addresses from RIR.

The role of IANA is to allocate IP addresses from the pools of unallocated addresses to the RIRs. IANA does not make allocations directly to ISPs or end users except in specific circumstances, such as allocations of multicast addresses or other protocol-specific needs.

There are five regional RIRs:

* AfriNIC: Africa region
* APNIC: Asia/Pacific region
* ARIN: North America region
* LACNIC: Latin America and some Caribbean islands
* RIPE: Europe, the Middle East, and Central Asia

* End user requests IP address from their ISP

* IPv4 address or block of addresses
* IPv6 block of addresses
        + /64 network for end users
        + /48, /52, /56 for business users

* ISP distributes addresses from its assigned address space
* There are two types of IP addresses:
    + Provider-assigned address
        * Assigned by ISP from ISP address space
        * Renumbering needed when changing ISP provider
    + Provider-independent address
        * Assigned by RIR from its special address space

End users always send requests for an address space to their ISP. ISPs can assign one public IP address or a range of IP addresses.

In the IPv6 environment, ISPs typically assign /64 blocks of IP addresses to end users (this allocation is the smallest range of IP addresses that ISPs can assign) and /48, /52, or /56 blocks to business users. Block sizes depend on customer needs.

Blocks of IP addresses can be PI or PA. A PA block of IP addresses is used in simple topologies, where no redundancy is needed. Address space is assigned to you by the ISP from its address space. If you change your ISP, the new provider will give you new PA address space and you will have to renumber all devices with public IP addresses. You cannot transfer your old address space to the new service provider.

For a multihomed connection, PI address space is required. This address space is assigned to you directly by the RIR from its special address space. This address space can be routed through different service providers, so you have more flexibility when planning your connection to ISPs.
