# Cisco DevNet Python Development

This directory is not exclusive to Python. However, Python is the recommended tool due to its nature in administration.

## On-box vs. Off-box

We shall always start by considering appropriate image versions.

### Python Automation Benefits

#### NCCLient

NCClient is a Python library which enables developers to send and receive NETCONF messages. NCClient requires the developer to write the raw XML of the NETCONF message, and then takes care of the RPC layer and establishing the communications channel to the network device.

The raw XML needed to access a given feature can easily be found using a tool such as _Cisco's YangExplorer_. Once this XML code is obtained, it can be turned into a template using Python's native format method. You can also use a more powerful templating library like Jinja2.

The following shows an edit config call to NCClient from a Python script. The XML message has already been formatted and is sent as the variable snippet. 

## YDK-Py

NCClient is adequate for many types of scripts. However, some developers prefer not to work with raw XML. In order to address their needs, Cisco has released Yang Developer Kit (YDK)

YDK consists of two parts:

* YDK-gen: This generates Python bindings from YANG data models.
* YDK-py: The Python module with the actual bindings for Python

YDK can actually generate bindings for more languages than Python. Most developers will not need the YDK-gen tool unless they need to customize the bindings. YDK-py is the preferred tool for most developers, as it has the bindings already built.

YDK-py provides native Python bindings for YANG data models. Rather than writing raw XML, the coder works with native Python classes, variables, and functions.

The following code snippet shows an example of using YDK to configure an interface on a router or switch running IOS XE 16.5:

```python
from ydk.services import CRUDService
from ydk.providersimport NetconfServiceProvider
from ydk.models.cisco_ios_xeimport Cisco_IOS_XE_native as xe_native

def config(interface):
    """Add config data to interface object."""
    gigabitethernet= interface.Gigabitethernet() 
    gigabitethernet.name = "2/0/10" 
    gigabitethernet.description = "Connected_to_Core_Switch" 
    gigabitethernet.ip.address.primary.address = "15.10.1.1" 
    gigabitethernet.ip.address.primary.mask = "255.255.255.0" 
    ip_add.gigabitethernet.append(gigabitethernet)

interface = xe_native.Native.Interface()  # create object 
config(interface)  # add object configuration
```

