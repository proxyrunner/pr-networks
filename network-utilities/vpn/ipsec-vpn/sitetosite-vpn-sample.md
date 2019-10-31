# Site to Site VPN Configuration Sample w/Crypto Map

## Crypto Map Based VPN Caveats

* Crypto map based VPNs do not support routing protocols unless additiona (nested) encapsulation is used. Example:GRE
* The direction is implicitly outbound
* The assumption is that the peer addresses are routable; crypto does not provide routing per-se.
* An interface may have only one crypto map; howevere, a crypto map may be applied to multiple interfaces.

## Basic Crypto Map VPN Task List
   
* Phase 1 parameters:
    - [ ] ISAKMP policyL Authentication, Encryption (cipher), DH Group, and Hash
    - [ ] ISAKMP peer key, assuming pre-shared key

* Phase 2 parameters:
    - [ ] Crypto map: transform-set, peer address, and proxy-id
    - [ ] Transform-set: authentication, encryption and mode.
    - [ ] Define proxy-id ACL

    - [ ] Apply crypto map to interface
    - [ ] Generate some traffic!

## IPsec Encryption Best Practices

* Consider using PKI when possible
* If using PSK encrypt it in the running configuration
* Use a strong cryptographic suites:
    - [x] See Cisco white paper "Next Generation Encryption
    - [x] Use ECC "Elliptic Curve Cryptography" DH groups 19 or 20, if possible
    - [x] >2048 is best practice for non-ECC groups
    - [x] AES and SHA256
    - [x] Always avoid the following: DH groups 1/2/6, DES, 3DES, RC4, MD5, and SHA1.\*
