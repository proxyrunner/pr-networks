# EIGRP

## Realiable Transport

EIGRP doesn't use TCP or UDP. EIGRP uses Cisco's Reliable Transport Protcol (RTP). Not to be confused with Real-time Transport Protocol (RTP), which is a VoIP protocol. It makes sense that EIGRP was proprietary for a long while because of that.

EIGRP runs directly above IP layer as protocol number 88. RTP guarantees an ordered packet delivery, and supports both multicast and unicast traffic.

The multicast address is 224.0.0.10.

Only selected packets are sent reliably, requiring acknowledge upon receipt. For efficiency reasons, a multiaccess network  with multicast capabilities, like Ethernet,  will not send every __hello__ packet reliably.

### Review Question

What do ACK packets indicate when exchanging EIGRP updates between routers?

They indicate that the router received the update information, and this acknowledgment is mandatory.

After two routers have exchanged hellos and the neighbor adjacency is established, they exchange ACK packets, indicating that the other side received the update information.

## Configure Timers

```
BR3(config)# interface Serial 0/0
BR3(config-if)# ip hello-interval eigrp 100 10
BR3(config-if)# ip hold-time eigrp 100 30
```

### Validate

```
BR3# show ip eigrp interface detail serial 0/0
EIGRP-IPv4 Interfaces for AS(100)
                              Xmit Queue   PeerQ        Mean   Pacing Time   Multicast    Pending
Interface              Peers  Un/Reliable  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
Se0/0                    1        0/0       0/0        1249       0/15        6235           0
  Hello-interval is 10, Hold-time is 30
<... output omitted ...>
```