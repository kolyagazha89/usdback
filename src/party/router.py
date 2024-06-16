import json

from fastapi import APIRouter, Depends
from sqlalchemy import select, update, insert, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.classes.classes import class_table
from src.party.ParticipantClass import participantClass_table
from src.party.partcipant import participant_table
from src.party.schemas import addParticipant, addPC

router = APIRouter(
    prefix="/party",
    tags=["Party"]
)

@router.get('/')
async def get_participant(userId:int, stageId:int,session: AsyncSession = Depends(get_async_session)):
    query = select(participant_table).where(participant_table.c.user_id==userId).where(participant_table.c.stage_id==stageId)
    result = await session.execute(query)
    result=result.mappings().all()
    if not len(result)==0:
        return True
    else:
        return False

@router.post('/add')
async def add_stage(stageId:int,query:addParticipant, session: AsyncSession = Depends(get_async_session)):
    number = select(func.max(participant_table.c.number_party)).where(participant_table.c.stage_id==stageId)
    result = await session.execute(number)
    result=result.mappings().all()
    if(result[0].max_1!=None):
        number=int(result[0].max_1)+1
        if(len(str(number))==1):
            number = f"00{number}"
        else:
            if (len(str(number))==2):
                number = f"0{number}"
            else:
                number = str(number)
    else:
        number="001"
    stmt = insert(participant_table).values(number_party=number,user_id=query.user_id,stage_id=stageId)
    await session.execute(stmt)
    await session.commit()
    return number

# УЧАСТНИК КЛАСС

@router.get('/pc')
async def get_PC(userId:int,session: AsyncSession = Depends(get_async_session)):
    numberPart=select(participant_table).where(participant_table.c.user_id==userId)
    res = await session.execute(numberPart)
    res=res.mappings().all()
    if (not len(res) == 0):
        numberPart=res[0].participant_id
        query = select(participantClass_table).where(participantClass_table.c.PC_participant == numberPart)
        result = await session.execute(query)
        return result.mappings().all()
    return None

@router.post('/pc/add/')
async def add_stage(userId:str,stageId:int,query:addPC, session: AsyncSession = Depends(get_async_session)):
    numberPart = select(participant_table).where(participant_table.c.number_party ==userId).where(participant_table.c.stage_id==stageId)
    res = await session.execute(numberPart)
    res = res.mappings().all()
    partId = res[0].participant_id
    classid=select(class_table).where(class_table.c.name_class==query.PC_class)
    res = await session.execute(classid)
    res = res.mappings().all()
    classid = res[0].id_class
    stmt = insert(participantClass_table).values(PC_participant=partId,PC_class=classid)
    await session.execute(stmt)
    await session.commit()
    return 'succes'