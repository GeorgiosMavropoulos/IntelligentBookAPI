##exceptions for authors_books service
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler

#exception for duplicate entry
class DuplicateAuthorBookEntry(ExceptionServiceHandler):
    def __init__(self,message: str ="There is another entry with the same book and author"):
                    super().__init__(status_code=409,message=message, code="Duplicate entry")


#not found exception
class NotFound(ExceptionServiceHandler):
   def __init__(self,message: str ="Relationship wasn't found"):
                   super().__init__(status_code=404,message=message, code="Relationship not found")