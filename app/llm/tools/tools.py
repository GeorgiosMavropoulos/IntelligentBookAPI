###this file contains tools (methods) which allow the agent to interact with the database and the api
#import the Book service
from ...services.book_service import BookService


#create the class agent tools
class AgentTools:

    #create the tool which calls the get book by title method from the booksercvie