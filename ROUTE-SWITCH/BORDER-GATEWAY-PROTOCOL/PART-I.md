# Part I - Basic BGP Configuration

## Table of Contents

* [Basic BGP Concepts]
* [Configuring EBGP]
* [Configuring IBGP]
* [Multihop EBGP]
* [Route Exchange over BGP]
* [Route Aggregation]

## 1 - Basic BGP Concepts

### What is an Autonomous System?

A set of routers and networks under the control of a single administrative authority.

* Allows seperations of administrative domains
* IGPs run _within_ an AS
* IGPs route _between_ AS

Scaling was an issue for creating ARPA net (predescessor of Internet)

#### Problems Scaling

![Problems Scaling](../../img/BGP-AS1.PNG)

#### Separating Domains

![Domains Separated by Control](../../img/BGP-AS2.PNG)

### Back to Autonomous Systems

Moving forward...

* EGPs route _between_ autonomous systems
* BGP routes _among_ autonomous systems

![Domains Exchaning Routes](../../img/BGP-AS3.PNG)

## 1.1 Inter-domain concepts

### Autonomous System Numbers

* 16 bits
*  assigned by Regional Internet Registries, just like public IP addresses
* Public AS number
    + 1 - 64511
* Private AS number
    + 64512 - 65534
* Reserved AS Numbers
    + 0 and 65535
* New 32-bit AS numbers: RFC 4893

mBPG (multi-protocol BGP is not reviewed in this course. mBGP deals a lot with _address families_, meaning IPv4 __and__ IPv6.

For perspective between IGPs and BGP, IGPs find paths between routers, where BGP finds paths between _autonomous systems_.

### Trusted and Untrusted Peering

* IGP assumes its peers are trusted
    + all under the same administrative domain
    + therefore route exchange viewed holistically
* BGP assumes its peers are untrusted
    + under separate administrative domains
    + route information exchanged carefully
    + every external peering is viewed separately
    + incoming and ongoing route advertisements viewed separately



## Configuring EBGP

## Configuring IBGP

## Multihop EBGP

## Route Exchange over BGP

## Route Aggregation
