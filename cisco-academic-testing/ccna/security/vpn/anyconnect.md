# Basic Cisco AnyConnect SSL VPN

## Cisco AnyConnect Modes

* Standalone Mode
    + Establish tunnel without web browser
    + Permanently install Cisco AnyConnect on endpoint
    + User opens AnyConnect, enters credentials
    + User might need to choose group
    + automatically needed

* WebLaunch mode
    + User browses to URL, enters credentials
    + Optional banner
    + In portal, user starts
    + Connection established
    + Client must be as new as ASA's AnyConnect
    + Option: Policy to bypass client downloader
        * Weblaunch and automatic update disabled.
    
## SSL VPN Components

SSL/TLS tunnel with the Cisco ASA. The solution is bidirectional authentication, in which the client authenticates the Cisco ASA security appliance with a certificate-base authentication method, and the Cisco ASA security appliance authenticates the user using certificates and a local or external user database, or a combination.

* Internal CA
* AAA
* Active Directory
* DHCP/DNS

Datagram Transport Layer Securtyiy (DTLS) - is an alternative VPN transport protocol to SSL/TLS. DTLS allows datagram-based applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery. The DTLS protocol is based on the stream-oriented TLS protocol and is intended to provide similar security guarantees.

## SSL VPN Server Authentication

For an ASA to prove its authenticity, it creates a self-signed  x.509 certificate on each reboot and sends to client. A self-signed certificate is commonly not acceptable (after-all, I AM the Queens of England, you know?). The recommended approach is using a certificat authority service. Now, when a CA Authority signs the cert as well, the ASA is credible.

## SSL VPN Client Authentication

* Users choose a connection profile, or connect to a group URL
* Default Profile: DefaultWEBVPNGroup
    + Authentication: via ASA local Username/Password database
    + Client enters credentials, sent to ASA
    + ASA compares supplied credentials to local database
    + Tunnel established, restriction policies applied.

## SSL VPN Client IP Address Assignment

* ASA assigns IP address to client's virtual NIC
    + Used as source address to access all internal resources
* IP assignment methods
    + ASA local pool, assign to connection profile
        * Simplest method if all use same profile
    + ASA local pool, assign to group policy
        * Best if you need to differentiate multiple user groups
    * IP address assigned to use account in local db
        * Per-user IP addresses and policies
        * Simplifies auditing and tracking

### IP assignment sources

* Local Pool
* DHCP server
* RADIUS Server

## Basic AnyConnect SSL VPN Configuration Tasks

General deployment tasks are necessary to create a basic Cisco AnyConnect full-tunnel SSL VPN:

1. Install the Cisco AnyConnect client image, which should already be copied to the Cisco ASA flash memory. You can also skip this step, and you will be asked to install the AnyConnect image later when enabling full-client SSL VPN access.

2. Enable Cisco AnyConnect SSL VPN on Cisco ASA:

    * Enable full-client SSL VPN traffic termination on a Cisco ASA interface, which enables the security appliance SSL VPN server function. When enabling full-client SSL VPN access, you will be asked to select and install the Cisco AnyConnect image file, if you have not done it before.
    * You must assign the installed identity certificate of the Cisco ASA to the chosen VPN traffic termination interface.

3. Define an IP address pool.
4. Configure identity NAT for VPN client access.
5. Edit the default group policy or create a custom policy:

    * Make sure that support for Cisco AnyConnect SSL VPN is enabled.
    * Optionally, configure split tunneling, which allows you to tunnel only certain traffic to specific internal protected networks, while all other traffic bypasses the VPN tunnel.

6. Edit the default connection profile or create a custom profile:

    * Allow the user to choose a connection profile at login. This setting is required if you want to assign users to a specific connection profile rather than having them use the default DefaultWebVPNGroup profile.
    * Select the authentication method. The default option is local AAA authentication.
    * To provide IP addresses to the Cisco AnyConnect clients, create a local address pool.
