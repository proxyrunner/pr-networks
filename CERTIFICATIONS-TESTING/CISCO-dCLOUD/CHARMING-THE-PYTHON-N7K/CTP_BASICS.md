# Charm the Python Basics

## 1

Concatenate variables and change to upper case.

```python
CiscoLive_N7K# >>> var1 = "charming the python"
CiscoLive_N7K# >>> var2 = " at CiscoLive %s" % '2015'
CiscoLive_N7K# >>> var1 + var2
'charming the python at CiscoLive 2015'
CiscoLive_N7K# >>> var1 + var2.upper()
'charming the python AT CISCOLIVE 2015'
```

## 2

Write a Python script to the default directory _'bootflash:scripts'_. All scripts are stored _'bootflash:scripts'_ or in a sub-directory. Then from the __enable__ prompt view the contents of the script using the _show file ..._ commmand. From the __enable__ prompt run the script using the _'source'_ command.

```python
import os
os.chdir("/bootflash/scripts")
f = open("CiscoLive2015.py", 'w')
f.write("#!/usr/bin/env python\n")
f.write("import sys\n")
f.write("args = sys.argv[1:]\n")
f.write("for arg in args:\n")
# ESCAPE SEQ TAB REQUIRED OVER tab KEY
f.write("\tprint 'Welcome to CiscoLive2015 ' + arg\n")
f.close()
exit
```

```
show file bootflash:scripts/CiscoLive2015.py
source CiscoLive2015.py <your_name>
Welcome to CiscoLive2015 <your_name>.
```

## 3

Import the math module and calculate the area of a circle.

```python
import math
radius = 10
circ_area = math.pi * radius ** 2
circ_area
314.1592653589793
```

## 4 

Create a function called _areaCircle_ that will calculate the area of a circl when given that argument radius.

```python
def areaCircle(radius):
        return math.pi * radius ** 2

areaCircle(10)
# OUTPUT
# 314.1592653589793
```

## 5

Create a for-loop that calculates the area of a circle for 3 different random radius. Your integer values will be different

```python
from random import randint
radius = []
for iter in range(3):
	radius.append(randint(1,10))

type(radius), radius
# OUTPUT
# (<type 'list'>, [7, 4, 4])

for integer in radius:
	areaCircle(integer)
# OUTPUT
# 153.93804002589985
# 50.26548245743669
# 50.26548245743669
```

## 6

Create a function that converts an IPv4 decimal address to an IPv6 hexadecimal address.

```python
ipv4_addr = "10.7.0.1"
def getIPv6(ipv4addr):
    ipv6address = ["2001:"]
    hexadecimal = []
    ipv4_addr = ipv4addr.split('.')
    for item in ipv4_addr:
        hexadecimal.append(hex(int(item))[2:].zfill(2))
    for i, j in zip(hexadecimal[::2], hexadecimal[1::2]):
        ipv6address.append(":" + i + j)
    return "".join(ipv6address)

print getIPv6(ipv4_addr)

# CiscoLive_N7K# >>> print getIPv6(ipv4_addr)
# OUTPUT
# 2001::0a07:0001
```

## 7 

A _**convertipv4.py**_ script file was created in the _bootflash:scripts_ and it can be imported as a module and used in your code. You can call the method _'getIPv6'_ to convert an IPv4 address.

```python
# convertipv4.py
#!/usr/bin/env python
def getIPv6(ipv4addr):
    ipv6address = ['2001:']
    hexadecimal = []
    ipv4_addr = ipv4addr.split('.')
    for item in ipv4_addr:
        hexadecimal.append(hex(int(item))[2:].zfill(2))
    for i, j in zip(hexadecimal[::2], hexadecimal[1::2]):
        ipv6address.append(':' + i + j)
    return ''.join(ipv6address)
```

```python
from convertipv4 import getIPv6
getIPv6("10.7.0.1")
'2001::0a07:0001'
```
