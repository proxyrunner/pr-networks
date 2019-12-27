# Distribute Lists

* Control redistribution using ACLs or Prefix Lists
* ACL defines which subnet will be redistributed or denied into the target protocol

## Simple Configuration

```
R3(config)# access-list 7 permit 10.10.11.0 0.0.0.255
R3(config)# access-list 7 permit 10.10.12.0 0.0.0.255
R3(config)# router ospf 10
R3(config-router)# redistribute eigrp 100
R3(config-router)# distribute-list 7 out eigrp 100
```

The distribute-list 7 out eigrp 100 command defines that prefixes matched by access list 7 will be redistributed from EIGRP with AS 100 to the OSPF routing process.