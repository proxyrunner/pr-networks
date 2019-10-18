# IP Service Level Agreements (SLA)

Please note that this training and information is pertinent to Cisco(C) CCNP studies. Furthermore, IP SLA is a much more intricate and developed technology than the scope of this guide.

## Configuring IP SLA

Be be aware that version support varies by IOS.

* Define the IP SLA Probe

```
ip sla 11
icmp-echo 10.1.1.1 source-interface Ethernet 0/0
frequency 10
ip sla schedule 11 start-time now life forever
```

* Define the tracking object and link it to probe

```
track 1 ip sla 11 reachability
```

### What is this example doing?

This is a basic ICMP-based test to verify a path to ISP #1 is available. This is achieved by sending periodic ICMP echo-requests to a router at the ISP.

#### Verification

Here are 2 show commands to verify IP SLA configurations:

> show ip sla

##### Output:

```
R1#show ip sla
*Oct 18 13:43:06.627: %SYS-5-CONFIG_I: Configured from console by console
R1#show ip sla config
R1#show ip sla configuration 
IP SLAs Infrastructure Engine-III
Entry number: 11
Owner: 
Tag: 
Operation timeout (milliseconds): 5000
Type of operation to perform: icmp-echo
Target address/Source interface: 11.11.11.254/GigabitEthernet0/0
Type Of Service parameter: 0x0
Request size (ARR data portion): 28
Verify data: No
Vrf Name: 
Schedule:
   Operation frequency (seconds): 60  (not considered if randomly scheduled)
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

> show track

##### Output:

```

R1#show track
Track 1
  IP SLA 11 reachability
  Reachability is Up
    1 change, last change 00:00:45
  Latest operation return code: OK
  Latest RTT (millisecs) 19
```
