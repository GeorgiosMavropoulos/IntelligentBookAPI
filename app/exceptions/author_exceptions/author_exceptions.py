##this file contains exception classes for author
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler
#first exception class author name uniqueness
class DuplicateAuthorxception(ExceptionServiceHandler):
    def __init__(self,message: str ="There is another author registered with that name"):
        super().__init__(status_code=409,message=message, code="Duplicate author")
   

##author not found exception
class AuthorNotFoundException(ExceptionServiceHandler):
    def __init__(self,message: str ="The author you are looking for does not exist"):
            super().__init__(status_code=404,message=message, code="Author not found")
   