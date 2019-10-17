# NETCONF Internet Protocol

## WTF IS NETCONF

The Network Configuration Protocol is a network management protocol developed and standardized by the IETF. It was developed in the NETCONF working group and published in December 2006 as RFC 4741 and later revised in June 2011 and published as RFC 6241

## How do I operate NETCONF with Python

Check it out, __ncclient__.

[ncclient](https://github.com/ncclient/ncclient)

> pip install ncclient

```
Installing collected packages: lxml, ncclient
     Running setup.py install for ncclient ... done
Successfully installed lxml-4.4.1 ncclient-0.6.6
```

### Remote Procedure Call (RPC layer)

See NCClient to review RPCs role in Python Network Automation: NCClient requires the developer to write the raw XML of the NETCONF message, and then takes care of the RPC layer and establishing the communications channel to the network device.