###this file contains tools (methods) which allow the agent to interact with the database and the api
#import the Book service
from ...services.book_service import BookService
from sqlalchemy.ext.asyncio import AsyncSession


#create the class agent tools
class AgentTools():
     def __init__(self, db: AsyncSession): #create a db instance
        self.book_service = BookService(db)
    
    #create the tool which calls the get book by title method from the bookservcie
     async def book_search(self, book_title):
        #call the method from book service
        book = await self.bookService.get_books_by_title(book_title)

        return book

        
