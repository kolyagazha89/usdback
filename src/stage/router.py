from fastapi import APIRouter, Depends
from sqlalchemy import select, update, insert, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.stage.schemas import addStage,addSP,addST

from src.stage.stage import stage_table
from src.stage.stagePartner import SP_table
from src.stage.stageTags import ST_table

router = APIRouter(
    prefix="/stages",
    tags=["Stage"]
)
@router.get('/')
async def get_stage(session: AsyncSession = Depends(get_async_session)):
    query = select(stage_table)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/add')
async def add_stage(query: addStage, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(stage_table).values(**query.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/edit/')
async def edit_stage(stageId:int, query: addStage,session: AsyncSession = Depends(get_async_session)):
    query = update(stage_table).where(stage_table.c.stage_id == stageId).values(**query.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.get('/stage/')
async def item_stage(stageId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(stage_table).where(stage_table.c.stage_id == stageId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post("/delete/")
async def delete_stage(stageId:int, session: AsyncSession = Depends(get_async_session)):
    query = delete(stage_table).where(stage_table.c.stage_id==stageId)
    await session.execute(query)
    await session.commit()
    return 'succes'

# РОУТЕРЫ ЭТАП-ПАРТНЕР

@router.get("/sp/")
async def get_sp(stageId:int, session: AsyncSession = Depends(get_async_session)):
    query = select(SP_table.c.SP_partner).where(SP_table.c.SP_stage==stageId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/sp/add')
async def add_sp(query: addSP, session: AsyncSession = Depends(get_async_session)):
    for i in query.SP_partner:
        stmt = insert(SP_table).values(SP_stage=query.SP_stage,SP_partner=int(i.get('partner_id')))
        await session.execute(stmt)
        await session.commit()
    return 'succes'

@router.post("/sp/delete/")
async def delete_SP(stageId:int, partId:int, session: AsyncSession = Depends(get_async_session)):
    query = delete(SP_table).where(SP_table.c.SP_stage==stageId).where(SP_table.c.SP_partner==partId)
    await session.execute(query)
    await session.commit()
    return 'succes'

# РОУТЕРЫ ЭТАП-ТЭГ

@router.get("/st/")
async def get_st(stageId:int, session: AsyncSession = Depends(get_async_session)):
    query = select(ST_table.c.ST_tags).where(ST_table.c.ST_stage==stageId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/st/add')
async def add_st(query: addST, session: AsyncSession = Depends(get_async_session)):
    for i in query.ST_tags:
        stmt = insert(ST_table).values(ST_stage=query.ST_stage,ST_tags=int(i.get('tag_id')))
        await session.execute(stmt)
        await session.commit()
    return 'succes'

@router.post("/st/delete/")
async def delete_St(stageId:int, tagsId:int, session: AsyncSession = Depends(get_async_session)):
    query = delete(ST_table).where(ST_table.c.ST_stage==stageId).where(ST_table.c.ST_tags==tagsId)
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.get('/lastid/')
async def get_lastid(session: AsyncSession = Depends(get_async_session)):
    query = select(stage_table.c.stage_id).filter(stage_table.c.stage_id ==select(func.max(stage_table.c.stage_id)))
    result = await session.execute(query)
    return result.mappings().one()
