###create 2 classes for chat request and chat response. those classes will interact with the agent
from pydantic import BaseModel


#create the first class (chat request)
class ChatRequest(BaseModel):
    message:str



#chat response class
class ChatResponse(BaseModel):
    response:str