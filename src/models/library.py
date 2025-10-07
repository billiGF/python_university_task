from core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,Integer, ForeignKey

class Category(Base):
    name = Column(String, unique=True, nullable=False)
    magazine = relationship('Magazine', backref='categorys')


class Magazine(Base):
    name = Column(String, unique=True)
    theme = Column(Integer, ForeignKey('category.id'))