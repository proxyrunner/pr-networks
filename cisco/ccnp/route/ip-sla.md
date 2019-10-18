# IP Service Level Agreements (SLA)

## Configuring IP SLA

Be be aware that version support varies by IOS.

* Define the IP SLA Probe

```
ip sla 11
icmp-echo 10.1.1.1 source-intercace Ethernet 0/0
frequency 10
ip sla schedule 11 start-time now life forever
```

* Define the tracking object and link it to probe

```
track 1 ip sla 11 reachability
```
