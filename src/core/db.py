from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import Column, Integer
from src.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=PreBase)
engine = create_async_engine(settings.database)
AsyncSessionlocal = sessionmaker(engine, class_=AsyncSession)

async def get_async():
    async with AsyncSessionlocal() as get_session:
        yield get_session
