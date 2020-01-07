# ASA Objects

## What are Objects?

* Objects and Object-Groups are used to identify networks or services
* Objects can only have one entry inside it
* Object-groups can have multiple entries inside it
* There are two type of Objects that you can create

    1. Network
    2. Services

* There are six types of Object-Groups that you can create

    1. Network
    2. Service
    3. Protocol
    4. User
    5. ICMP-type
    6. Security

## Configuring Objects

### Example 1 - A PC

```
object network 0-PC
    host 192.168.0.100
```

### Example 2 - An entire subnet

```
object network 0-Subnet
    subnet 192.168.0.0 255.255.255.0
```

### Example 3 - An entire network

```
object network 0-Range
    range 192.18.0.1 192.168.0.10
```

## Configuring Objects Continued…

### Example 4 - A service

```
object service 0-telnet
    service tcp destination eq telnet
```

### Example 5 - A protocol

```
object service 0-dns
    service udp destination eq domain
```

### Example 6 - A source port

```
object service 0-SourcePort
    service tcp source eq 1234
```

## Configuring Object Groups

### Example 1 - A group of subnets

```
object-group network OG-Subnet
    network-object 192.168.0.0 255.255.255.0
    network-object  192.168.1.0 255.255.255.0
```

### Example 2 - A group of hosts

```
object-group network OG-Hosts
    network-object host 10.0.0.1
    network-object host 10.0.0.2
```

### Example 3 - and group os hosts and Subnets

```
object-group network OG-Hosts_and_Subnets
    network-object host 10.0.0.1
    network-object 192.168.0.0 255.255.255.0
```

## Configuring Object-Groups Continued

### Example 4

```
object-group service OG-Telnet_DNS
    service-object tcp destination eq telnet
    service-object udp destination eq domain
```

* Access-lists are used to define permissions for traffic flow
* You can create two kinds of Access-lists
	1. Interface-based
	2. Global
* Interface-Based ACL's take precendence over Global ACL's
	
## Order of check for ACLs

1. Match traffic usin Interface-Based ACL. If no match, then move to Step 2
2. Match traffic using Global ACL. If no match, then move to step 3
3. Match traffic using Adaptive Security Algorithm

All traffic from higher security-level to lower security-level is permitted and all traffic from lower security-level to higher security-level is denied by default

## Configuring Interface-Based-ACL

### Example 1

```
access-list OUT_IN extended permit tcp any host 10.0.0.1 eq telnet
```

### Example 2

```
access-list OUT_IN extended permit tcp any 192.168.0.0 255.255.255.0 eq telnet
```

### Example 3

```
access-list OUT_IN extended permit tcp any object O-PC eq telnet
```

### Example 4

```
access-list OUT_IN extended permit object 0-telnet any object 0-Subnet
```

### Example 5

```
access-list OUT_IN extended permit tcp any object-group OG-Hosts_and_Subnets eq telnet
```

## Configuring Interface-Based ACL

### Example 6

```
access-list OUT_IN extended permit object-group OG-Telnet_DNS any object-group OG-Hosts_and_Subnets
```

## Applying ACL to an interface

### Examples 1

```
access-group OUT_IN in interface OUTSIDE
```

### Example 2

```
access-group OUT_IN out interface OUTSIDE
```
