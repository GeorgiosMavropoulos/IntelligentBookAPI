#this file contains the book model
from datetime import datetime
#import db column and attributes
from sqlalchemy import  String, Integer, Text, DECIMAL, CheckConstraint, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from ..database.base import Base 

#create publisher model
class Publisher(Base):
 __tablename__ = "publishers"
 id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
 publisher:Mapped[str] = mapped_column(String(50),nullable=False, index=True)
 

 #constains
 __table_args__ = (
       
         # length(publisher) >= 1 make sure title will never be an empty string    
         CheckConstraint("length(publisher) >= 1", name="publisher_min_length"),

     
     
         
     )