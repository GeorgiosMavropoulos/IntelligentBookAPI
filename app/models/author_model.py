#this file contains the book model
from datetime import datetime
#import db column and attributes
from sqlalchemy import  String, Integer, Text, DECIMAL, CheckConstraint, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from ..database.base import Base 

#create author model
class Author(Base):
 __tablename__= "authors"
 id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
 author: Mapped[str] = mapped_column(String(50),nullable=False, index=True)
#constains
 __table_args__ = (
       
         # length(author) >= 1 make sure title will never be an empty string    
         CheckConstraint("length(author) >= 1", name="author_min_length"),

     
         
     )
