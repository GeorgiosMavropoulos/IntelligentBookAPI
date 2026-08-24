##this file contains the post endpoint to interact with the agent
from fastapi import APIRouter, Depends, HTTPException, status
from ollama import AsyncClient
from .client import AgentConnection,  ChatRequest #import messag agent


#create router instance
router = APIRouter(prefix="/chat_request", tags=["Chat_request"])
#create a dependency function 
  #create a helper function which initialized the agent
def get_agent() -> AgentConnection:
      client = AsyncClient()
      return AgentConnection(client)

#create the post class to send requests and receive responses
@router.post('/',status_code=status.HTTP_200_OK)
#method to fetch the chat request and responses method from client.py
async def agent_request(request:ChatRequest,agent:AgentConnection=Depends(get_agent)):

    #call the method to send and receive message
    chat = await agent.message_agent(request)

    #return the resposne
    return{"data":chat}
