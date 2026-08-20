import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
#load the .env file
load_dotenv()

#import the Database's url from .env
DATABASE_URL = os.getenv("DATABASE_URL") 

if DATABASE_URL is None:
    raise Exception("Error. Database URL is missing")

#create async engine
engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True) # enable echo to read sql queries in the terminal


#create session
SessionLocal = async_sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)

#create get_db method as dependency for fastapi
async def get_db():
    
     async with SessionLocal() as session:
        yield session #create a new session for each request
    