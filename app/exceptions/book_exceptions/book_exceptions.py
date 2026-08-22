##this file contains exception classes for book

#first exception class ISBN uniqueness
class DuplicateISBNException(Exception):
    pass

##book not found exception
class BookNotFoundException(Exception):
    pass


#publisher does not exist
class PublisherNotFound(Exception):
    pass