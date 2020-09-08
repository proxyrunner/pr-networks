# Postman Collection

## Login to APIC

> https://{{apic}}/api/aaaLogin.json

### Body

Raw parameters:

```
{ "aaaUser" : { "attributes": {"name":"{{username}}","pwd":"{{password}}" } } }
```
