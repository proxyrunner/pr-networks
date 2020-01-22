# NAT

## Static NAT

```
Router(config)# interface Ethernet 0/1
Router(config-if)# ip address 209.165.201.1 255.255.255.240
Router(config-if)# ip nat outside
Router(config-if)# exit
Router(config)# interface Ethernet 0/0
Router(config-if)# ip address 172.16.1.1 255.255.255.0
Router(config-if)# ip nat inside
Router(config-if)# exit
Router(config)# ip nat inside source static 172.16.1.10 209.165.201.5
```

## Dynamic NAT

```
Router(config)# access-list 1 permit 172.16.1.0 0.0.0.255
Router(config)# ip nat pool NAT-POOL 209.165.201.5 209.165.201.10 netmask 255.255.255.240
Router(config)# interface Ethernet 0/1
Router(config-if)# ip address 209.165.201.1 255.255.255.240
Router(config-if)# ip nat outside
Router(config-if)# exit
Router(config)# interface Ethernet 0/0
Router(config-if)# ip address 172.16.1.1 255.255.255.0
Router(config-if)# ip nat inside
Router(config-if)# exit
Router(config)# ip nat inside source list 1 pool NAT-POOL
```

## PAT

```
Router(config)# access-list 1 permit 172.16.1.0 0.0.0.255
Router(config)# interface Ethernet 0/0
Router(config-if)# ip address 172.16.1.1 255.255.255.0
Router(config-if)# ip nat inside
Router(config-if)# interface Ethernet 0/1
Router(config-if)# ip address 209.165.201.1 255.255.255.240
Router(config-if)# ip nat outside
Router(config-if)# exit
Router(config)# ip nat inside source list 1 interface Ethernet 0/1 overload
```

## NAT Virtual Interface

```
Router(config)# access-list 10 permit 192.168.10.0 0.0.0.255
Router(config)# ip nat source list 10 interface Ethernet 0/1 overload
Router(config)# interface Ethernet 0/0
Router(config-if)# ip nat enable
Router(config)# interface Ethernet 0/1
Router(config-if)# ip nat enable
```
