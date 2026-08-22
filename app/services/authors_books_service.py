#import book and author not found exceptions since I will need to check if book and author actually exist
from ..exceptions.author_exceptions.author_exceptions import AuthorNotFoundException
from ..exceptions.book_exceptions.book_exceptions import BookNotFoundException
from ..exceptions.authors_books_exceptions.authors_books_exceptions import DuplicateAuthorBookEntry
from ..models.book_authors_model import AuthorBooks
from ..schemas.book_authors_schema import CreateBookAuthors
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Boolean
from ..models import author_model, book_model, book_authors_model

#create the class
class AuthorsBooksService:
    def __init__(self,db:AsyncSession):
        self.db = db

        #helper method to search if  author exists
    async def _author_exists(self,author_id) -> bool:
        #query to validate whether given author exists
        search_author = await self.db.execute(select(author_model.Author).where(author_model.Author.id== author_id))

        #get the actual result via scalars
        author = search_author.scalar_one_or_none()

        #return an error if author does not exist
        if author is None:
            return False


        return True #return true if exists


    #function to validate if book exists
    async def _book_exists(self,book_id) -> bool:
        #query to validate whether given author exists
        search_book = await self.db.execute(select(book_model.Book).where(book_model.Book.id == book_id))
        
        #get the actual result via scalars
        book= search_book.scalar_one_or_none()
        
        #return an error if author does not exist
        if book is None:
            return False
        
        
        return True #return true if exists



    #create author books relation method
    async def create_author_books_relation(self,authors_books:AuthorBooks):
        #try-except for error handling
        try:

            #search if given author id matches with an existent author
            if not await self._author_exists(authors_books.author_id): # use author exists method
                raise AuthorNotFoundException("The author does not exist")

            #search if given book id matches with an existent book
            elif not await self._book_exists(authors_books.book_id): # use book exists method
                raise BookNotFoundException("The book does not exist")

            relation = book_authors_model(book_id=authors_books.book_id, author_id=authors_books.author_id)
            #add the relation
            self.db.add(relation)
            #commit the action
            await self.db.commit()
            #refresh th db
            await self.db.refresh(relation)
            #return the relation
            return relation
        except:
            #rollback the action in case of failure
            await self.db.rollback()
            raise




        #method to get the relation
    async def get_authors_books(self,skip:int=0, limit:int = 100):

        #create a variable to delegate the result from select query
        get_books_authors = await self.db.execute(select(book_authors_model.AuthorBooks).offset(skip).limit(limit))

        #use scalars to extract the  result
        books_authors = get_books_authors.scalars().all()

        #return the result
        return books_authors


    #method to get by author's id
    async def get_by_author_id(self,author_id:int):
         #create a variable to delegate the result from select query
         get_books_authors = await self.db.execute(select(book_authors_model).where(book_authors_model.AuthorBooks.author_id == author_id))

         #extract the result
         books_authors = get_books_authors.scalars().all()

         #return an error message if not found
         if books_authors is None:
             raise AuthorNotFoundException("No relations found about the requested author")
         #return the result
         return books_authors



        