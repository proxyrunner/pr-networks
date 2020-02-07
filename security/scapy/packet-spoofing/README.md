# Packet Spoofing with Scapy

Hey folks. This short tutorial will give you a brief introduction into spoofing packets in a network. You will also be able to simultaneously cause a DoS.

## Topology

This is a simple technique consisting of a single host attached to a /24 network switch.

![Packet Spoofing Lab]()

## Getting Started

First you'll need to validate you have an IP address. In this case I assigned a static IP address to my host:

![IP Address Assignment]()

### Validate connectivity

Now that you've assigned an IP address. Use ping to test your network connectivity:

![Ping test]()

## Creating your packet on Scapy