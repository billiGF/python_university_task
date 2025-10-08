from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.base import CRUDBase
from src.models.library import Category



async def check_category_by_name(categorycreat: str, session: AsyncSession):
    info = await session.execute(
        select(Category.id).where(
            Category.name == categorycreat
        )
    )
    info = info.scalars().first()
    return info

category_crud = CRUDBase(Category)