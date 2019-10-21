# Border Gateway Protocol

## BGP Path Attributes

Every BGP update consists of one or more IP subnets and a set of attributes that are attached to them.

* BGP metrics are called path attributes
* BGP attributes are categorized as __well-known__ or __optional__
* All compliant implementations must recognize well-known attributes
* You should no expect taht all implementations can recognize optional attributes. Only some implementations (that could be private) are able to reconize optional attributes

All BGP implementations are required to recognize well-known attributes. Optional attributes are either specified in later extensions of BGP or even in private vendor extensions that are not documented in a standard document.

## Well-Known Attributes

Well-known attributes are divided into mandatory and discretionary categories.

* All well-known attributes propagate to other neighbors
* Discretionary well-known attributes are optional; they could be present in update messages

Three specific well-known attributes are required to be present on every update. They are:

1. Next-hop
2. AS-Path
3. Origin attribute

These are referred to as mandatory well-known attributes. Other well-known attributes may or may not be present, depending on the circumstances under which the updates are sent and the desired routing policy. The well-known attributes that could be present, but are not required, are called __discretionary__ well-known attributes.

* Origin

| &nbsp;e&nbsp;|&nbsp; Route originated in EGP &nbsp;|
|:---:|:---:|
| i | Route originated in an IGP |
| ? | Route was redistributed into BGP|

* AS-path
     + Sequence of AS numbers through which the network is accessible
* Next-hop
     + IP address of the next-hop router

The three mandatory well-known attributes are origin, AS-path, and next-hop:

* __Origin__: When a router first originates a route in BGP, it sets the origin attribute.  If information about an IP subnet is injected using the _network_ command or via aggregation (route summarization within BGP), the origin attribute is set to "i" for IGP.

If information about an IP subnet is injected using redistribution, the origin attribute is set to "?" for unknown or incomplete information (these two words have the same meaning). The origin code "e" was used when the Internet was migrating from EGP to BGP and is now obsolete.

* __AS-path__: The egress router modifies the AS-path attribute every time information about a particualr IP subnet passes over an AS border. When a router first originates a route in BGP, the AS-path attribute is empty. Each time taht the route crosses an AS boundary, the transmitting AS prepends its own AS number to appear first in the AS path.

You can track the sequence of autonomous systems through whic the route has passed by using the AS-path attribute.

__Next-hop__: The router also modifies the next-hop attribute as the route passes through the network. This attribute indicates the IP address of the next-hop router. The next-hop router is the router to which the receiving router should forward the IP packets to reach the destination that is advertised in the routing update.

### Discretionary Well-Known BGP Attributes

* Local preference

     + Used for consistent routing policy within an AS

* Atomic aggregate

     + Informs the neighbor AS that the originating router aggregated routes

__All__ BGP implementations must support discretionary well-known attributes. However, discretionary well-known attributes do not have to be present in all BGP updates. Routers use discretionary well-known attributes only when those functions are required.

The following are descriptions of these two attributes:

* __Local preference__: Local preference is used in the route selection process. This attribute is carried within an AS only. The router prefers a route with a high local preference value to a route with a low value.

By default, routes that are received from a peer AS are tagged with the local preference set to a value of 100 before that are entered into the local AS. If this value is changed through BGP configuration, the BGP selection process is influenced. Because all routers within the AS get the attribute along with the route, a consistent routing decision is made throughout the AS.

* __Atomic aggregate__: The atomic aggregate attribute is attached to a route that is created as a result of route summarization (called aggregation in BGP). This attribute signals that information that was present in the original routing updates may have been lost when the updates were summarized into a single entry.
