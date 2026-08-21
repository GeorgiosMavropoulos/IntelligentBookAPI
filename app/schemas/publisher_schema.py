from pydantic import BaseModel, Field, ConfigDict

from typing import Annotated


#create annotations
PublisherName = Annotated[str, Field(min_length=1, max_length=50, description="Publisher's name")]


#Publisher base class
class PublisherBase(BaseModel):
     publisher: PublisherName


#CREATE Publisher
class PublisherCreate(PublisherBase):
    pass

#Update Publisher 
class PublisherUpdate(PublisherBase):
     publisher: PublisherName | None = None #optional update



#Publisher response
class PublisherResponse(PublisherBase):
    id: int
    
     #tell pydantic to read ORM models
    model_config = ConfigDict(from_attributes=True)