###this is the main entry point
#import get_db
from .database.database import get_db
from sqlalchemy import text 
#import fast api
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession 
#import  the routers
from .routes.book_routes.book_routes import router as book_router
from .routes.publisher_routes.publisher_routes import router as publisher_router
from .routes.author_routes.author_routes import router as author_router
from .routes.authors_books.authors_books import router as author_book_router
import os
##import the exception handler 
from .exceptions.base_exception_class import ExceptionServiceHandler, exception_service_handler

#import agent router 
from .llm.agent_routes import router as agent_router
##create an instance of fastAPI
app = FastAPI()


from .models import book_model, publisher_model, author_model, book_authors_model

##register exception handler
app.add_exception_handler(ExceptionServiceHandler, exception_service_handler)



#register books router
app.include_router(book_router)

#register publisher's router
app.include_router(publisher_router)

#register author's router
app.include_router(author_router)

#register author book router
app.include_router(author_book_router)


#register the agent
app.include_router(agent_router)

#method with db's smoke test
async def test_db_connection(db:AsyncSession):
    
        #create a request to DB
        await db.execute(text('Select 1'))

        #if all goes well return a message indicating the db works fine
        return{"status":"healthy","message": "Application and Database are up and running"}
          

@app.get('/health') #create a test route to validate that the app is working
async def root(db: AsyncSession = Depends(get_db)):
    try:
       db_status =  await test_db_connection(db)
       return db_status
    except:
         raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,detail='Database is unavailable')
         

    

    