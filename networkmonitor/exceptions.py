

class NetworkMonitorException(Exception):
    """
    All NetworkMonitor excpetions base from this
    """

class InvalidProtocol(NetworkMonitorException):
    """
    Raised when user enters a protocol that is not supported by NetworkMonitor
    """

class InvalidNodeConfiguration(NetworkMonitorException):
    """
    Raised when a user is missing one of the required parameters.
    Json nodes require Name, Address and Protocol
    """