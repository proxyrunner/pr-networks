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

## Further Research

You may also consider [data center style EtherChannel, better known as VPC](../DATA-CENTER/NX-OS/VPC.md)

## L2 Etherchannel Configuration

* ports must match

``` L2 CONFIGURATION
# PRIVILEGED EXEC MODE
# SELECT INTERFACE
!
interface range gig 3/3 , gig 3/2
!
# INTERFACE CONFIG MODE
!
speed auto 
!
duplex auto
!
# mdix auto
!
# CREATE PORT-CHANNEL GROUP
!
channel-group 1 mode on
!
no shut
!
exit
!
# SAME AS LAYER 2 INTERFACE
!
int port-channel 1
!
switchport trunk encapsulation dot1q
!
switchport mode trunk
!
no shut
!
end
!
```

## L3 Etherchanel Configurations

* ports must match

```
# PRIVILEGED EXEC MODE
# SELECT INTERFACE
!
interface range gig 5/0 , gig 6/0
!
# INTERFACE CONFIG MODE
!
# REMOVE LAYER 2
# no switchport
#
channel-group 1
!
no shut
!
exit
!
# Remember to make the port channel a routed 
# interface as well.
!
int port-channel 1
!
# ip address 10.0.250.254 255.255.255.0
!
end
!
```

## Port-Channel L2/L3 Show Commands and Validation

### How to Select a Port-Channel

#### L2

Notice channel-group for L2 is higher than in routers

> channel-group ?

```
## SELECT PORT-CHANNEL NUMBER
##  MAX NUMBER IS 255

LAN1-DIST-A(config-if)#channel-group ?   
  <1-255>  Channel group number
  auto     Enable LACP auto on this interface
```

#### L3

```
LAN1-WAN-A(config-if-range)#channel-group ?
  <1-64>  Channel group number

LAN1-WAN-A(config-if-range)#channel-group 1 ?
  <cr>

LAN1-WAN-A(config-if-range)#channel-group 1 

%Interface MTU set to channel-group MTU 1500.

GigabitEthernet1/0 added as member-1 to port-channel1
 
%Interface MTU set to channel-group MTU 1500.

%Interface MTU set to channel-group MTU 1500.

GigabitEthernet0/0 added as member-2 to port-channel1
```

### How to Select Port-Channel Mode

> channel-group 1 mode ?

```
## DESIGNATE PORT-CHANNEL MODE

LAN1-DIST-B(config-if-range)#channel-group 1 mode ?                 
  active     Enable LACP unconditionally
  auto       Enable PAgP only if a PAgP device is detected
  desirable  Enable PAgP unconditionally
  on         Enable Etherchannel only
  passive    Enable LACP only if a LACP device is detected

LAN1-DIST-B(config-if-range)#channel-group 1 mode on
```

### Verify Port-Channel interfaces

> show etherchannel summary 

```
## VERIFY PORT-CHANNEL

LAN1-DIST-A#show etherchannel summary 
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      N - not in use, no aggregation
        f - failed to allocate aggregator

        M - not in use, minimum links not met
        m - not in use, port not aggregated due to minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)          -        Gi3/2(P)    Gi3/3(P)    

LAN1-DIST-A#
```