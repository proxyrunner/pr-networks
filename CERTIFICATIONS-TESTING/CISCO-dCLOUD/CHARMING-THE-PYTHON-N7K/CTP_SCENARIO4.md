# Scenario Interface Description

Scenario 4. Configure interface description based on CDP XML elements
In this section, you will use Python to configure interface descriptions using the CDP table XML element tree.

## Steps

Configure interface description based on CDP XML elements

1. Review the XML tree data structure and the hierarchy and element names. The XML namespace is assigned to xmlns.

```
>>> from cisco import *
>>> import xml.etree.cElementTree as etree
>>> cdp_dict = dict()
>>> print cdp_dict.items()
[]
>>> cdp_xml = cli("show cdp neighbor | xml | exclude ']]>]]'")
>>> print cdp_xml
>>> xml_namespace = "{http://www.cisco.com/nxos:1.0:cdpd}"
>>> root = etree.fromstring(cdp_xml)
>>> print root.tag
```

2. Using the XML namespace and an element as a starting point, you can iterate and extract specific data. The CDP neighbor table info is assigned specific XML element names such as ‘device_id’, ‘intf_id’ and ‘port_id’.

```
>>> for element in root.iter(xml_namespace + 'ROW_cdp_neighbor_brief_info'):
... neighbor = element.find(xml_namespace + 'device_id').text
... local_intf = element.find(xml_namespace + 'intf_id').text
... remote_intf = element.find(xml_namespace + 'port_id').text
... if neighbor not in cdp_dict:
... cdp_dict[neighbor] = {}
... cdp_dict[neighbor]['local_intf'] = [local_intf]
... cdp_dict[neighbor]['remote_intf'] = [remote_intf]
... elif local_intf not in cdp_dict[neighbor]['local_intf']:
... cdp_dict[neighbor]['local_intf'].append(local_intf)
... cdp_dict[neighbor]['remote_intf'].append(local_intf)
...
>>>
```

3. Assign the neighbor and associated local and remote interfaces into a nested dictionary.

```
>>> print cdp_dict.items()
[('N7K_2(TB3EB2EEBDB)', {'local_intf': ['Ethernet2/2', 'Ethernet2/3', 'Ethernet2/4', 'Ethernet2/5'],
'remote_intf': ['Ethernet2/2', 'Ethernet2/3', 'Ethernet2/4', 'Ethernet2/5']}),
('R101 ', {'local_intf': ['Ethernet2/1'], 'remote_intf': ['GigabitEthernet0/1']})]
4. Now configure a description on all local interfaces using XML data.
>>> for key, value in cdp_dict.items():
... neighbor = " connected to " + key + "'s"
... for item in range(len(value['local_intf'])):
... local_intf = " local intf " + value['local_intf'][item]
... remote_intf = " remote intf " + value['remote_intf'][item]
... cli("conf t ; interface " + value['local_intf'][item])
... cli("description " + local_intf + neighbor + remote_intf + " (via XML)")
... cli("end")
...
>>>
```

5. Confirm interface description configured is using the CDP information.

```
# show run int eth2/1-5 | in interface|description
!Command: show running-config interface Ethernet2/1-5
interface Ethernet2/1
description local intf Ethernet2/1 connected to R101 's remote intf GigabitEthernet0/1 (via XML)
interface Ethernet2/2
description local intf Ethernet2/2 connected to N7K_2(TB3EB2EEBDB)'s remote intf Ethernet2/2 (via XML)
interface Ethernet2/3
description local intf Ethernet2/3 connected to N7K_2(TB3EB2EEBDB)'s remote intf Ethernet2/3 (via XML)
interface Ethernet2/4
description local intf Ethernet2/4 connected to N7K_2(TB3EB2EEBDB)'s remote intf Ethernet2/4 (via XML)
interface Ethernet2/5
description local intf Ethernet2/5 connected to N7K_2(TB3EB2EEBDB)'s remote intf Ethernet2/5 (via XML)
```