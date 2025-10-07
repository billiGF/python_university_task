from models.library import Category, Magazine
from core.db import AsyncSessionlocal
from shcemas.library import CategoryCreate, MagazineCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def creating_category(
        category: CategoryCreate, 
        session: AsyncSession)-> Category:
    new_category = category.dict()
    db_category = Category(**new_category)
    session.add(db_category)
    await session.commit()
    await session.refresh(db_category)
    return db_category


async def cheking_category(categorycreat: str, session: AsyncSession):
    info = await session.execute(
        select(Category.id).where(
            Category.name == categorycreat
        )
    )
    info = info.scalars().first()
    return info



async def read_all_category_from_db(session: AsyncSession, pagination)-> list[Category]:
    result = await session.execute(
        select(Category).limit(pagination.limit).offset(pagination.offset)
    )
    return result.scalars().all()



async def adding_magazine(session: AsyncSession, magazine: MagazineCreate):
    unpacking = magazine.dict()
    feeld = Magazine(**unpacking)
    session.add(feeld)
    await session.commit()
    await session.refresh(feeld)
    return feeld

async def cheking_magazine_theme(session: AsyncSession, theme: int):
    result = await session.execute(
        select(Magazine.id).where(
            Magazine.id == theme
        )
    )
    rusult = result.scalar()
    return result
