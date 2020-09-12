# Scenario mBGP

Configure IPv6 addresses and BGPv6 protocol
In this section, you will use Python to generate IPv6 addresses by converting existing IPv4 decimal addresses into hexadecimal, and then configure IPv6 addresses on the interfaces. You will also deploy a BGPv6 configlet on the Nexus node using Python to complete the IPv6 routing requirement.

## Steps

Configure IPv6 addresses and BGPv6 protocol

1. Import the convertipv4 module to use the getIPv6 method. Review the XML tree data structure and the hierarchy and element names. The XML namespace is assigned to xmlns.

```
>>> from cisco import *
>>> from convertipv4 import getIPv6
>>> import xml.etree.cElementTree as etree
>>> intf_brief_dict = dict()
>>> print intf_brief_dict.items()
[]
>>> intf_brief_xml = cli("show ip int brief | xml | exclude ']]>]]'")
>>> print intf_brief_xml
>>> xml_namespace = "{http://www.cisco.com/nxos:1.0:ip}"
>>> root = etree.fromstring(intf_brief_xml)
>>> print root.tag
```

2. Using the XML namespace and an element as a starting point, you can iterate and extract specific data. Use the getIPv6 method to convert the IPv4 address.

```
>>> for element in root.iter(xml_namespace + 'ROW_intf'):
... prefix = element.find(xml_namespace + 'prefix').text
... intf_name = element.find(xml_namespace + 'intf-name').text
... if intf_name not in intf_brief_dict:
... intf_brief_dict[intf_name] = {}
... intf_brief_dict[intf_name]['IPv4'] = prefix
... intf_brief_dict[intf_name]['IPv6'] = getIPv6(prefix)
...
>>> print sorted(intf_brief_dict.items())
[('Eth2/1', {'IPv4': '192.168.101.1', 'IPv6': '2001::c0a8:6501'}), ('Eth2/2', {'IPv4': '10.2.2.1', 'IPv6': '2001::0a02:0201'}), ('Eth2/3', {'IPv4': '10.2.3.1', 'IPv6':
'2001::0a02:0301'}), ('Eth2/4', {'IPv4': '10.2.4.1', 'IPv6': '2001::0a02:0401'}), ('Eth2/5', {'IPv4': '10.2.5.1', 'IPv6': '2001::0a02:0501'}), ('Lo701', {'IPv4': '10.7.0.1', 'IPv6': '2001::0a07:0001'})]
```

3. Now configure IPv6 address on all IPv4 interfaces, using the cli() API. The loopback701 and Eth2/1-5 interfaces should all have IPv6 addresses configured. The IPv6 routing table now has directly attached routes, and is learning the Loopback702 ipv6 address on N7K_2 via ospfv3.

```
>>> for key, value in intf_brief_dict.items():
... intf = key
... ipv6_addr = value['IPv6']
... if 'Lo' in intf:
... ipv6_mask = '/128'
... else:
... ipv6_mask = '/126'
... cli("conf t ; interface " + key)
... cli("ipv6 address " + ipv6_addr + ipv6_mask)
... cli("end")
...
>>> clip("show ipv6 int brief")
>>> clip("show ipv6 route")
```

4. A bgpv6_configlet.txt file that contains the required BGPv6 configuration was created in the bootflash:scripts directory. Open and read the file and put into a list.

```
# show file bootflash:scripts/bgpv6_configlet.txt
>>> bgpv6_file = open("/bootflash/scripts/bgpv6_configlet.txt", 'r')
>>> bgpv6_config = bgpv6_file.read().split("\n")
>>> print bgpv6_config
>>> print bgpv6_config[0]
>>> type(bgpv6_config)
```

5. Change the interpreter prompt into configuration mode. Iterate over each line in the list and configure the BGPv6 protocol. Confirm BGPv6 peering is up and you are receiving ipv6 routes.

```
>>> cli("conf t")
(config) # >>> for item in bgpv6_config:
(config) # ... print item
(config) # ...
(config) # >>> for item in bgpv6_config:
(config) # ... cli(item)
(config) # ...
(config-router-neighbor-af) # >>> cli(”end")
>>>
>>> clip("show run bgp")
>>> clip("show bgp ipv6 unicast summary")
>>> clip("show ipv6 route")
```