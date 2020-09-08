# Application Centric Infrastructure [ACI]

## Getting Started

These references are all Data Center [ACItoolkit](https://acitoolkit.readthedocs.io/en/latest/objectmodel.html)

## Definitions and Index of ACI Terminology

__Tenant__ is the root class within the acitoolkit object model hierarchy. All of the application topology configuration occurs within a Tenant.

__AppProfile__ is the Application Profile class. It contains the configuration for a given application.

__EPG__ is the Endpoint Group class. This is the object for defining configuration that is applied when endpoints connect to the fabric.

__Context__ is the class representing an L3 namespace (roughly, a traditional VRF in Cisco terminology).

__BridgeDomain__ is the class representing an L2 forwarding domain (roughly, a traditional VLAN). It is associated with a single Context.

__Subnet__ is the class representing an L3 subnet. It is associated with a single BridgeDomain.

__OutsideEPG__ is the class representing an EPG that connects to the world outside the fabric. This is where routing protocols such as OSPF are enabled.

__Contracts__ define the application network services being provided and consumed by EPGs. EPGs may provide and consume many contracts.

__Taboos__ define the application network services that can never be provided or consumed by EPGs.

__FilterEntry__ contained within either a Contract or a Taboo. Defines the traffic profile that the Contract or Taboo applies.

### Inteface Object Model

