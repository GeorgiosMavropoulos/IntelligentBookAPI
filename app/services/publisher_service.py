from ..models import publisher_model
from ..schemas.publisher_schema import PublisherCreate, PublisherUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,delete

from sqlalchemy.exc import IntegrityError
from ..exceptions.publisher_exceptions.publisher_exceptions import DuplicatePublisher

#create the publisher service
class PublisherService:
    def __init__(self,db:AsyncSession):
        self.db = db


    #create publisher exception
    async def create_publisher(self,publisher:PublisherCreate):
        try:
         #delegate into a a variable model's attributes
         publisher = publisher_model(publisher =publisher.publisher)

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
           raise DuplicatePublisher(publisher.publisher) from e
        #return general exception
        except:
           await self.db.rollback()
           raise

