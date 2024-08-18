from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.news.news import news_table
from src.news.schemas import addNews
from src.users.user import stage_table
router = APIRouter(
    prefix="/news",
    tags=["News"]
)
@router.get('/')
async def get_specific_class(session: AsyncSession = Depends(get_async_session)):
    query = select(news_table,stage_table).join(stage_table, news_table.c.user_id==stage_table.c.id)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/add')
async def add_class(add_news: addNews,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(news_table).values(**add_news.dict(), date_news=datetime.now().date())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/edit/')
async def edit_class(newsId:int,edit_name : addNews,session: AsyncSession = Depends(get_async_session)):
    query = update(news_table).where(news_table.c.id_news == newsId).values(**edit_name.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.get('/news/')
async def item_class(newsId:int,session: AsyncSession = Depends(get_async_session)):
    query = select(news_table,stage_table).where(news_table.c.id_news == newsId).join(stage_table, news_table.c.user_id==stage_table.c.id)
    result = await session.execute(query)
    return result.mappings().all()
@router.post("/delete/")
async def delete_stage(newsId:int, session: AsyncSession = Depends(get_async_session)):
    query = delete(news_table).where(news_table.c.id_news == newsId)
    await session.execute(query)
    await session.commit()
    return 'succes'