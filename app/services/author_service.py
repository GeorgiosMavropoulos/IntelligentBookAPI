#import book model
from ..models import author_model
from ..schemas.author_schema import AuthorCreate, AuthorUpdate, AuthorResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,delete
from sqlalchemy.exc import IntegrityError
from ..exceptions.author_exceptions.author_exceptions import DuplicateAuthorxception,AuthorNotFoundException


#create author service class
class AuthorService:
     def __init__(self, db:AsyncSession):
        self.db = db


    #create author method
     async def create_author(self,author:AuthorCreate):
      #try except for error handling
      try:
         #create a  new variable and delegate model's attributes
         new_author = author_model(author=author.author)

         #add the author to the db
         self.db.add(new_author)
         #commit the change
         await self.db.commit()
         #refresh
         await self.db.refresh(new_author)
         #return the new author objct
         return new_author

      ##handle exception for duplicate author's name
      except IntegrityError as e:
         await self.db.rollback()
         raise DuplicateAuthorxception(author.author) from e
      except:  
         #return an exception and rollback the action
         await self.db.rollback()
         raise


      #get all authors
     async def get_all_authors(self, skip: int = 0, limit: int = 100):
         #create a variable to delegate to it the result
         result = await self.db.execute(select(author_model.Author).offset(skip).limit(limit))

         #return the result
         return result.scalars().all


     #get author by id 
     async def get_author_by_id(self, author_id:int):
        #create a variable to delegate to it the result
         result = await self.db.execute(select(author_model.Author).where(author_model.Author.id == author_id))

          #check if author exists
         author =  result.scalar_one_or_none()

         #return an error message if author does not exist
         if author is None:
            raise AuthorNotFoundException("Author does not exist")

         #return author if exists
         return author

        
     #get author by name function
     async def get_author_by_name(self,author_name:str):
      #create a variable to delegate to it the result
      result = await self.db.execute(select(author_model.Author).where(author_model.Author.author == author_name))

      #check if author exists
      author =  result.scalar_one_or_none()
       #return an error message if author does not exist
      if author is None:
       raise AuthorNotFoundException("Author does not exist")

       #return author if exists
       return author
      
