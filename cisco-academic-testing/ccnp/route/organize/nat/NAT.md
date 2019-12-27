# The dreaded NAT

## Static NAT

Static NAT is a one-to-one mapping between an inside address and an outside address. It allows external devices to initiate connections to internal devices. 

This implementation is especially useful when you want to provide access to the servers of a company, for example, a web server. In this case, you map an inside local address of the server to an inside global address through which the server is reachable.

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