# Crypto Map Based IPsec VPNs

## ISAKMP & IKE Overview

### IPsec Data Plane (SPI)

![SPI](https://github.com/gil-ryan/grs-networking-public/blob/master/network-utilities/vpn/ipsec-vpn/spi.PNG)

### ISAKMP Overview

![Phases I & II](https://github.com/gil-ryan/grs-networking-public/blob/master/network-utilities/vpn/ipsec-vpn/isakmps.PNG)

* ISAKMP: Internet Security Association and Key Management Protocol
* ISAMKP is a protocol that defines procedures/framework of key exchange
* ISAKMP can implemented in various ways such as:
    + Manual Keying
    + IKE: Internet Key Exchange
    + GDOI: Group Domain of Interpretation
    + KINK: Kerberized Internet Negotiations of Keys

### Security Associations

* Security Association [SA]: relationship between two endpoints that have agreed on parameters.
* Parameters are matching in a top down processing similar to an access-list.
* The endpoints are known as "IKE peers"
    + In the context of site-to-site VPN, the peer is the routers IP address.
    + One router initiates to its peers and the IKE responder looks for a policy match

### Diffie-Hellman Exchange

* The purpose of Diffie-Hellman protocol is to generate and exchange shared keys over an insecure channel.
* In IPsec nomenclature this is referred to as the "DH Group":
    + For example: DH Group 1 defines 768 bit key material
    + Generally speak bigger is better; current best practice is 2048 bit key or larger.\*
* Re-keying occurs at the specified interval (SA lifetime) to maintain key integrity
* Re-keying can be CPU intensive if not done in hardware.

## IKE Phase I

* Problem solved by IKE Phase I: establish a secure channel to exchange parameters about IKE phase II
* Components of IKE Phase I are defined in something known as the "ISAKMP policy".
* Leverages UDP/500 [oR UDP/4500 when NAT traversal is necessary]
* IKE Phase I works in one of two mode:
    1. Main Mode: Used for site-to-site VPNs. IKE exchange occurs over several discreet steps; slower but more secure
    2. Aggressive Mode: Typically use for client access VPNs only. Few exchanges with the result of being faster but less secure
* Components of ISKMP [IKE Phase 1]:
    1. Cipher SuiteL example AES
    2. Diffie-Hellman (DH Group) algorithm: generate symmetric key
    3. Hashing algorithm: example SHA
    4. Authentication method: pre-shared key or PKI
    5. SA Lifetime: how long before re-keying
* Goal of ISAKMP: arrive at a state known as the ISAKMP Security Association (SA).
* A successful ISAKMP SA is a "tether" to the VPN peer that indicates both hosts agree on parameters of the VPN. [Also called IKE Phase 1]

### IKE Phase I Authentication

* IKE phase 1 supports three authentication types:
    1. Pre-shared Keys [PSK]
    2. RSA Certificates [PKI]
    3. RSA Encrypted Nonces
        + A cryptograhic none is a random or pseudo-random number issued in an authentication protocol to ensure that old communications cannot be reused in replay attacks
* Pre-shared keys are easier for lab purposes but not very scalable and ultimately is not as secure. [Note: PSK's can be encrypted in the running configuration.]
* PKI provides more scalability and scales much better.

## ISE Phase II

* Basic components of IKE phase 2:
    1. Cipher Suite: example AES
    2. Authentication: example SHA
    3. Mode: tunnel or transport
    4. Protocol: AH or ESP
* Goal of phase II: arrive at a state known as the IPsec Security Association (SA) and establish a security parameter index (SPI).
* These are the parameters used for data plane traffic encryption/decryption

* Only one exchange mode named "quick mode".
* Phase II supports two protocols:
    1. Authentication Header (AH): IP protocol number 51 only support authentication
    2. Encapsulating Security Payload (ESH): IP protocol number 50 support authentication & encryption.

* When used with NAT, leverages UDP/4500
* Phase 2 runs in one of two modes:
    1. Tunnel: encrypts/authenticates entire IP packet and creates new headers.
    2. Transport: only the payload is encrypted/authenticated.

### IKE Phase 2 PFS

* Phase 2 support "perfect forward secrecy" (PFS)
* PFS dictates whether the DH keys generated in phase I can be reused for phase II
* When enabled, phase 2 runs its own DH exchange.
    + Benefit: increased security for phase II
    + Drawback: more resource intensive to maintain separate sets of keys for both phases.
    

## Site to Site VPN Configuration Sample w/ Crypto Map

## IPsec Encryption Best Practices

