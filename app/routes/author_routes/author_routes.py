 #import all ther required modules
from fastapi import APIRouter, Depends, HTTPException, status
from ...database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession 
from ...services.author_service import AuthorService, AuthorCreate, AuthorUpdate
from ...schemas.author_schema import  AuthorResponse

#initialize the router 
router = APIRouter(prefix="/authors", tags=["Authors"])

#helper function to instantiate the service with active db session
def get_author_service(db:AsyncSession = Depends(get_db)) ->AuthorService:
    return AuthorService(db)



#create author endpoint
@router.post('/',status_code=status.HTTP_201_CREATED)
#method to create an author
async def create(author:AuthorCreate, author_service = Depends(get_author_service)):
    #call the method from service to create the author
    new_author = await author_service.create_author(author)

    #return the result
    return{"message":"Author added with success","data":author}


#get authors endpoint
@router.get('/',status_code=status.HTTP_200_OK)
#Method to fetch authors
async def get_authors(skip:int = 0, limit:int = 100, author_service = Depends(get_author_service)):
    #call the service method to fetch all authors and delegate the result in a variable
    authors = await author_service.get_all_authors(skip,limit)

    #return the result with a success message
    return{"message":"Success","data":authors}

