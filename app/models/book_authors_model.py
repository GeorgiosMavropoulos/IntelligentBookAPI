#this file contains the book model
from datetime import datetime
#import db column and attributes
from sqlalchemy import  String, Integer, Text, DECIMAL, CheckConstraint, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from ..database.base import Base 


#create a conjunctions table to connect authors + books
class AuthorBooks(Base):
 __tablename__ = "author_books"
 book_id: Mapped[int] = mapped_column(Integer,  ForeignKey("books.id", ondelete="CASCADE"),nullable=False,primary_key=True)
 author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id", ondelete="CASCADE"),nullable=False,primary_key=True)