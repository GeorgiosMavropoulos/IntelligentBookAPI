###this is the main entry point

#import fast api
from fastapi import FastAPI

##create an instance of fastAPI
app = FastAPI()

#create a test route to validate that the app is working
@app.get('/')
def root():
    return{"message":"It's up and running"}