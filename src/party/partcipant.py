import sqlalchemy
from sqlalchemy import Integer, Column, String, Boolean,ForeignKey

from src.users.user import stage_table as user
from src.stage.stage import stage_table as stage

metadata = sqlalchemy.MetaData()


participant_table = sqlalchemy.Table(
    "participant",
    metadata,
    Column("participant_id",Integer, primary_key=True),
    Column("number_party", String(3)),
    Column("user_id", Integer,ForeignKey(user.c.id)),
    Column('stage_id',Integer,ForeignKey(stage.c.stage_id))
)
