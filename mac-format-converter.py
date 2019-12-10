#
# Convert a text file of MAC addresses from 12:34:56:78:91:01 to 1234.5678.9101 format
#

macs = open('mac.txt', 'r')
  
for mac in macs.readlines():
    mac = mac.replace(':', '')
    ciscomac = '.'.join(mac[i:i + 4] for i in range(0, 12, 4)).lower()
    print(ciscomac)
