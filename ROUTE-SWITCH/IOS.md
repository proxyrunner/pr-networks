# Internetwork Operating System - IOS

## Privileges and Administration

## Enable Remote Adminstration and Privileges

### Enable SCP

> ip scp server enable

From what I've dealt with, you'll need some AAA commands too:

```
S1(config)#do sho run | i aaa
aaa new-model
aaa authentication login default local
aaa authorization exec default local none 
aaa session-id common
!
S1(config)#do sho run | i username
username grs privilege 15 secret 5 $1$d7ch$S7Bm12t3Juy/8Lx0MXi/m1
```

### User Mode

The first time you boot IOS, the CLI prompt initializes in _user mode_. Denoted with a __>__ symbol.

> Switch>

or

> Router>

### Exec Mode

```
# Enter exec mode
enable
```

### Privileged Exec Mode

Once you're in _exec mode_ like so:

> Router#

You can use the __configure terminal__ command to enter _privileged exec_ mode

```
# The famous conf t
configure terminal
```

> Router(config)# 

#### SSH Directly into Privilege Mode

> line vty 0 15
>
> privilege level 15