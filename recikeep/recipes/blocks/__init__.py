from unittest import TestCase


class BlockStartNotFoundException(BaseException):
    pass

class BlockEndNotFoundException(BaseException):
    pass

class BlockIsEmptyException(BaseException):
    pass
