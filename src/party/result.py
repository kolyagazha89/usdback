import sqlalchemy
from sqlalchemy import Integer, Column, String, Boolean,ForeignKey

from src.party.ParticipantClass import participantClass_table

metadata = sqlalchemy.MetaData()


result_table = sqlalchemy.Table(
    "result",
    metadata,
    Column("result_id",Integer, primary_key=True),
    Column("result_value", String(3)),
    Column("result_PC", Integer,ForeignKey(participantClass_table.c.PC_id)),
)
