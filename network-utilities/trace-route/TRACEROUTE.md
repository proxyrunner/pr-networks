#Traceroute Topics

## Topics to Discuss:
	*How traceroute works
	*Interpreting DNS in traceroute
	*Understanding network latency ICMP prioritization and rate-limiting
	*ICMP prioritization and rate-limiting
	*Asymmetric forwarding paths 
	*Load balancing across multiple paths
	*Traceroute and MPLS
	*Random Traceroute Factoid
		*The default starting destination probe port in the UNIX traceroute implementation is 33434. This comes from 32768 (215) + 666 (the mark of Satan). Coincidence?
		
		
## How Traceroute Works
	1. Launch a probe packet towards DST, with a TTL of 1.
	2. Every router hop decrements the IP TTL of the packets by 1.
	3. When the TTL hits 0, packet is dropped, router sends ICMP TTL Exceed packets to SRC with the original probe packet as payload
	4. SRC receives this ICMP message, displays a traceroute "hop"
	5. Repeat from step 1, with TTL incremented 1 each time, until…
	6. DST host receives probe, returns ICMP Dest Unreachable
	7. SRC stops the traceroute upon receipt of ICMP Dest Unreachable



## Traceroute Implementation Details
	* Traceroute can use many protocols for probe packets
		* Classic UNIX traceroute uses UDP probes
			* With a starting destination of 33434, incrementing once per probe.
			* Cannot detect the end of the traceroute if the DST does not return an ICMP Dest Unreachable. This can happen as the results of firewalls, configuration settings, or a real application listening on the destination port
		* Other implementations use ICMP Echo Request probes
			* Windows tracert.exe and MTR are the two biggest examples
			* These also cannot detect the end of the traceroute if the DST does not return an ICMP Echo Response. This may or may not be more frequently firewalled than the UDP -> ICMP Dest Unreachable response.
		* Many modern traceroute implementations can do all
			* Configurable UDP, TCP, or ICMP probe packets via CLI flags.
			* TCP is a poor choice for general use (frequently filtered), trpically only seen as a method to work around specific firewalls.
	
## Traceroute Implementation Details part II 
	* Most implementations send multiple probes per router hop
		* The default for classic traceroute is 3 probes per hop
			* Giving the latency results, or 3 *'s if there is no response
		* One specific implementation (MTR) sends an endless loop of probes.
