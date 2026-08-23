##exceptions for authors_books service
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler

#exception for duplicate entry
class DuplicateAuthorBookEntry(ExceptionServiceHandler):
    pass


#not found exception
class NotFound(ExceptionServiceHandler):
    pass