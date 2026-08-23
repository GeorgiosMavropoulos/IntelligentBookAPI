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



#get author by id endpoint

@router.get('/{id}',status_code=status.HTTP_200_OK)
#method to retrieve the author
async def get_author(id:int,author_service = Depends(get_author_service)):
   #use the get method to retrieve items
   author = await author_service.get_author_by_id(id)
   #return the result
   return {"message":"Success", "data":author}



#get author by name
@router.get('/name/{author_name}',status_code=status.HTTP_200_OK)
#method to retrieve the author
async def get_author_by_name(author_name:str,author_service = Depends(get_author_service)):
   #use the get method to retrieve items
   author = await author_service.get_author_by_name(author_name)
   #return the result
   return {"message":"Success", "data":author}



#update author endpoint
@router.put('/{author_id}',status_code=status.HTTP_200_OK)
#create the method to update author's data
async def update( author:AuthorUpdate, author_id:int, author_service = Depends(get_author_service)):
    #use the update method from author_service.py to update the data
    update = await author_service.update_author(author,author_id)

    #return the result with a success message
    return {"message":"The author has been updated with success","data":author}


#delete author endpoint
@router.delete('/{author_id}',status_code=status.HTTP_204_NO_CONTENT)
#METHOD to delete the author
async def delete(author_id:int, author_service = Depends(get_author_service)):
    #use the delete method from author service
    delete = await author_service.delete_author(author_id)

    #return the result with a message of success
    return{"message":"The author has been deleted with success","data":delete}

