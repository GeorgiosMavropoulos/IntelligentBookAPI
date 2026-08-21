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
         return result.scalars().all()


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
      


     #update author function
     async def update_author(self,author:AuthorUpdate,author_id:int):
        #try except for error handling
         try:
          #try to retrieve the requested author to see if exists
          result = await self.db.execute(select(author_model.Author).where(author_model.Author.id == author_id))

          #retrieve the result from the object
          update_author = result.scalar_one_or_none()

          #return an error message if author not found
          if update_author is None:
             raise AuthorNotFoundException("Cannot find the requested author")

          update_data = author.model_dump(exclude_unset=True) #use model dump since not all attributes should be changed
          #if all goes well update the author's name
          for field, value in update_data.items():
             setattr(update_author,field,value)

          #commit the action
          await self.db.commit()
          #refresh
          await self.db.refresh(update_author)

          #return the author
          return update_author
         
         #return an exception if author's name is duplicate
         except IntegrityError as e:
          await self.db.rollback() #roll back the action if update fails
          raise DuplicateAuthorxception(author.author) from e
         
         except:
            await self.db.rollback() #roll back the action if update fails
            raise




         #function to delete author
     async def delete_author(self,author_id:int):
          try:

           #create a variable to delegate delete method
           delete_author = await self.db.execute(delete(author_model.Author).where(author_model.Author.id == author_id))

            #create a variable delete_rows to access row count
           delete_rows = delete_author.rowcount
           #return an error message if no row got deleted
           if delete_rows <= 0:
              raise AuthorNotFoundException("This author does not exist")

           #if all goes well commit
           await self.db.commit()
           #return author objct
           return delete_author

          except:
                 #rollback
                 await self.db.rollback()
                 raise
        