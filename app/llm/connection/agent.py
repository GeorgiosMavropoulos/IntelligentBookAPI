#this file contains the method which intializes the connection with the localhost where ollama listens  #create a helper function which initialized the agent
#import the agent connection class
from ..client.client import AgentConnection, AsyncClient

from sqlalchemy.ext.asyncio import AsyncSession
from ...database.database import get_db
from ..component.agent_component import AgentToolCalling
from fastapi import Depends
def get_agent(db: AsyncSession = Depends(get_db)) -> AgentConnection:
      client = AsyncClient(host="http://localhost:11434")
      #create a db instance for tool calls
      agent_tool_call = AgentToolCalling(db)
      return AgentConnection(client,agent_tool_call)
