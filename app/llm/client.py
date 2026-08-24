
from ollama import AsyncClient #import ollama lib to connect with ollama. this library handles the connection with localhost's url etc
#import the agent's prompt
from .agent_component import AgentPrompts


##import respense and chat request classes from agent_schema
from .agent_schema import ChatRequest, ChatResponse
agent = AsyncClient(host="http://localhost:11434") ##define the url the agent listens

class AgentConnection():
     def __init__(self, client: AsyncClient): ##initialize an async client connection with constructor
        self.client = client   
  

    #create a function which connects with hermes
     async def message_agent(self,request:ChatRequest) -> ChatResponse:
        #try-except to handle errors
        try:
            #connect with ollama agent
            ollama_response= await self.client.chat(model="hermes3:8b", messages = [
    {
        "role": "system",
        "content": AgentPrompts.agent_prompt()
    },
    {
       "role":  "user",
       "content": request.message
    }
])

            #extract agent's response
            agent_reply = ollama_response['message']['content']
            #return as ChatResponse object
            return ChatResponse(response=agent_reply)
        
        except  Exception as e:
            #return an error if connections fails
            return ChatResponse(response=f"Agent failed to respond:{str(e)}")


