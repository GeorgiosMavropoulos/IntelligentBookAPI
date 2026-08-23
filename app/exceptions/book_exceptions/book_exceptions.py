##this file contains exception classes for book
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler
#first exception class ISBN uniqueness
class DuplicateISBNException(ExceptionServiceHandler):
     def __init__(self,message: str ="There is another book registered with the same ISBN"):
            super().__init__(status_code=409,message=message, code="Duplicate ISBN")

##book not found exception
class BookNotFoundException(ExceptionServiceHandler):
    def __init__(self,message: str ="The book you are looking for does not exist"):
                super().__init__(status_code=404,message=message, code="Book Not Found")


#publisher does not exist
class PublisherNotFound(ExceptionServiceHandler):
    def __init__(self,message: str ="The publisher you are looking for does not exist"):
                    super().__init__(status_code=404,message=message, code="Publisher Not Found")