# Charming the Python on Nexus 7k Platform

I'm going to shorthand this tutorial's name to CTP so it's less cumbersome to name files.

## Goals

* Scenario 1. Python Interpreter
* Scenario 2. Basic Python Programming
* Scenario 3. Configure interface description using CDP neighbor table
* Scenario 4. Configure interface description based on CDP XML elements
* Scenario 5. Configure IPv6 addresses and BGPv6 protocol

## Cisco Module

### 'cli()' API

This will execute CLI commands from your Python interpreter, notice the control/special characters.

```python
CiscoLive_N7K# >>> cli("show hostname")
'CiscoLive_N7K \n'
CiscoLive_N7K# >>> cli("show vlan")
'\nVLAN Name                             Status    Ports\n---- -------------------------------- --------- -------------------------------\n1    default                          active    Eth3/1, Eth3/2, Eth3/3, Eth3/4\n                                                Eth3/5, Eth3/6, Eth3/7, Eth3/8\n                                                Eth3/9, Eth3/10, Eth3/11\n                                                Eth3/12, Eth3/13, Eth3/14\n                                                Eth3/15, Eth3/16, Eth3/17\n                                                Eth3/18, Eth3/19, Eth3/20\n                                                Eth3/21, Eth3/22, Eth3/23\n                                                Eth3/24, Eth3/25, Eth3/26\n                                                Eth3/27, Eth3/28, Eth3/29\n                                                Eth3/30, Eth3/31, Eth3/32\n                                                Eth3/33, Eth3/34, Eth3/35\n                                                Eth3/36, Eth3/37, Eth3/38\n                                                Eth3/39, Eth3/40, Eth3/41\n                                                Eth3/42, Eth3/43, Eth3/44\n                                                Eth3/45, Eth3/46, Eth3/47\n                                                Eth3/48, Eth4/1, Eth4/2, Eth4/3\n                                                Eth4/4, Eth4/5, Eth4/6, Eth4/7\n                                                Eth4/8, Eth4/9, Eth4/10, Eth4/11\n                                                Eth4/12, Eth4/13, Eth4/14\n                                                Eth4/15, Eth4/16, Eth4/17\n                                                Eth4/18, Eth4/19, Eth4/20\n                                                Eth4/21, Eth4/22, Eth4/23\n                                                Eth4/24, Eth4/25, Eth4/26\n                                                Eth4/27, Eth4/28, Eth4/29\n                                                Eth4/30, Eth4/31, Eth4/32\n                                                Eth4/33, Eth4/34, Eth4/35\n                                                Eth4/36, Eth4/37, Eth4/38\n                                                Eth4/39, Eth4/40, Eth4/41\n                                                Eth4/42, Eth4/43, Eth4/44\n                                                Eth4/45, Eth4/46, Eth4/47\n                                                Eth4/48\n\nVLAN Type         Vlan-mode\n---- -----        ----------\n1    enet         CE     \n\nRemote SPAN VLANs\n-------------------------------------------------------------------------------\n\nPrimary  Secondary  Type             Ports\n-------  ---------  ---------------  -------------------------------------------\n\n\n\n'
CiscoLive_N7K# >>> 
```

### 'clip()' API

The _clip()_ API outputs directly to stdout and returns nothing to Python, but is more readable.

```python
CiscoLive_N7K# >>> clip("show hostname")
CiscoLive_N7K 
CiscoLive_N7K# >>> clip("show vlan")

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Eth3/1, Eth3/2, Eth3/3, Eth3/4
                                                Eth3/5, Eth3/6, Eth3/7, Eth3/8
                                                Eth3/9, Eth3/10, Eth3/11
                                                Eth3/12, Eth3/13, Eth3/14
                                                Eth3/15, Eth3/16, Eth3/17
                                                Eth3/18, Eth3/19, Eth3/20
                                                Eth3/21, Eth3/22, Eth3/23
                                                Eth3/24, Eth3/25, Eth3/26
                                                Eth3/27, Eth3/28, Eth3/29
                                                Eth3/30, Eth3/31, Eth3/32
                                                Eth3/33, Eth3/34, Eth3/35
                                                Eth3/36, Eth3/37, Eth3/38
                                                Eth3/39, Eth3/40, Eth3/41
                                                Eth3/42, Eth3/43, Eth3/44
                                                Eth3/45, Eth3/46, Eth3/47
                                                Eth3/48, Eth4/1, Eth4/2, Eth4/3
                                                Eth4/4, Eth4/5, Eth4/6, Eth4/7
                                                Eth4/8, Eth4/9, Eth4/10, Eth4/11
                                                Eth4/12, Eth4/13, Eth4/14
                                                Eth4/15, Eth4/16, Eth4/17
                                                Eth4/18, Eth4/19, Eth4/20
                                                Eth4/21, Eth4/22, Eth4/23
                                                Eth4/24, Eth4/25, Eth4/26
                                                Eth4/27, Eth4/28, Eth4/29
                                                Eth4/30, Eth4/31, Eth4/32
                                                Eth4/33, Eth4/34, Eth4/35
                                                Eth4/36, Eth4/37, Eth4/38
                                                Eth4/39, Eth4/40, Eth4/41
                                                Eth4/42, Eth4/43, Eth4/44
                                                Eth4/45, Eth4/46, Eth4/47
                                                Eth4/48

VLAN Type         Vlan-mode
---- -----        ----------
1    enet         CE     

Remote SPAN VLANs
-------------------------------------------------------------------------------

Primary  Secondary  Type             Ports
-------  ---------  ---------------  -------------------------------------------
```

### 'clid()' - For CLI commands that support XML

For CLI commands that support XML the ‘clid()’ API returns outputs as a Python dictionary.

```
CiscoLive_N7K# >>> clid("show hostname")
{'hostname': 'CiscoLive_N7K'}
```

#### More examples with 'clid()'

```python
CiscoLive_N7K# >>> clid("show hostname")
{'hostname': 'CiscoLive_N7K'}
CiscoLive_N7K# >>> hostname = clid("show hostname")
CiscoLive_N7K# >>> type(hostname)
<type 'dict'>
CiscoLive_N7K# >>> hostname
{'hostname': 'CiscoLive_N7K'}
CiscoLive_N7K# >>> 
CiscoLive_N7K# >>> hostname.values()
['CiscoLive_N7K']
CiscoLive_N7K# >>> hostname.keys()
['hostname']
CiscoLive_N7K# >>> hostname.items()
[('hostname', 'CiscoLive_N7K')]
CiscoLive_N7K# >>> cli("conf t ; hostname somethingelse")
''
somethingelse(config)# 
somethingelse(config)# >>> 
somethingelse(config)# >>> 
somethingelse(config)# >>> 
somethingelse(config)# >>> cli("hostname CiscoLive_N7K")
''
CiscoLive_N7K(config)# cli("exit")
''
CiscoLive_N7K# >>> 
```

