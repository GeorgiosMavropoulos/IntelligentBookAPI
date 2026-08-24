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

          
        
        """Fetch the requested book from the database."""
    
        #call the method from book service
        
        print("BOOK SEARCH title:", book_title)
        book = await self.book_service.get_books_by_title(book_title)
        print("DATABASE RESULT:", book)

        #validate if book is empty or not
        if book:
            return {"data":book}
        else:
            return {"message":"Book does not exist in our database"}


       

        
