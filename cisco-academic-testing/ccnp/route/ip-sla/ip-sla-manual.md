# IP SLA Manual

## R(config-ip-sla)#

```
IP SLAs entry configuration commands:
  dhcp         DHCP Operation
  dns          DNS Query Operation
  ethernet     Ethernet Operations
  exit         Exit Operation Configuration
  ftp          FTP Operation
  http         HTTP Operation
  icmp-echo    ICMP Echo Operation
  icmp-jitter  ICMP Jitter Operation
  mpls         MPLS Operation
  path-echo    Path Discovered ICMP Echo Operation
  path-jitter  Path Discovered ICMP Jitter Operation
  tcp-connect  TCP Connect Operation
  udp-echo     UDP Echo Operation
  udp-jitter   UDP Jitter Operation
  voip         Voice Over IP Operation
```

## R(config)#

```
R6(config)#ip sla ?                                       
  <1-2147483647>          Entry Number
  auto                    IP SLAs Auto Configuration
  enable                  Enable Event Notifications
  endpoint-list           Endpoint list configuration
  ethernet-monitor        IP SLAs Auto Ethernet Configuration
  group                   Group Configuration or Group Scheduling
  key-chain               Use MD5 Authentication for IP SLAs Control Messages
  logging                 Enable Syslog
  low-memory              Configure Low Water Memory Mark
  reaction-configuration  IP SLAs Reaction-Configuration
  reaction-trigger        IP SLAs Trigger Assignment
  reset                   IP SLAs Reset
  responder               Enable IP SLAs Responder
  restart                 Restart An Active Entry
  schedule                Entry Scheduling
  server                  IPPM server configuration
```

```
R6(config)#ip sla schedule ?
  <1-2147483647>  Entry number
```

```
R6(config)#ip sla schedule 1?
<1-2147483647>  
```

```
R6(config)#ip sla schedule 1 ?
  ageout      How long to keep this Entry when inactive
  life        Length of time to execute in seconds
  recurring   Probe to be scheduled automatically every day
  start-time  When to start this entry
  <cr>
```

```
R6(config)#ip sla schedule 1 start-time ?
  after     Start after a certain amount of time from now
  hh:mm     Start time (hh:mm)
  hh:mm:ss  Start time (hh:mm:ss)
  now       Start now
  pending   Start pending
```

```
R6(config)#ip sla schedule 1 start-time now ? 
  ageout     How long to keep this Entry when inactive
  life       Length of time to execute in seconds
  recurring  Probe to be scheduled automatically every day
  <cr>
```

```
R6(config)#ip sla schedule 1 start-time now life ?
  <0-2147483647>  Life seconds (default 3600)
  forever         continue running forever
```
