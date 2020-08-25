# Etherchannel - Port-Channel

Etherchannel groups together multiple physical connections into one logical connection.

## Etherchannel Theory

* Allows higher bandwidth between switches
* provides load-balancing
* create redundant links

* called 802.3AD standard
* people assume its back and forth 'equal-load-balancing'

### Load-Balancing Algorithms

1. DST-IP
2. DST-MAC
3. SRC-DST-IP
4. SRC-DST-MAC
5. SRC-IP
6. SRC-MAP

#### LACP

Link Aggregation Control Protocol

|LACP Channel Mode | On | Passive | Active |
|:-:|:-:|:-:|:-:|
|__On__| Y | X | X |
|__Auto__| X| X | Y |
|__Desirable__| X | Y | Y |

#### PAgP

Port Aggregation Protocol is Cisco's proprietary

| PAgP Channel Mode | On | Auto | Desirable |
|:-:|:-:|:-:|:-:|
|__On__| Y | X | X |
|__Passive__| X| X | Y |
|__Active__| X | Y | Y |

###

## L2 Etherchannel Configuration

* ports must match

```
(config-if-range)# speed auto 
(config-if-range)# duplex auto
(config-if-range)# mdix auto
(config-if-range)# channel-group 1 mode ?
(config)#int port-channel 1
# Can be treated like a L2 interface…
(config-if)# switchport trunk encapsulation dot1q
(config-if)# switchport mode trunk
```

## L3 Etherchanel Configurations

```
(config-if-range)# no switchport
(config-if-range)# channel-group 1 mode on
(config-if-range)# exit

# Remember to make the port channel a routed interface as well.
(config)# int port-channel 1
(config-if)# no switchport
(config-if)# ip address x.x.x.x s.s.s.s
```
