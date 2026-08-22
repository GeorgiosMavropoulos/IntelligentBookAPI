#import all ther required modules
from fastapi import APIRouter, Depends,  status
from ...database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession 
from ...services.publisher_service import PublisherService, PublisherCreate, PublisherUpdate
from ...schemas.publisher_schema import PublisherResponse


#initialize the router 
router = APIRouter(prefix="/publishers", tags=["Publishers"])

#helper function to instantiate the service with active db session
def get_publisher_service(
    db: AsyncSession = Depends(get_db)
) -> PublisherService:
    return PublisherService(db)



#create publisher post route
@router.post('/',status_code=status.HTTP_201_CREATED)
#method to create the publisher
async def create_publisher(publisher:PublisherCreate,publisher_service = Depends(get_publisher_service)):
    #call the create method from publisher service
    new_publisher = await  publisher_service.create_publisher(publisher)
    #return the result
    return new_publisher


#get router
@router.get('/',status_code=status.HTTP_200_OK)
#method to get the publishers
async def get_publishers(skip: int = 0, limit: int = 10,publisher_service = Depends(get_publisher_service)):
  #use the get method to retrieve items
  publishers = await publisher_service.get_all_publishers(skip,limit)

  #return the result
  return publishers


#get publisher by id
@router.get('/{id}',status_code=status.HTTP_200_OK)
#method to retrieve the publisher
async def get_publisher(id:int,publisher_service = Depends(get_publisher_service)):
   #use the get method to retrieve items
   publisher = await publisher_service.get_publisher_by_id(id)
   #return the result
   return publisher



#get publisher by name
@router.get('/name/{publisher_name}',status_code=status.HTTP_200_OK)
#method to retrieve the publisher
async def get_publisher(publisher_name:str,publisher_service = Depends(get_publisher_service)):
   #use the get method to retrieve items
   publisher = await publisher_service.get_publisher_by_name(publisher_name)
   #return the result
   return publisher



#update publisher routerS
@router.put('/{publisher_id}',status_code=status.HTTP_201_CREATED)
#method to update the publisher
async def update_publisher(publisher: PublisherUpdate,publisher_id:int,publisher_service = Depends(get_publisher_service)):
   #call the service method to update the publisher\
   update_publisher = await publisher_service.update_publisher(publisher_id,publisher)

   #return the result
   return update_publisher
   
