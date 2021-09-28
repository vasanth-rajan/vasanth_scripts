class CustomError(Exception):
    """Base class for other exceptions"""

class HTTPServerError(CustomError):
    """Raised when response error code is 5XX"""

class HTTPClientError(CustomError):
    """Raised when response error code is 4XX"""
