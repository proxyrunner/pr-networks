# BGP - Border Gateway Protocol

## External Neighbors

### Prequisites

* BGP ASN
* Router configuration mode

```
neighbor ip-address 1.1.2.2 remote-as 64513
neighbor ip-address description EXTERNAL NEIGHBOR [IP] - [ASN NAME] - [ASN #]
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
