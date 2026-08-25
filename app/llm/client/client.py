
from ollama import AsyncClient #import ollama lib to connect with ollama. this library handles the connection with localhost's url etc
#import the agent's prompt
from ..component.agent_component import AgentPrompts
##import tools to access the methods the agent will use
from ..tools.tools import AgentTools
#import tool definition
from ..component.agent_component import AgentToolCalling
##import respense and chat request classes from agent_schema
from ..schema.agent_schema import ChatRequest, ChatResponse
agent = AsyncClient(host="http://localhost:11434") ##define the url the agent listens


class AgentConnection():
     def __init__(self, client: AsyncClient,agent_tool_call:AgentToolCalling): ##initialize an async client connection with constructor
        self.client = client   
        self.agent_tool_call = agent_tool_call
  

    #create a function which connects with hermes
     async def message_agent(self,request:ChatRequest) -> ChatResponse:
        #try-except to handle errors
        try:

            #initialize messages array
            messages = [{ "role": "system","content": AgentPrompts.agent_prompt()}, {"role":  "user","content": request.message}]
                    
            #interact with ollama agent through chatting
            ollama_response= await self.call_agent(messages)       
                    
            agent_reply = ollama_response.message.content   
          
            #call the method to handle tool calls if agent has to call a tool
            if ollama_response.message.tool_calls:
             ollama_response = await  self.handle_tool_calls(messages,ollama_response)

             agent_reply = ollama_response.message.content                    
                                                                            

            #return as ChatResponse object
            return ChatResponse(response=agent_reply)
        
        except  Exception as e:
            #return an error if connections fails
            return ChatResponse(response=f"Agent failed to respond:{str(e)}")




     #helper method to handle request and response    
     async def call_agent(self,messages):
        #create a variable and delegate the chat method from ollama package
        ollama_response = await self.client.chat(model="hermes3:8b",messages = messages, tools =AgentToolCalling.agent_search_book_definition() #provide the agent the search book definition
         )
        
        #append ollama_response at messages
        messages.append(ollama_response.message)
        #return the response
        return ollama_response

     #helper method to handle tool calls
     async def handle_tool_calls(self,messages, ollama_response):
         #if tool call exist extract the tool
      if ollama_response.message.tool_calls:
        #use a for loop to iterate through tools and messages
        for tool in ollama_response.message.tool_calls:
         tool_name = tool.function.name
         arguments=tool.function.arguments
         
         #assign arguments as a book title
         book_title = arguments["book_title"]
                           
         #use the method from AgentTools to search for the book
                           
         result= await self.agent_tool_call.agent_search_book(tool_name,book_title)
         ##append the result if it's not none in messages
         if result is not None: 
            messages.append({
              "role": "tool",
              "tool_name": tool_name,
               "content": str(result)
               })
         
              #create the second chat call
        ollama_response = await self.client.chat(
         model="hermes3:8b",
         messages=messages
        )

         #return the response
        return ollama_response
         

