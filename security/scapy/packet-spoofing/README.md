# Packet Spoofing with Scapy :incoming_envelope:

Hey folks. This short tutorial will give you a brief introduction into spoofing packets in a network. You will also be able to simultaneously cause a DoS.

## Topology

This is a simple technique consisting of a single host attached to a /24 network switch.

![Packet Spoofing Lab](https://github.com/gil-ryan/grs-networking-public/blob/master/img/topo.PNG)

## Getting Started

First you'll need to validate you have an IP address. In this case I assigned a static IP address to my host:

![IP Address Assignment](https://github.com/gil-ryan/grs-networking-public/blob/master/img/static-assign.PNG)

### Validate connectivity

Now that you've assigned an IP address. Use ping to test your network connectivity:

![Ping test](https://github.com/gil-ryan/grs-networking-public/blob/master/img/ping-switch.PNG)

You should also make youself familiar with Wireshark packet capture to analyze and inspect that you're generating correctly.

![Wireshark Capture of Host-Switch ICMP](https://github.com/gil-ryan/grs-networking-public/blob/master/img/wireshark-capture.PNG)

## Creating your packet on Scapy

Scapy allows you to generate network traffic, the sky is the limit from here. It is built in Python so the fundamentals remain the same

![Scapy Commands](https://github.com/gil-ryan/grs-networking-public/blob/master/img/scapy-atk.PNG)

In this picture I'm assigning the parameters to variable _packet_. It's important to take another PCAP to validate that Scapy is working, we can see here that our source address is correctly being generated as _1.2.3.4_, as opposed to the host's static IP, _10.161.0.69_.

![Validate the spoofed traffic](https://github.com/gil-ryan/grs-networking-public/blob/master/img/spoofed-packet.PNG)

Finally, we take the _packet_ variable, and multiply it to instruct Scapy to send as many copies as the product of our new variable:

![Test DoS Attack](https://github.com/gil-ryan/grs-networking-public/blob/master/img/testdos.PNG)

And there we have it! Traffic that has been spoofed from host address _10.161.0.69_ to _1.2.3.4_.

