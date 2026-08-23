##this file contains exception classes for book
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler
#first exception class ISBN uniqueness
class DuplicateISBNException(ExceptionServiceHandler):
    pass

##book not found exception
class BookNotFoundException(ExceptionServiceHandler):
    pass


#publisher does not exist
class PublisherNotFound(ExceptionServiceHandler):
    pass