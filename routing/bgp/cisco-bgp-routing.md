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

|:---:|:---:|
| i | Route originated in an IGP | 