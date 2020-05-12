# Dynamic Multipoint VPN - DMVPN

## Hub Configuration

```
conf t
interface Tunnel0
ip address 10.0.0.2 255.255.255.0
no ip redirects
ip mtu 1400
ip nhrp map multicast dynamic
ip nhrp network-id 99
ip tcp adjust-mss 1360
tunnel source Gig0/0
tunnel mode gre multipoint
tunnel key 99
end
```

## Default Spoke Tunnel Config

```
conf t
int tun 0
ip add 10.0.0.1 255.255.255.0
ip nhrp map multicast 1.1.2.2
ip nhrp map 10.0.0.1 1.1.2.2
ip nhrp network-id 99
ip nhrp nhs 10.0.0.1
tunne source gig 0/0
tunnel destin 1.1.2.2
tunnel key 99
end
```
