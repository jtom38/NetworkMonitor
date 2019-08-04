

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

class InvalidConfigFileType(NetworkMonitorException):
    """
    Raised when the configuration file tha was passed is not a .yaml or .json file
    """