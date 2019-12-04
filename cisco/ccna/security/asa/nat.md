# Network Address Translation

## Mastering the Fundamentals

* RFC 1631
* Layer 3 forwarding device to provide address simplification and conservation.
* Most commonly used to connect private LANs to the internet.
* You can configure NAT using only one address for the entire network to the outside world.

Cisco's NAT terms:

* __Inside local address:__ The IPv4 address that is assigned to a host on the inside network. The inside local address is likely to be one that falls within the RFC 1918 reserved private IPv4 address space.
* __Inside globl address:__ A globally routable IPv4 address that represents one or more inside local IPv4 addresses to the outside world.
* __Ouside local address:__ The IPv4 address of an outside host as it appears to the inside network. Not necessarily a public address, the outside local address is allocated from a routable address space.
* __Ouside global address:__ The IPv4 address that is assigned to a host on the outside network by the host owner. The outside global address is allocated from a globally routable address or network space. 

## Configuring NAT on Cisco ASA

### Network Object NAT

* NAT as parameter of a network object
* Quick and easy
* Mapped address specified for object

* Static NAT
* Dynamic NAT
* PAT

* Policy NAT

### The NAT Tables

* __Manual NAT__ (first section): The manual NAT section enables the administrator to define translations that the appliance compares before the other two sections. 
    * These translations are usually very precise. 
        + They can include translation on both the source and destination IP addresses, requiring the connection to be to a specific destination for the rule to match.

* __Auto NAT__ (second section): The auto NAT section, _also referred to as object NAT_, contains translations that are defined in the object itself. This section allows each object definition to include a single translation for every object that is configured. 
    * These translations are usually static translations for servers that have clients connecting to them from the Internet or are dynamic translations for clients connecting to the Internet.

* __Manual NAT__ after auto NAT (third section): The manual NAT section that comes after the auto NAT section contains more general translations that are not handled by the sections above. 
    *Translations in the manual NAT section are used only when a connection fails to match any entries in the first two sections.

__\* If no translation is found in the NAT table, the packet is forwarded without a translation, according to any applied access rules.__



## Examples of NAT Verification

```
# show xlate
3 in use, 3 most used
Flags: D - DNS, e - extended, I - identity, i - dynamic, r - portmap,
       s - static, T - twice, N - net-to-net
NAT from dmz:172.16.1.50 to outside:192.168.1.100
    flags s idle 15:34:04 timeout 0:00:00

NAT from inside:10.1.1.50 to outside:192.168.2.144 flags i idle 0:02:51 timeout 3:00:00
NAT from inside:10.1.1.10 to outside:192.168.2.177 flags i idle 0:05:22 timeout 3:00:00
TCP PAT from inside:10.1.1.50/59782 to outside:192.168.1.1/59782 flags ri idle 0:00:54 timeout 0:00:30
TCP PAT from inside:10.1.1.10/1116 to outside:192.168.1.1/1116 flags ri idle 0:01:17 timeout 0:00:30
```

```
# show nat
Manual NAT Policies (Section 1)
1 (dmz) to (Partner_Network) source dynamic DMZ_Network 172.18.1.11_PAT destination static 172.16.1.0_network 172.17.1.0_network
    translate_hits = 4, untranslate_hits = 19

Auto NAT Policies (Section 2)
1 (dmz) to (outside) source static DMZ-Server 192.168.1.11
    translate_hits = 12956, untranslate_hits = 2523
2 (inside) to (outside) source dynamic 10.0.1.0_network interface
    translate_hits = 1204, untranslate_hits = 3061

Manual NAT Policies (Section 3)
1 (any) to (outside) source dynamic 10.0.0.0_Private 192.168.1.8_outside
    translate_hits = 4728, untranslate_hits = 92837
```

## Basic Configurations

```
Interface GigabitEthernet0/2
    no shutdown
    nameif dmz
    security-level 50
    ip address 172.16.1.1 255.255.255.0
Interface GigabitEthernet0/3
    no shutdown
    nameif outside
    security-level 0
    ip address 192.168.1.1 255.255.255.0
```
