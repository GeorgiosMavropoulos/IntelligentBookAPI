##exceptions for authors_books service

#exception for duplicate entry
class DuplicateAuthorBookEntry(Exception):
    pass


#not found exception
class NotFound(Exception):
    pass