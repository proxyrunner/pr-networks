# Cisco's Nexus Platform

Cisco Nexus Operating System (NX-OS) does not support PAgP for port channels.

## LAN Port Channel Modes

Several port channel modes are available that must be configured to correspond between devices. Some combinations of port modes are supported; others are not. The following table lists the channel modes.

* Passive (LACP)
    *  Responds to LACP packets that it receives
    * Does not initiate LACP negotiation
* Active (LACP)
    * Initiates negotiations with other ports by sending LACP packets
* On (Static)
    * Does not send any LACP packets
    * Does not join any LACP channel groups
    * Becomes an individual link with that interface

Note: You must enable the LACP feature before you can configure and use LACP functions.

| Channel Mode | Passive | Active | On |
|:-:|:-:|:-:|:-:|
|Passive|—|OK|—|
|Active|OK|OK|—|
|On|—|—|OK|