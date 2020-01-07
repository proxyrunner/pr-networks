# OSPF Authentication

OSPF has different types of authentication, EIGRP doesn't.

Two-step process:

1. Authentication must be enabled, and authentication type must be selected.
2. The authentication key must be configured per interface.

You may do it one of two ways:

1. Enable at the interface using the __ip ospf authentication [message-digest]__ interface-level command.

> ip ospf authentication [message-digest]

2. Enable on all interfaces in an area by changing the area wide authentication setting using the __area <#> authentication [message-digest]__ subcommand under router ospf.

> area <#> authentication [message-digest]

* Authentication Key
    + Cannot be configured area wide
    + Must be configured individually on each interface
* Three types of authentication:
    + Type 0: no authentication
    + Type 1: clear text authentication
    + Type 2: MD5 authentication

* OSPF also supports the use of multiple keys on the same interface, but it does not support key chain
* Multiple keys can only be configured with the type 2 MD5 authentication type.
* This is useful when doing migration of keys
* These keys cannot be configured as time based.

## OSPF Authentication Pt. II

For a type 0, no configuration is required. You can also configure authentication type for area-wide settings:

> area <#> authentication (type 1)

> area <#> authentication message-digest(type 2)

To configure auth type using interface subcommands, you can use these

> ip ospf authentication null (type 0)

> ip ospf authentication (type 1)

> ip ospf authentication message-digest (type 2)

