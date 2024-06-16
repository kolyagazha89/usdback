import sqlalchemy
from sqlalchemy import Integer, Column, String, Boolean,ForeignKey

from src.classes.classes import class_table
from src.party.partcipant import participant_table
from src.stage.stage import stage_table

metadata = sqlalchemy.MetaData()


participantClass_table = sqlalchemy.Table(
    "participantClass",
    metadata,
    Column("PC_id",Integer, primary_key=True),
    Column("PC_participant", Integer, ForeignKey(participant_table.c.participant_id)),
    Column("PC_class", Integer,ForeignKey(class_table.c.id_class)),
)
