from fastapi import APIRouter, Depends
from sqlalchemy import select,update, insert,delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.partners.schemas import addPartner
from src.partners.partners import partners_table
from src.partners.typePartner import TP_table

router = APIRouter(
    prefix="/partners",
    tags=["Partners"]
)
@router.get('/')
async def get_partner(session: AsyncSession = Depends(get_async_session)):
    query = select(partners_table)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/add')
async def add_partner(add_partner: addPartner,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(partners_table).values(**add_partner.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/edit/')
async def edit_partner(partId:int, edit_partner: addPartner,session: AsyncSession = Depends(get_async_session)):
    query = update(partners_table).where(partners_table.c.partner_id == partId).values(**edit_partner.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.get('/partner/')
async def item_partner(partId:int, session: AsyncSession = Depends(get_async_session)):
    query = select(partners_table).where(partners_table.c.partner_id == partId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post("/delete/")
async def deletepart(partId:int, session: AsyncSession = Depends(get_async_session)):
    query = delete(partners_table).where(partners_table.c.partner_id==partId)
    await session.execute(query)
    await session.commit()
    return 'succes'

#ТИП ПАРТНЕРА
@router.get('/tp/')
async def get_tp(session: AsyncSession = Depends(get_async_session)):
    query = select(TP_table)
    result = await session.execute(query)
    return result.mappings().all()

@router.get('/tpelem/')
async def item_TP(tpId:int, session: AsyncSession = Depends(get_async_session)):
    query = select(TP_table).where(TP_table.c.TP_id == tpId)
    result = await session.execute(query)
    return result.mappings().all()