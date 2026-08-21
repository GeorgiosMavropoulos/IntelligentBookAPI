#this file contains the book model
from datetime import datetime
#import db column and attributes
from sqlalchemy import  String, Integer, Text, DECIMAL, CheckConstraint, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from ..database.base import Base 

#create book model
class Book(Base):
 __tablename__ = "books"
 id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
 title: Mapped[str] = mapped_column(String(255), nullable=False, index=True) 
 
 year: Mapped[int] = mapped_column(Integer,nullable=False)
 isbn: Mapped[str] = mapped_column(String(255),nullable=False,index=True,unique=True)
 price: Mapped[DECIMAL] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
 description:Mapped[str] = mapped_column(Text,nullable=False)
 genre: Mapped[str] = mapped_column(String(60),nullable=False)
 language: Mapped[str] = mapped_column(String(60),nullable=False)
 created_at: Mapped[datetime] = mapped_column(DateTime,server_default=func.now(), nullable=False)
 updated_at: Mapped[datetime] = mapped_column(DateTime,server_default=func.now(), onupdate=func.now(),nullable=False)
 stock: Mapped[int] = mapped_column(Integer, nullable=False)
 publisher_id: Mapped[int] = mapped_column(Integer, ForeignKey("publishers.id"),nullable=False)
 #constrains
 __table_args__ = (
        # length(title) >= 1 make sure title will never be an empty string
        CheckConstraint("length(title) >= 1", name="title_min_length"),

        #validate that year will never be below 0
        CheckConstraint("year >= 1000 AND year <= 2100", name="year_valid_range"),

        # CONSTRAINT for isbn: ISBN should be 10 or 13 chars
        CheckConstraint("length(isbn) = 10 OR length(isbn) = 13", name="book_isbn_length_valid"),
         #price should be a positive range(> 1)
        CheckConstraint("price >= 1",name="price_positive_range"),
           
        #stock can't be a negative number
        CheckConstraint("stock >=0", name="stock_negative_number"),

        #genre cannot accept empty string
        CheckConstraint("length(genre) >= 1",name="genre_min_length"),

        #min lang chars
        CheckConstraint("length(language)>= 1",name="language_min_length"),

          #min description chars
         CheckConstraint("length(description)>= 1",name="description_min_length"),
        
    )



