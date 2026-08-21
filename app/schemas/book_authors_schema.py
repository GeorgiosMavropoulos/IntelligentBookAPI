from pydantic import BaseModel, ConfigDict




#create book authors class
class BookAuthorsBase(BaseModel):
  book_id: int
  author_id: int


#create book authors
class CreateBookAuthors(BookAuthorsBase):
  pass



#BookAuthors response
class BookAuthorsResponse(BookAuthorsBase):
   #tell pydantic to read ORM models
   model_config = ConfigDict(from_attributes=True)