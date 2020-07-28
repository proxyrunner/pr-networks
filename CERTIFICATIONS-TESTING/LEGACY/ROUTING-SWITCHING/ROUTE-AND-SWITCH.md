# Route and Switch

This doc will contain immediate resources that are vital in routing and switching environments.


## Administrative Distance

| Route Source | Default Distance Value|
|:-:|:-:|
| Connected interface | 0 |
| Static Route | 1 |
| EIGRP Summary Route | 5 |
| eBGP | 20 |
| iEIGRP | 90 |
| IGRP | 100 |
| OSPF | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EGP | 140 |
| On Demand Routing (ODR) | 160 |
| External EIGRP | 170 |
| iBGP | 200 |
| Unknown* | 255 | 

\* If the administrative distance is 255, the router does not believe the source of that route and does not install the route into the routing table
