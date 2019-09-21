

class NetworkMonitorException(Exception):
    """
    All NetworkMonitor excpetions base from this
    """

class InvalidProtocol(NetworkMonitorException):
    """
    Raised when user enters a protocol that is not supported by NetworkMonitor
    """

# Log Errors
class InvalidLogType(NetworkMonitorException):
    """
    Raised when the user tries to use a illegal logging type.  Currently supports sqlite.
    """

class FailedToLogMessage(NetworkMonitorException):
    """
    Raised when the requested log does not get added to the records.
    """

###

# Config Loader
class InvalidNodeConfiguration(NetworkMonitorException):
    """
    Raised when a user is missing one of the required parameters.
    Json nodes require Name, Address and Protocol
    """

class InvalidConfigFileType(NetworkMonitorException):
    """
    Raised when the configuration file that was passed is not a .yaml or .json file
    """

class FailedToLoadConfigurationFile(NetworkMonitorException):
    """
    Raised when we run into a problem loading the requested config file.
    """

class FailedToGenerateNewFile(NetworkMonitorException):
    """
    Raised when generating a new config file via CLI.
    If a file exists already? raise
    """
