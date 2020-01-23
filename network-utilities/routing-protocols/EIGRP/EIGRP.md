# EIGRP

EIGRP doesn't use TCP or UDP. EIGRP uses Cisco's Reliable Transport Protcol (RTP). Not to be confused with Real-time Transport Protocol (RTP), which is a VoIP protocol. It makes sense that EIGRP was proprietary for a long while because of that.

EIGRP runs directly above IP layer as protocol number 88. RTP guarantees an ordered packet delivery, and supports both multicast and unicast traffic.

The multicast address is 224.0.0.10.

Only selected packets are sent reliably, requiring acknowledge upon receipt. For efficiency resons, a multiaccess network  with multicast capabilities, like Ethernet,  will not send every __hello__ packet reliably.