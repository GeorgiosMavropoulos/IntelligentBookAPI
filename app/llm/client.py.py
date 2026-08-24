
from ollama import AsyncClient #import ollama lib to connect with ollama. this library handles the connection with localhost's url etc


##import respense and chat request classes from agent_schema
from .agent_schema import ChatRequest, ChatResponse
#create a function which connects with hermes
async def message_agent(request:ChatRequest) -> ChatResponse:
    #try-except to handle errors
    try:
        #connect with ollama agent
        ollama_response= await AsyncClient().chat(model="hermes3:8b",messages=[{"role":"user","content":request.message}])

        #extract agent's response
        agent_reply = ollama_response['message']['content']
        #return as ChatResponse object
        return ChatResponse(response=agent_reply)
      
    except  Exception as e:
        #return an error if connections fails
        return ChatResponse(response=f"Agent failed to respond:{str(e)}")


