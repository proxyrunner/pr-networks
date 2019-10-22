# Optional BGP Attributes

Optional BGP attributes are either transitive or nontransitive. Here are the differences:

* Transative: propagated to other neighbors if not recognized, partial bit set indicates that the attribute was not recognized
* Nontransitive: discarded if not recognized

Recognized optional attributes are propagated to other neighbors based on their meaning (not constrained by transitive bit). When a router receives an update that contains an optional attribute, the router checks to see if it recognizes it. If it does, then the router should know how to handle it.

If the router does not recognize the attribute, the BGP implementation shoudl look for the transitive bit in the attribute code. Some attributes, although not recognized by the router, _might still be helpful to upstream routers and should be propated_.

## Transitive Attributes

These attributes (called __transitive optional attributes__) are propagated even when they are not recognized. If a router propagates an unknown transitive optional attribute, it sets an extra bit in the attribute header. This bit is called the __partial bit__. The partial bit indicates that at least one of the routers in the path did not recognize the meaning of a transitive optional attribute.

Other attributes, called __nontransitive optional attributes__, might be of no value to upstream routers if a router earlier in the path does not recognize them. Routers will drop these attributes if they are not recognzied.

### Nontransitive Attributes

* MED

     + Discriminates between multiple entry points to a single AS

### Transitive Attributes

* Aggregator

     +  Specifies IP address and AS number of the router that performed route aggregation

* Community

     + Used for route tagging

One of the nontransitive attributes is the MED attribute, which also influences the BGP route selection process. Whenever there are several links between two adjacent autonomous systems, on AS can use the MED attribute to tell another AS to prefer one of the links for specific destinations.

### Tansitive Optional Attributes

* __Aggregator__: This attribute identifies the AS and the router within that AS that created a route summarization, or aggregate.
* __Community__: This attribute is a numerical value that can be attached to certain routes as they pass a specific point in the network. For filtering or route selection purposes, other routers can examine the commnuity value at different points in the network. BGP configuration may cause routes with a specific community value to be treated differently than others.
