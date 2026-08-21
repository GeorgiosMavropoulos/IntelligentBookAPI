from pydantic import BaseModel, Field, ConfigDict

from typing import Annotated

##create types using annotated in order not to repeat myself later
AuthorName = Annotated[str, Field(min_length=1, max_length=50,description="Author's name")]

#Author base class
class AuthorBase(BaseModel):
    author: AuthorName


#CREATE AUTHOR
class AuthorCreate(AuthorBase):
    pass

#Update Author 
class AuthorUpdate(AuthorBase):
    author: AuthorName | None = None #optional update



#Author response
class AuthorResponse(AuthorBase):
    id: int
    author:AuthorName
     #tell pydantic to read ORM models
    model_config = ConfigDict(from_attributes=True)