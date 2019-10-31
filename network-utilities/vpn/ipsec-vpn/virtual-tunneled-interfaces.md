# IPsec Secured GRE w/Crypto Map

## IPsec Secured GRE w/Crypto Map

* Two draw backs of basic crypto map VPNs is that they are not-multi protocol and do not support broadcast/multicast.
* One solution is to leverage GRE.
* This solves several problems:
    1. Cuts down on proxy ACL. (Only need tunnel source/destination)
    2. Allows routing protocols to run inside the tunnel
    3. Multiprotocol

## IPsec Secured GRE Tunnel

* Key point: do not apply an IPSEC-ISAKMP crypto map to a tunnel interface. [This is not supported in recent code.]
* To secure a GRE tunnel, the crypto map is applied to the physical interface and the proxy identity ACL matches only the GRE source and destination traffic.
* There is a difference between GRE over IPsec [what we want] versus IPsec over GRE [not supported]

## IPsec Data Plan & MTU

* IPsec may have issues with MTU if the "df-bit" can not be read in the encrypted packet.
* This prevents path MTU discovery from working and therefore transits packets may be fragmented
* Three possible methods to resolve:
    1. Decrease MTU to a safe value of 1400
    2. Configure IPsec to support path MTU (copy df-bit) discovery.
    3. For TCP traffic: have router adjust MSS to 1360.

## IPsec GRE

* Using a crypto map can be difficult due to the amount of configuration which leaves a potential for error.
* It is possible to use a streamline version of a crypto map that is called an "IPsec profile".
* An IPsec profile has the following characteristics:
    + Does not require a proxy-ID since is the defined by the tunnel already
    + Does not require a peer address since this is the tunnel endpoint
    + Requires only a transform-set