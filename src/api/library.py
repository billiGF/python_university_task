from fastapi import APIRouter, HTTPException, Depends
from shcemas.library import CategoryCreate, Pagination, MagazineCreate
from crud.library import creating_category, cheking_category, read_all_category_from_db, adding_magazine, cheking_magazine_theme
from core.db import get_async, AsyncSession
from typing import Annotated

router = APIRouter(
    # prefix='/f',
    # tags=['Magazine']
    )


@router.post('/category/', tags=['Magazine'])
async def greetings(
    category: CategoryCreate,
    session: AsyncSession = Depends(get_async)
    ):

    name_category = await cheking_category(category.name, session)
    if name_category is not None:
        raise HTTPException(
            status_code=422,
            detail='This category already exeist'
        )

    result = await creating_category(category, session)
    return result

PaginationDEP = Annotated[Pagination, Depends(Pagination)]

@router.get('/category/', tags=['Magazine'])
async def get_category(
    pagination: PaginationDEP,
    session: AsyncSession = Depends(get_async),
    ):
    
    geting_category = await read_all_category_from_db(session, pagination)
    return geting_category


@router.post('/magazine/')
async def create_magazine(magazine: MagazineCreate, session: AsyncSession = Depends(get_async)):
    first_check = await cheking_magazine_theme(session, magazine.theme)
    if first_check is None:
        raise HTTPException(
            status_code=422,
            detail='There is no such a Category'
        )
    cheking = await adding_magazine(session, magazine)
    return cheking