from fastapi import APIRouter, Depends
from sqlalchemy import select,update, insert,delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.tagsStage.schemas import addTag

from src.tagsStage.tagsStage import tagsStage_table
router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)
@router.get('/')
async def get_tags(session: AsyncSession = Depends(get_async_session)):
    query = select(tagsStage_table)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/add')
async def add_tags(query:addTag,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(tagsStage_table).values(**query.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.get('/tag/')
async def item_partner(tagId:int, session: AsyncSession = Depends(get_async_session)):
    query = select(tagsStage_table).where(tagsStage_table.c.tag_id == tagId)
    result = await session.execute(query)
    return result.mappings().all()

