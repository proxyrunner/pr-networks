# Getting Started

## Distinguish Name and Managed Object

__Management Information Tree (MIT)__
__Management Object (MO)__
__Distinguished Name (DN)__

The DN provides the fully qualified path from the root of the object tree to the object itself.

DN is made up of a series of pieces known as __relative names(RN)__.

dn = {rn}/{rn}/{rn}/{rn}...

## Define Your Variables

* Settings > Manage Environments

## Create New Request to Login to APIC

```
POST    https://{{APIC}}/api/aaaLogin.json

Body

{ "aaaUser" : { "attributes": {"name":"{{username}}","pwd":"{{password}}" } } }
```

