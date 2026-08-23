##this file contains the base exception class in order to allow the other exception classes to inhert it
from fastapi import Request
from fastapi.responses import JSONResponse

#create the base exception class
class ExceptionServiceHandler(Exception):
     def __init__(self, status_code: int, message: str, code: str): #initialize a contructor

           self.status_code = status_code
           self.message = message
           self.code = code #string id for frontend if needs be

   
  #exception handler to handle the exceptions
async def exception_service_handler(request:Request,exception:ExceptionServiceHandler):
           #return the response
           return JSONResponse(
                 status_code=exception.status_code,
                 content={
                       "status":"error",
                       "code":exception.code,
                       "message":exception.message
                 }
                 ) 