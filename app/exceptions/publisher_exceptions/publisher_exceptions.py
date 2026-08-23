#this file contains exception classes for publisher
#import the exception handler I wrote
from ..base_exception_class import ExceptionServiceHandler

class DuplicatePublisher(ExceptionServiceHandler):
    pass


class PublisherNotFound(ExceptionServiceHandler):
    pass