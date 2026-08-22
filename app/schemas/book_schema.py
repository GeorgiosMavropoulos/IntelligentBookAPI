from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from datetime import datetime
from typing import Annotated
from typing import Optional


##create types using annotated in order not to repeat myself later
BookTitle = Annotated[str, Field(min_length=1, max_length=255,description="Book title")]
BookYear = Annotated[int, Field(ge=1000, le=2100,description="Publication year")]
BookISBN = Annotated[str, Field(min_length=10, max_length=13,pattern=r"^(\d{10}|\d{13})$", 
        description="ISBN must be exactly 10 or 13 digits long")]
BookPrice = Annotated[Decimal, Field(ge=1,max_digits=10, decimal_places=2, description="Price must be > than 1")]
BookGenre = Annotated[str, Field(min_length=1,max_length=60, description="Book's genre")]
BookLanguage = Annotated[str, Field(min_length=1,max_length=60,description="Book's language")]
BookDescription = Annotated[str,Field(min_length=1,max_length=500, description="Book's description")]
BookPublisher_Id = Annotated[int, Field(ge=1, description="The ID of the existing publisher")]
BookStock = Annotated[int, Field(ge=0, description="Book's quantity")]

#create a book base class
class BookBase(BaseModel):
    title: BookTitle
    year: BookYear
    isbn: BookISBN
        
    price: BookPrice
    genre: BookGenre
    language: BookLanguage


#create book 
class BookCreate(BookBase):
      description: BookDescription
    # Pass the database publisher_id foreign key during creation
      publisher_id: BookPublisher_Id

    #pass stock
      stock: BookStock 

#book update
class BookUpdate(BookBase):
    title: Optional[BookTitle]   = None
    year: Optional[BookYear] = None
    isbn: Optional[BookISBN]  = None
    price: Optional[BookPrice] = None
    description: Optional[BookDescription]  = None

    stock: Optional[BookStock]  = None
    genre: Optional[BookGenre]  = None
    language: Optional[BookLanguage]  = None
    publisher_id: Optional[BookPublisher_Id]  = None
       
     

#book response
class BookResponse(BookBase):
     id: int
     #tell pydantic to read ORM models
     model_config = ConfigDict(from_attributes=True)
     #return from server created and updated date
     created_at: datetime
     updated_at: datetime