###this is the main entry point
#import get_db
from .database.database import get_db
from sqlalchemy import text 
#import fast api
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession 
#import  the router
from app.routes.book_routes import book_routes
##create an instance of fastAPI
app = FastAPI()

#register books router
app.include_router(book_routes.router)

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
         

    

    