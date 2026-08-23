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

