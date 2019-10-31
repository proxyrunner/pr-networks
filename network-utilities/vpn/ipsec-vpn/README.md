# Intro to IPsec VPN Bootcamp

## We take a look at the various use cases for VPNs. 

* Types of VPN Models
* security Technologies with VPNs
* Virtual Tunnel Interfaces
* DMVPN

## Objectives
 
* Understand Site to Site VPN
* Learn and understand IKE Phase I 7 II
* Understand benefits of IPsec VPN
* NHRP, GRE, VTI
* EIGRP, OSPF, BGP over DMVPN

## Types of VPNs

* Client Access VPN
    + Software VPN Client
    + VPN Concentrator
* Host to Host VPN
    + Server VPN Agent
    + Server VPN Agent
* Site to Site VPN
    + Chicago
    + Raleigh

### Site to Site VPN Examples

* Site to Site VPN is a very popular form of VPN
* While many VPN technologies include encryption, authentication, data integrity, some don't.
* Examples:
    + MPLS VPN
    + IPsec VPN
    + GRE, IP in IP, VTI Tunnel
    + Private leased line or L2 circuit (T1, MetroEthernet, etc.)

## VPN Models
* Peer to peer model
    + Requires service provider involvement, tunneling or routing methods.
    + Value add of service provider
    + Simple for customer to deploy (SP administered)
* Overlay model
    + Service provider agnostic; does not require support of the SP.
    + Typically agnostic of the underlay
    + Requires customer to configure and support

### VPN Model Examples

* Peer to peer model examples:
    + MPLS VPN, L2 VPN
    + Service provider (QinQ) Tunneling
    + Leased or packet switched technologies\*
* Overlay model examples:
    + GRE Tunnel (plain text or secured)
    + VTI's
    + DMVPN

## IPsec Benefits

* IPsec is an overlay VPNs type
* Relatively easy to deploy
* Can provide the following:
    1. Authentication\*
    2. Data Integrity\*
    3. Confidentiality \*
    4. Anti-reply\*

## IPsec suite

* IPsec is a layer 3 protocol
* Implicitly IPsec protects any upper layer payload
* IPsec is actually a suite of protocols & methods that provide the aforementioned functionality:
    + Encapsulation Security Protocol (ESP), Authentication Header (AH)
    + Diffie-Hellman (DH)
    + Internet Security Association and Key Management Protocol (ISAKMP) which is implemented as Internet Key Exchange (IKE).
    + Various hashing & cipher suites: AES, SHA, 3DES, etc.

