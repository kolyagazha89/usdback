from fastapi import APIRouter, Depends
from sqlalchemy import select,insert,update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.classes.classes import class_table
from src.classes.schemas import addClass
router = APIRouter(
    prefix="/class",
    tags=["Classes"]
)
@router.get('/')
async def get_specific_class(session: AsyncSession = Depends(get_async_session)):
    query = select(class_table)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/add')
async def add_class(add_class: addClass,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(class_table).values(**add_class.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/edit/{class_id}')
async def edit_class(classId:int,edit_name : addClass,session: AsyncSession = Depends(get_async_session)):
    query = update(class_table).where(class_table.c.id_class == classId).values(**edit_name.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.post('/class/{class_id}')
async def item_class(classId:int,session: AsyncSession = Depends(get_async_session)):
    query = select(class_table).where(class_table.c.id_class == classId)
    result = await session.execute(query)
    return result.mappings().all()