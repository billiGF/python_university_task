from fastapi import APIRouter, HTTPException, Depends
from src.shcemas.library import CategoryCreate, Pagination, MagazineCreate
from src.crud.library import category_crud
from src.core.db import get_async, AsyncSession
from typing import Annotated
from src.crud.library import check_category_by_name

router = APIRouter(
    # prefix='/f',
    tags=['Magazine']
    )


@router.post('/category/')
async def greetings(
    category: CategoryCreate,
    session: AsyncSession = Depends(get_async)
    ):

    name_category = await check_category_by_name(category.name, session)
    if name_category is not None:
        raise HTTPException(
            status_code=422,
            detail='This category already exeist'
        )

    result = await category_crud.post(category, session)
    return result

# PaginationDEP = Annotated[Pagination, Depends(Pagination)]

@router.get('/{category}/')
async def get_category(
    # pagination: PaginationDEP,
    category_id: int,
    session: AsyncSession = Depends(get_async),
    ):
    geting_category = await category_crud.get(category_id, session,)
    if geting_category is None:
        raise HTTPException(
            status_code=404,
            detail='No such of Category'
        )
    return geting_category


@router.get('/category')
async def get_multi_category(session: AsyncSession = Depends(get_async)):
    info = await category_crud.get_multi(session)
    return info