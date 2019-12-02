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
