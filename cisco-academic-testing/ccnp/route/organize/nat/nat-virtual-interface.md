# NAT Virtual Interface (NVI)

As of Cisco IOS Software version 12.3(14)T, Cisco introduced a new feature that is called NAT Virtual Interface, which removes the requirement to configure an interface as inside or outside.

Introducing NVI:

    No need to identify inside and outside interfaces

    Different order of operation

Example configuration:

Router(config)# access-list 10 permit 192.168.10.0 0.0.0.255
Router(config)# ip nat source list 10 interface Ethernet 0/1 overload
Router(config)# interface Ethernet 0/0
Router(config-if)# ip nat enable
Router(config)# interface Ethernet 0/1
Router(config-if)# ip nat enable

NVI removes the requirements to configure an interface as either inside or outside. Also, the NAT order of operations is slightly different with NVI. Classic NAT first performs routing and then translates the addresses when going from an inside interface to an outside interface, and vice versa when traffic flow is reversed. NVI, however, performs routing, translation, and then routing again. NVI performs the routing operation twice, before and after translation, before forwarding the packet to an exit interface, and the whole process is symmetrical. Because of the added routing step, packets can flow from an inside to an inside interface, in classic NAT terms, which would fail if classic NAT was used.

To configure interfaces to use NVI, use the ip nat enable interface configuration command.