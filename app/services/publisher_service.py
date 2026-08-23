from ..models.publisher_model import Publisher
from ..schemas.publisher_schema import PublisherCreate, PublisherUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,delete

from sqlalchemy.exc import IntegrityError
from ..exceptions.publisher_exceptions.publisher_exceptions import DuplicatePublisher, PublisherNotFound

#create the publisher service
class PublisherService:
    def __init__(self,db:AsyncSession):
        self.db = db


    #create publisher exception
    async def create_publisher(self,publisher:PublisherCreate):
        try:
         #delegate into a a variable model's attributes
         publisher = Publisher(publisher =publisher.publisher)

         #search if there's another publisher with the same name registerd
         publisher_exists = await self.db.execute(select(Publisher).where(Publisher.publisher == publisher.publisher))
         #extract the orm objct from result
         requested_publisher = publisher_exists.scalar_one_or_none()

         #return a duplicate publisher exception if publisher already exists
         if requested_publisher is not None:
            raise DuplicatePublisher() 

         #add the puiblisher
         self.db.add(publisher)
         #commit into the db
         await self.db.commit()
         #refresh
         await self.db.refresh(publisher)

         #return publisher
         return publisher

        #return exception for duplicate publisher
        except IntegrityError as e:
           await self.db.rollback()
           raise 
        #return general exception
        except:
           await self.db.rollback()
           raise

    #get all publishers method
    async def get_all_publishers(self, skip: int = 0, limit: int = 100):
       #execute the query and delegate into a variable the result
       publishers = await self.db.execute(select(Publisher).offset(skip).limit(limit))

       #return the publishers
       return publishers.scalars().all()


    #get publisher by id method
    async def get_publisher_by_id(self,publisher_id:int):
     
       #execute the query and delegate the result 
       get_publisher = await self.db.execute(select(Publisher).where(Publisher.id == publisher_id ))

       ##get the result using scalars
       publisher = get_publisher.scalar_one_or_none()

       #return an error message if publisher doesn't exist
       if publisher is None:
          raise PublisherNotFound()


       #return publisher if all goes well
       return publisher

    #get publisher by its name
    async def get_publisher_by_name(self,publisher_name:str):
       #create a variable to delegate to it the result
       get_publisher  = await self.db.execute(select(Publisher).where(Publisher.publisher == publisher_name))

       ##get the result using scalars
       publisher = get_publisher.scalar_one_or_none()

       
       #return an error message if publisher doesn't exist
       if publisher is None:
          raise PublisherNotFound()


        #return publisher if all goes well
       return publisher

    #update publisher
    async def update_publisher(self,publisher_id:int,publisher:PublisherUpdate):
       #try-except to handle errors
       try:
          #retrieve the requested publisher by their id
          result = await self.db.execute(select(Publisher).where(Publisher.id == publisher_id))

          #use scalars to convert the object
          updated_publisher= result.scalar_one_or_none()

          #return an error message if publisher does not exists
          if updated_publisher is None:
             raise PublisherNotFound()


          #validate if there's another publisher with the same name available if publisher name was given
          if publisher:
             search_publisher = await self.db.execute(select(Publisher).where(Publisher.publisher == publisher.publisher, Publisher.id != publisher_id))

             #extract the orm object from the result
             publisher_exists = search_publisher.scalar_one_or_none()

             #raise the exception if publisher name exists in another row
             if publisher_exists is not None:
                raise DuplicatePublisher()

          #use model dump since not all attributes need to change. now it's one attribute but later we may add more
          update_data = publisher.model_dump(exclude_unset=True)

          #for loop to loop through the attributes and change what it's needed
          for field,value in update_data.items():
             setattr(updated_publisher,field,value)

         #commit the change
          await self.db.commit()
          #refresh
          await self.db.refresh(updated_publisher)

          #return the objct
          return updated_publisher
       #exception if publisher's name is duplicate
       except IntegrityError as e:
          #rollback to cancel the db operation
          await self.db.rollback()
          raise 
       #return a general exception
       except:
          await self.db.rollback()
          raise



       #delete publisher method
    async def delete_publisher(self,publisher_id:int):
       #try-except for error handling
       try:
          #declare a variable to store the result from the deletion query
          publisher_delete = await self.db.execute(delete(Publisher).where(Publisher.id == publisher_id))

          ##create a variable delete_rows to access row count
          deleted_rows = publisher_delete.rowcount

          #return an error message if row count == 0
          if deleted_rows <=0:
             raise PublisherNotFound()

          #if all goes well commit
          await self.db.commit()
        

          #return the result
          return publisher_delete
       except:
           await  self.db.rollback()
           raise