from src.core.db import AsyncSession
from src.shcemas.library import CategoryCreate
from sqlalchemy import select

class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def post(
            self,
            category: CategoryCreate, 
            session: AsyncSession):
        new_category = category.dict()
        db_category = self.model(**new_category)
        session.add(db_category)
        await session.commit()
        await session.refresh(db_category)
        return db_category

    async def get(
            self,
            category_id,
            session: AsyncSession):
        get_category = await session.execute(select(self.model).where(
            self.model.id == category_id
        ))
        get_category = get_category.scalars().first()
        return get_category
    
    async def get_multi(
            self,
            session: AsyncSession):
        info = await session.execute(select(self.model))
        info = info.scalars().all()
        return info