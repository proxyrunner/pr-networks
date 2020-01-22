# Configuring Redistribution

Redistribution is a trickier topic on the Cisco exams. It appears in the CCNA topics but isn't fully embraced until you're well into the professional level topics.

There are several techniques used in controlling routing updates. The first we'll  review are _distribute lists_.

## Distribute Lists

 _Distribute lists_ allow you to apply a classic ACL to routing updates. It is the simplest to configure, but has some limitations. An immediate warnining I must indicate is as follows:

```
R1(config-router)#distribute-list NAMED-TEST in
Access-list type conflicts with prior definition
% This command only accepts named standard IP access-lists.
R1(config-router)#
```

As you can see, you can only configure __standard__ named ACLs on inbound or outbound distribute-lists. Another important factor is that classic ACLs do not affect traffic that is originated from the route, so applying one to an interface has no effect on the outgoing routing advertisements.

