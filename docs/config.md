# NetworkMonitor - Configuration

## How to get started

At the root of the program you will find example.json and example.yaml.  Make a copy of the files and name it how you want.  You can use either format with NetworkMonitor.

## Layout

### SleepInterval

This tells the application how long it should wait before it checks all the nodes again. Recomendation is to leave it around 5 minutes.  If you go any lower at this time you could be flooding a node with way too much traffic and make things worse.

### Protocols

These are protocol spific variables

#### ICMP

For ICMP we will wait 1 second before we move on to the next node.  In test this gave the best responce time.

### Nodes

For NetworkMonitor to correctly monitor a node you will need the following values as a minimum.

#### Name

This is a human readable name.  If you use another term for a node you can use that here.  This is just for the operator to know what it is.

#### Address

This is the value that will be used to monitor the desires node.  Make sure the value can be used manually before asking NetworkMonitor to watch it for you.

#### Protocol

Currently it supports the following protocols  

* ICMP (ping)
* HTTP:Get
* HTTP:Post

With HTTP requests you can define the port within the address field.  https:\\exchange.contoso.com:433. as a quick example.

#### Required

Tell Networkmonitor true if you are monitoring your gateway node.  A device that is required to be online and working to get outbound.

Tell it false if you are monitoring a service that does not require to be online to have proper network connectitity.
