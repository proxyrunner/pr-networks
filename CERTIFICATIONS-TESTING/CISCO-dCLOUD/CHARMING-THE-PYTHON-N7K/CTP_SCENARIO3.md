# Scenario CDP

Scenario 3. Configure interface description using CDP neighbor table

In this section, you will use Python to configure interface descriptions using the information from the CDP table.

## Steps

Configure interface description using CDP neighbor table

1. Using the CLI API we will capture the output of the CDP table. We only need the specific neighbor information. So we will start to remove unnecessary lines of data. When for-loop completes it will display which items were popped. The 1st six lines are removed.

```python
from cisco import *
import pprint

cdp_dict = dict()
print cdp_dict.items()[]
cdp_table = cli("show cdp neighbor").strip().split("\n")
print cdp_table
pprint.pprint(cdp_table)
cdp_table[0]
cdp_table[-1]
for iter in range(6):
cdp_table.pop(0)
...

```

2. Create cdp_list1, using list comprehension, to add each cdp_table line as an individual list within cdp_list1. Use split() to split items within each list. Create cdp_list2 and only add cdp_list1 items that are not empty.

```
 pprint.pprint(cdp_table)
 cdp_list1 = [line.split() for line in cdp_table]
 pprint.pprint(cdp_list1)
 cdp_list2 = [item for item in cdp_list1 if item != []]
 pprint.pprint(cdp_list2)
[['R101 '],
['Eth2/1', '144', 'R', 'B', 'IOSv', 'Gig0/1'],
['N7K_2(TB3EB2EEBDB)'],
['Eth2/2', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/2'],
['N7K_2(TB3EB2EEBDB)'],
['Eth2/3', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/3'],
['N7K_2(TB3EB2EEBDB)'],
['Eth2/4', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/4'],
['N7K_2(TB3EB2EEBDB)'],
['Eth2/5', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/5'],
['Total', 'entries', 'displayed:', '5']]
```

3. CDP neighbors with large names need to be inserted in the next line and then removed. Also notice there is a list starting with ['Total'...] at the end of the output which must be removed.

```
 for item in cdp_list2:
... item_location = cdp_list2.index(item)
... if len(item) == 1:
... cdp_list2[item_location + 1][0:0] = item
... cdp_list2.pop(item_location)
... elif 'Total' in item:
... cdp_list2.pop(item_location)
...

 pprint.pprint(cdp_list2)
[['R101 ', 'Eth2/1', '144', 'R', 'B', 'IOSv', 'Gig0/1'],
['N7K_2(TB3EB2EEBDB)', 'Eth2/2', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/2'],
['N7K_2(TB3EB2EEBDB)', 'Eth2/3', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/3'],
['N7K_2(TB3EB2EEBDB)', 'Eth2/4', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/4'],
['N7K_2(TB3EB2EEBDB)', 'Eth2/5', '136', 'R', 'S', 's', 'N7K-C7018', 'Eth2/5']]
```

4. Now add each CDP neighbor into the dictionary cdp_dict as a main key of nested dictionary key:values. Add the local/remote interfaces as the nested dictionary key:values. Make the nested dictionary values of type list, to allow for multiple interfaces to be added.

```
 for item in cdp_list2:
... if item[0] not in cdp_dict.keys():
... cdp_dict[item[0]] = {}
... cdp_dict[item[0]]['local_intf'] = [item[1]]
... cdp_dict[item[0]]['remote_intf'] = [item[-1]]
... elif item[1] not in cdp_dict[item[0]]['local_intf']:
... cdp_dict[item[0]]['local_intf'].append(item[1])
... cdp_dict[item[0]]['remote_intf'].append(item[-1])
...

 print cdp_dict.items()
[('N7K_2(TB3EB2EEBDB)', {'local_intf': ['Eth2/2', 'Eth2/3', 'Eth2/4', 'Eth2/5'], 'remote_intf': ['Eth2/2', 'Eth2/3', 'Eth2/4', 'Eth2/5']}), ('R101 ', {'local_intf': ['Eth2/1'], 'remote_intf': ['Gig0/1']})]
```

5. Now configure a description on all local interfaces, identifying the neighbor and its connected interface. Use the cdp_dict key:value pairs to create the description syntax, and configure using the cli() API.

```
 for key, value in cdp_dict.items():
... neighbor = ' connected to ' + key + "'s"
... for item in range(len(value['local_intf'])):
... local_intf = 'local intf ' + value['local_intf'][item]
... remote_intf = ' remote intf ' + value['remote_intf'][item]
... cli("conf t ; interface " + value['local_intf'][item])
... cli("description " + local_intf + neighbor + remote_intf + " (via screen scraping)")
... cli("end")
...

```

6. Confirm interface description configured is using the CDP information.

```
# show run int eth2/1-5 | in interface|description
!Command: show running-config interface Ethernet2/1-5
interface Ethernet2/1
description local intf Eth2/1 connected to R101 's remote intf Gig0/1 (via screen scraping)
interface Ethernet2/2
description local intf Eth2/2 connected to N7K_2(TB3EB2EEBDB)'s remote intf Eth2/2 (via screen scraping)
interface Ethernet2/3
description local intf Eth2/3 connected to N7K_2(TB3EB2EEBDB)'s remote intf Eth2/3 (via screen scraping)
interface Ethernet2/4
description local intf Eth2/4 connected to N7K_2(TB3EB2EEBDB)'s remote intf Eth2/4 (via screen scraping)
interface Ethernet2/5
description local intf Eth2/5 connected to N7K_2(TB3EB2EEBDB)'s remote intf Eth2/5 (via screen scraping)
```