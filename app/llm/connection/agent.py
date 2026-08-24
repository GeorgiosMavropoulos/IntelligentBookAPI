#this file contains the method which intializes the connection with the localhost where ollama listens  #create a helper function which initialized the agent
#import the agent connection class
from ..client.client import AgentConnection, AsyncClient
def get_agent() -> AgentConnection:
      client = AsyncClient(host="http://localhost:11434")
      return AgentConnection(client)
