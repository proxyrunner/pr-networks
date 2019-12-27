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

```
R6#show ip sla ?
  application             IP SLAs Application
  authentication          IP SLAs Authentication Information
  auto                    IP SLAs Auto Show Commands
  configuration           IP SLAs Configuration
  endpoint-list           IP SLAs Endpoint list configuration
  enhanced-history        IP SLAs Enhanced History
  ethernet-monitor        IP SLAs Auto Ethernet Monitor
  event-publisher         IP SLAs Event Publisher
  group                   IP SLAs Group Scheduling/Configuration
  history                 IP SLAs History
  mpls-lsp-monitor        IP SLAs MPLS LSP Monitor
  reaction-configuration  IP SLAs Reaction Configuration
  reaction-trigger        IP SLAs Reaction Trigger
  responder               IP SLAs Responder Information
  statistics              IP SLAs Statistics
  summary                 IP SLAs Statistics Summary
  twamp                   IP SLAs TWAMP
```

```
R6(config-track)#?
Tracking instance configuration commands:
  default        Set a command to its defaults
  default-state  Default object state
  delay          Tracking delay
  exit           Exit from tracking configuration mode
  no             Negate a command or set its defaults
```

```
R6#show ip sla configuration
IP SLAs Infrastructure Engine-III
Entry number: 1
Owner: 
Tag: 
Operation timeout (milliseconds): 5000
Type of operation to perform: icmp-echo
Target address/Source interface: 7.7.7.7/GigabitEthernet0/0
Type Of Service parameter: 0x0
Request size (ARR data portion): 28
Verify data: No
Vrf Name: 
Schedule:
   Operation frequency (seconds): 5  (not considered if randomly scheduled)
   Next Scheduled Start Time: Start Time already passed
   Group Scheduled : FALSE
   Randomly Scheduled : FALSE
   Life (seconds): Forever
   Entry Ageout (seconds): never
   Recurring (Starting Everyday): FALSE
   Status of entry (SNMP RowStatus): Active
Threshold (milliseconds): 5000
Distribution Statistics:
   Number of statistic hours kept: 2
   Number of statistic distribution buckets kept: 1
   Statistic distribution interval (milliseconds): 20
Enhanced History:
History Statistics:
   Number of history Lives kept: 0
   Number of history Buckets kept: 15
   History Filter Type: None
```

```
R6#show track
Track 1
  IP SLA 1 reachability
  Reachability is Up
    1 change, last change 00:00:40
  Latest operation return code: OK
  Latest RTT (millisecs) 16
R6#
```