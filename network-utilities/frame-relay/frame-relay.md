# Frame Relay Configurations

## Simple configuration to put Frame-Relay on an interface

```
!
interface Serial0
 ip address 3.1.3.1 255.255.255.0
 encapsulation frame-relay
 frame-relay interface-dlci 140
!
```
