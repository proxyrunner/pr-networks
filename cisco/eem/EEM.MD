# Embedded Event Manager 

EEM is a cisco proprietary software component to assist administrators.

### Support

* IOS
* IOS XR
* NX-OS

EEM tracks a classifies events that take place on a router, as well as provides notification options for those events. EEM allows you to automate tasks, perform minor enhancements, and create workarounds.

### Two independent pieces

* Applets
* Scripting

## EEM Detectors

They can consist of the following:

* SNMP - Monitoring SNMP Objects
* Syslog - Respond to various syslog messages, allows for REGEX
* Counter - Monitoring and responding to interface counter when cross threshold settings.
* CLI Events - Screening CLI input for a REGEX match
* None - Event detector is use to test EEM Script/Applet using "event manager run" command
* Timers - Countdown, watchdog, and CRON
* IP SLA and Netflow Events

## Common REGEX

* ^ = Start of string
* $ = End of String
* . = Any single character
* "*" = zero or more instance
* + = One or more instances
* ? = Zero or one instances
