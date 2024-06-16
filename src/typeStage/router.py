from fastapi import APIRouter, Depends
from sqlalchemy import select,update, insert,delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from src.typeStage.typeStage import typeStage_table
router = APIRouter(
    prefix="/type",
    tags=["Type"]
)
@router.get('/')
async def get_type(session: AsyncSession = Depends(get_async_session)):
    query = select(typeStage_table)
    result = await session.execute(query)
    return result.mappings().all()

@router.get('/type/')
async def item_type(typeId:int, session: AsyncSession = Depends(get_async_session)):
    query = select(typeStage_table).where(typeStage_table.c.type_id == typeId)
    result = await session.execute(query)
    return result.mappings().all()