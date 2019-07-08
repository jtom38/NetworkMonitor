

class NetworkMonitorException(Exception):
    """
    All NetworkMonitor excpetions base from this
    """

class InvalidProtocol(NetworkMonitorException):
    """
    Raised when user enters a protocol that is not supported by NetworkMonitor
    """