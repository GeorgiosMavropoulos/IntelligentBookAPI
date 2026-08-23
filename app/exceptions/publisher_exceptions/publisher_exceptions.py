#this file contains exception classes for publisher
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler

class DuplicatePublisher(ExceptionServiceHandler):
    def __init__(self,message: str ="There is another publisher registered with the same name"):
                super().__init__(status_code=409,message=message, code="Duplicate publisher")


class PublisherNotFound(ExceptionServiceHandler):
    def __init__(self,message: str ="There publisher you are looking for does not exist"):
                super().__init__(status_code=409,message=message, code="Publisher not found")