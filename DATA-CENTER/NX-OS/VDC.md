# Virtual Device Context

* First understand a switches attributes
    + Control Plane
    + Data Plane
    + Management Plane
* VDCs enable the virtualization of these planes and hardware resources meaning each VDC has it's very own.
* Enables collapsing of multiple logical networks into single physical infrastructure
    + production, dev, test
    + intranet, DMZ, extranet

## Interface Allocation

* Ports are assigned on a per VDC basis and cannot be shared across VDCs
* once a port is assigned, all subsequent configuration is done from within that VDC
* is this example, a N77-F348XP-25 requires allocation in port groups of eight to align ASIC resources

## VDC Configuration

- [ ] Configure Terminal
- [ ] Show license usage

It's important to check the licensing, because unless you're on a production NX-OS device, or have one in the lab. Chances are going to be you cannot configure VDCs on any virtual instance of NX-OS. It's a bummer, similar to ASA contexts. In this case we'll only be able to operate and work on our current VDC.