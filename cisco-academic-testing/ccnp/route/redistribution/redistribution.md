# Configuring Redistribution

## Introduction

Redistribution is a large and very important topic. One of your customers has aquired another competitor, lets face it, it happens frequently.

### The Need for Redistribution

There will come a time when you face a mix of problems involving routing, typically, supportability is usually the first.

#### Why use simultaneous routing protocols?

* Temporarily  during conversion or migrations
* Application-specific protocol support
* Political boundaries (groups that don't work well together)
* Mismatch between devices (mixed vendor environment)

### Defining Route Restribution

Routes that are learned by other means are selectively redistributed into a routing protocol from one of three sources:

1. Another routing protocol
2. Static routes
3. Directly connected routes

#### Routing loop prevention

Only routes in the routing table are redistributed.
