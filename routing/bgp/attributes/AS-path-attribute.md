# AS-Path Attribute

An edge router modifies the AS-path attribute every time information about a particular IP subnet passes over an AS border. When a router first originates a route in BGP, the AS-path attribute is empty. The local AS number is prepended to the AS path each time that the route crosses an AS boundary.

* The AS-path attribute is empty when a local route is inserted into the BGP table.
* The AS number of the sender is prepended to the AS-path attribute when the routing update crosses the AS boundary.
* An AS that receives routing information with its own AS number in the AS path silently ignores the information. 

## There are several consequences of AS-path attribute behavior

* When you examine BGP routes, the AS path can be interpreted as the sequence of autonmous syste,s that must be passed through to reach the indicated network. The AS originally injected the route into BGP is always found at the right-most end of the AS path.
* It is easy to distinguish local routes from routes that have been received from other autonomous systems. BGP routes with an empty AS path were injected into BGp from within the local AS.

### AS-Path Attribute Example
