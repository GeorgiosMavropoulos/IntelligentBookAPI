##this file contains agent's logic, @tools, prompt method etc
##import tools to access the methods the agent will use
from ..tools.tools import AgentTools
#class prompts
class AgentPrompts:
   
    #create a method to pass agent's prompt
    def agent_prompt():
     instructions = "You are a helpful AI assistant for a bookstore." \
     "Your role is to help users with questions about books and information available through the bookstore."\
     "Follow these rules:"\
     "1. When the user asks for information about a specific book, use the `book_search` tool first to retrieve the available bookstore data."\
     "2. Use the information returned by the tool to answer the user clearly and concisely."
     "3. If the book does not exist in the database and you get the message 'Book does not exist in our database', just provide the user accurate information based on your knowledge.Never make up something." \
     "4. If you can't find relevant information just say the user the I cannot find relevant information"\
     "5. If they ask you something irrelevant, remind them that you are a book store AI assistant only. You can use this phrase:`I am sorry my fellow nerdy, I am here to provide information regarding books, only. If you need a general assistant go to chat gpt,lol`"
     "6.Always prioritize accurate information from the bookstore tools over your own knowledge."\
     "7.You can only answer about books. Tell them to get the fuck of if they ask something else"
     #return the prompt
     return instructions


class AgentToolCalling:

    #create an agent tools instance method
    def __init__(self,db):
       self.db = AgentTools(db)

    #notify agent which methods it can use
    def agent_search_book_definition():
   #create search book definition
      tools = [
        {
            "type": "function",
            "function": {
                "name": "book_search",
                "description": "Search the bookstore database for a book by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "book_title": {
                            "type": "string",
                            "description": "The title of the book to search for."
                        }
                    },
                    "required": ["book_title"]
                }
            }
        }
    ]
      return tools


    #method to validate if there's a method for the requested tool name
    async def agent_search_book(self,tool_name:str,book_title:str):
       
       
       #validate if tool_name == book_search
       if tool_name == 'book_search':
          #call book_search method
        tool = await  self.db.book_search(book_title)

        #return the tool
        return tool
       



     
     
       
       
