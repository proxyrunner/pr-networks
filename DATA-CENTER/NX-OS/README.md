# Getting Started

So...what the hell am I talking about? Great question, for now, this repository will focus on [Cisco Systems Data Center products.](https://www.cisco.com/c/en/us/solutions/data-center-virtualization/index.html) We will do some in depth dives in the _Nexus_ platform, followed by the _Application Centric Infrastructure_, better known as _ACI_.

## Table of Contents

### Feature Configuration

* [Virtual Port Channel - VPC](./VPC.md)
    + [VPC Configurations](./CONFIGURATIONS/vpc.conf)
* [Virtual Device Context - VDC](./VDC.md)
    + [VDC Configurations](./CONFIGURATIONS/vdc.conf)


## NX-OS Features

Designed for the Data Center. NX-OS is a single operating system that covers the entire Cisco Nexus Platform. It had true modularity, meaning you only enable process, so if want to run _Telnet_, it must be enabled.

* Virtualization
    + VRF Aware
    + Virtual Port Channels
    + Virtual device context
    + MPLS
    + Locater ID Separator Protocol
* Resiliency (High Availability)
    + ISSU (In-Service Software Upgrade)
    + Non-Disruptive Stateful Supervisor Switchover (SSO)
    + Stateful process restarts
    + Gracefull Process Restart
* Operation
    + GOLD, Smart Call Home, EEM w/ TCL
    + Netflow, NDE v5/v9, FNF CLI
    + SPAN, ERSPAN, ACL Capture
    + Wireshark
    + SNMP/MIB
    + NETCONF/XML
    + Configuration checkpoint and rollback
* IPv4/IPv6 address-family support
