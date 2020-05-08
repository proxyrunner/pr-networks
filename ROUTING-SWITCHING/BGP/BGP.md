# BGP - Border Gateway Protocol

## External Neighbors

### Prequisites

* BGP ASN
* Router configuration mode

```md
neighbor *'ip-address'* remote-as _autonomous-system-number_
neighbor *'ip-address'* description _EXTERNAL NEIGHBOR [IP] - [ASN NAME] - [ASN #]_
```

Example:

```
configure terminal
router bgp 64512
neighbor 1.1.2.2 remote-as 64513
neighbor 1.1.2.2 description EXTERNAL NEIGHBOR 1.1.2.2 - verizon datacenter - AS64513
```

### Shutdown External Neighbor

```
neighbor ip-address shutdown
```

Example:

```
neighbor 1.1.2.2 shutdown
```
