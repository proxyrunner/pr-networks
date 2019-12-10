# AnyConnect Lab on Cisco ASA

Subject: This field is broken down into subfields that present components of the system’s identity. In this case:

* CN (Common Name) is Site1 SSL VPN: often the DNS hostname is listed in the CN field,
* O (Organization) is CCNAsec Labs. The owning company is generally specified in the O field.
* OU (Organizational Unit) is Lab Operations. The department that is associated with the system is generally specified in the OU field.

 While not used here, other fields that are often present within the subject are C for country, S for state or P for province, and L for locality.

* Subject Alternative Name: This field shows DNS Name = vpn.site1.public. When browsing an HTTPS URL, the server hostname is specified at the beginning of the URL. The browser expects that hostname to match either the CN in the subject field or a DNS Name in the Subject Alternative Name field. If neither is the case, the browser will display a security warning due to the mismatch. Because of this dependency on hostname resolution, properly functioning DNS is very important to PKI.
* Valid from and Valid to: Certificates have a limited lifespan. If the browser determines that the current time is not within the validity window that is specified by these two fields, it will display a security warning to the user. Because of this, valid time settings are very important to PKI. The NTP protocol is often used to ensure valid time.
* Issuer: This field identifies the CA that signed this identity certificate. In this case, it is the Services, Inc. Signing CA. If the browser has access to the public key of this CA, it will use the public key to verify the signature on the certificate. The browser gets the CA public key from the CA identity certificate. If the browser does not have the CA identity certificate in its certificate store, it will display a security warning to the user. Also, if the browser does have the CA identity certificate but the signature is found to be invalid, it will display a security warning to the user.
* Public Key: The public key of the Site1-ASA. The Site1-ASA is the only system that has the matching private key. Assuming that the browser accepted the name of the SSL server, found that the time was within the certificate validity period and that the CA signature was valid, then the browser will generate a session key to protect the SSL data. It will encrypt the session key with this public key and forward it to the SSL server. Only the real server (in this case, the Site1-ASA) will have the associated private key to decrypt the session key. If the server can decrypt the session key, then data can flow bidirectionally over the SSL connection that is protected by the session key that is specified by the client.

### CA Certificate

```
crypto ca trustpoint Services-Root-CA
    recovation-check none
    no id-usage
    enrollment terminal
crypto ca authenticate Services-Root-CA nointeractive
    ...
    <key not inserted for brevity>
    ...
    quit
```

### Identity Certificate

```
crypto ca trustpoint SSL-VPN
    revocation-check none
    keypair Self-Signed-KeyPair
    id-usage ssl-ipsec
    fqdn vpn.site1.public
    subject-name CN=Site1 SSL VPN,OU=Lab Operations,O=CCNAsec Labs
    enrollment terminal
crypto ca enroll SSL-VPN noconfirm
```
