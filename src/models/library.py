from src.core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,Integer, ForeignKey

class Category(Base):
    name = Column(String(20))

# class Category(Base):
#     name = Column(String)
#     category_id = Column(Integer, ForeignKey('navigator.id'))

