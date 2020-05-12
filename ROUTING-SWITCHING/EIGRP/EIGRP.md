# Enhanced Interior Gateway Routing Protocol - EIGRP

## Quick Configuration

### Named EIGRP Quick Config

```
# ENTER PRIVILEGED EXEC MODE
conf t
router eigrp CCIE
add ipv4 as 1
# /24 wildcard mask
network 1.0.0.0 0.255.255.255
# advertise /32
# network 7.7.7.7
!
!
# VALIDATE
do sho run | sec route
# EXIT ROUTER-CONFIG MODE
end
```

## Don't understand? Need an explanation?

Please refer to my [FAQ](https://github.com/gil-ryan/ultimate-cli-handbook#learn-more-faq) portion of the handguide!
