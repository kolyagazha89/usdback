from fastapi import APIRouter, Depends
from sqlalchemy import select, update, insert, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.users.user import stage_table
from src.users.back import back_table
from src.users.battery import battery_table
from src.users.front import front_table
from src.users.schemas import addFront, addSub, addBack, addBattery
from src.users.sub import sub_table

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post('/num/')
async def get_num(num:str,session: AsyncSession = Depends(get_async_session)):
    query = select(stage_table).where(stage_table.c.grz==num)
    result = await session.execute(query)
    return result.mappings().all()




@router.get('/front/')
async def item_front(userId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(front_table).where(front_table.c.user_id == userId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/front/add')
async def add_fronte(query: addFront, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(front_table).values(**query.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/front/edit/')
async def edit_front(userId:int, query: addFront,session: AsyncSession = Depends(get_async_session)):
    query = update(front_table).where(front_table.c.user_id == userId).values(**query.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'


@router.get('/sub/')
async def item_sub(userId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(sub_table).where(sub_table.c.user_id == userId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/sub/add')
async def add_sub(query: addSub, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(sub_table).values(**query.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/sub/edit/')
async def edit_sub(userId:int, query: addSub,session: AsyncSession = Depends(get_async_session)):
    query = update(sub_table).where(sub_table.c.user_id == userId).values(**query.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.get('/back/')
async def item_back(userId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(back_table).where(back_table.c.user_id == userId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/back/add')
async def add_back(query: addBack, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(back_table).values(**query.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/back/edit/')
async def edit_back(userId:int, query: addBack,session: AsyncSession = Depends(get_async_session)):
    query = update(back_table).where(back_table.c.user_id == userId).values(**query.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'

@router.get('/battery/')
async def item_battery(userId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(battery_table).where(battery_table.c.user_id == userId)
    result = await session.execute(query)
    return result.mappings().all()

@router.post('/battery/add')
async def add_battery(query: addBattery, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(battery_table).values(**query.dict())
    await session.execute(stmt)
    await session.commit()
    return 'succes'

@router.post('/battery/edit/')
async def edit_battery(userId:int, query: addBattery,session: AsyncSession = Depends(get_async_session)):
    query = update(battery_table).where(battery_table.c.user_id == userId).values(**query.dict())
    await session.execute(query)
    await session.commit()
    return 'succes'