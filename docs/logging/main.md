# Loggers

## Log Message

Logging messages are stored with the following values.

### key

Keys are defined with the uuid4 values.  This way we can avoid any dupliate records in the index.

### level

This defines what type of event took place.  Common ones are as follows:  

Information = The Service came back online
Warning     = The Service just went offline
Error       = The service has been offline and not come back

### Message

This gives you a bit more information on what took place.

### Address

We record the address that was given with the event.  If you are tracking google.com with ICMP we will take the address that was given.

### Protocol

This will state the Protocol that was used to monitor the node.  See Documentation of Protocols to get more information.

### Time

This contains when the event took place.
