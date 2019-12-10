# IPsec VPNs

A site-to-site VPN is an extension of a classic WAN network. Site-to-site VPNs connect entire networks to each other. Previously, a leased-line or Frame Relay connection was required to connect sites, but because most corporations now have Internet access, these connected can be replaced with site-to-site VPNs.

Hosts send and receive transparent TCP/IP traffic between each other. VPN gateways provide security services at the borders between the trusted and nontrusted networks.

A VPN gateway is responsible for encrypting packets that are destined for the peer network, attaching message authentication codes, and encapsulating the protected data using a new IP header.

The transformed packet is routed across the untrusted network that is based on the VPN gateway IP addresses specified in the new IP header. Upon arrival, the peer VPN gateway strips the headers, verifies and decrypts the content, and relays the original packets towards the target host inside its private network.

Remote-access VPN is an evolution of dialoup connections. Remote-access VPNs can support the needs of telecommuters, mobile users, and extranet consumer-to-business traffic. Remote-access VPNs connect individual hosts that must access their company network securely over the Internet.

If a VPN is used to connect entities belonging to the same organization, it is considerd an intranet VPN. If a VPN is used to connect entities belonging to two different organization, it is considered an extranet VPN. This distinction is separate from site-to-site and remote access. Similarly, remote-access VPNs can be used for both intranet and extranet connections.

It is important to recognize there is more out there than IPsec VPN (wireguard, for example). SSL provides a suite of security services that is similar to security services provided by IPsec. SSL VPN has become popular for the implementation of remote-access VPNs.

## IPsec Security Services

* Confidentiality
* Data integrity
* Origin authenticatio
    + PSKs - Preshared Key
    + Digital certificates
    + RSA encrypted nonces
* Antireplay protection
    + packets are protected by comparing the sequence number
* Key management

### Encryption Algorithms and key length

* __DES__ algorithm: DES was developed by IBM. DES uses a 56-bit key, ensuring high-performance encryption. DES is a symmetric key cryptosystem

* __3DES__ algorithm: The 3DES algorithm is a variant of the 56-bit DES. 3DES operates in a way that is similar to how DES operates, in that data is broken into 64-bit blocks. 3DES then processes each block three times, each time with an independent 56-bit key. 3DES provides a significant improvement in encryption strength over 56-bit DES. 3DES is a symmetric key cryptosystem

* __AES__: The National Institute of Standards and Technology (NIST) has recently adopted AES to replace the aging DES-based encryption in cryptographic devices. AES provides stronger security than DES and is computationally more efficient than 3DES. AES offers three different key lengths: 128-, 192-, and 256-bit keys

* __RSA__: RSA is an asymmetrical key cryptosystem. It commonly uses a key length of 1024 bits or larger. IPsec does not use RSA for data encryption. IKE uses RSA encryption only during the peer authentication phase

* __SEAL__: SEAL is a stream cipher that was developed in 1993 by Phillip Rogaway and Don Coppersmith, which uses a 160-bit key for encryption

Symmetric encryption algorithms such as AES require a common shared-secret key to perform encryption and decryption. You can use email, courier, or overnight express to send the shared-secret keys to the administrators of the devices. This method is obviously impractical, and does not guarantee that keys are not intercepted in transit. Public-key exchange methods allow shared keys to be dynamically generated between the encrypting and decrypting devices.

The Diffie Hellman key agreement is a public key exchange method. This method provides a way for two peers to establish a shared-secret key, which only they know, even though they are communicating over an insecure channel.

Elliptic Curve Diffie Hellman is a variant of the DH protocol using Elliptical Curve Crypto. It is part of the Suite B standards.

These algorithms are used within IKE to establish session keys. They support different prime sizes that are identified by different DH or ECDH groups. DH groups vary in the computational expense that is required for key agreement and the strength against cryptographic attacks. Larger prime sizes provide stronger security, but require more computational horsepower to execute.

* DH1: 768-bit
* DH2: 1024-bit
* DH5: 1536-bit
* DH14: 2048-bit
* DH15: 3072-bit
* DH16: 4096-bit
* DH19: 256-bit ECDH
* DH20: 384-bit ECDH
* DH24: 2048-bit ECDH

VPN data is transported over untrusted networks such as the public Internet. Potentially, this data could be intercepted and read or modified. To guard against this, HMACs are utilized by IPsec.

IPsec uses HMAC as the data integrity algorithm that verifies the integrity of the message. The figure below depicts a keyed hash that is a simplification of the more complex HMAC algorithm. The HMAC algorithm itself is beyond the scope of this material. HMAC is defined in RFC 2104. Like a keyed hash, HMAC utilizes a secret key known to the sender and the receiver. But HMAC also adds padding logic and XOR logic, and utilizes two hash calculations to produce the message authentication code.

When you are conducting business long-distance, it is necessary to know who is at the other end of the phone, email, or fax. The same is true of VPN networks. The device on the other end of the VPN tunnel must be authenticated before the communication path is considered secure.

* PSKs: A secret key value is entered into each peer manually and is used to authenticate the peer. At each end, the PSK is combined with other information to form the authentication key.
* RSA signatures: The exchange of digital certificates authenticates the peers. The local device derives a hash and encrypts it with its private key. The encrypted hash is attached to the message and is forwarded to the remote end, and it acts like a signature. At the remote end, the encrypted hash is decrypted using the public key of the local end. If the decrypted hash matches the recomputed hash, the signature is genuine.
* RSA encrypted nonces: A nonce is a random number that is generated by the peer. RSA-encrypted nonces use RSA to encrypt the nonce value and other values. This method requires that each peer is aware of the public key of the other peer before negotiation starts. For this reason, public keys must be manually copied to each peer as part of the configuration process. This method is the least used of the three authentication methods.
* ECDSA signatures: The ECDSA is the elliptic curve analog of the DSA signature method. ECDSA signatures are smaller than RSA signatures of similar cryptographic strength. ECDSA public keys (and certificates) are smaller than similar-strength DSA keys, resulting in improved communications efficiency. Furthermore, on many platforms, ECDSA operations can be computed more quickly than similar-strength RSA operations. These advantages of signature size, bandwidth, and computational efficiency may make ECDSA an attractive choice for many IKE and IKE version 2 (IKEv2) implementations.

## IKE

IPsec uses IKE to authenticat a peer computer and generate encryption keys.