# Cisco's Adaptive Security Appliance or ASA

Cisco ASA software is one of the best and most classical firewall out there. To put it simply, an ASA comes out-of-the-box with everything secure, so nothing will traverse through it without a whitelist.

Contrary to many popular introductory tutorials, Layer-3 connectivity can be established as long as the following criteria is met:

* the IP address is reachable (routable,switched)
* an ACL and access-group statement is configured.

I say this because many times, I'll find a great tutorials with extraneous configurations for say, DNS. Now don't get me wrong! Configuring DNS is an extremely important part in securing your ASA, but not pertinent with our fundamental task right now, __getting started__.

```
# ACCESS-LIST CONFIGURATION
access-list TEST1 extended permit ip any any
# ACCESS-GROUP 
access-group TEST1 in interface OUTSIDE
```

Now these few statements should __never, ever__ go into a production firewall. The first statement allows __all connectivity__, and the second command initiates the flow of traffic from the _OUTSIDE_ to the _INSIDE_.