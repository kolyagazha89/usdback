import sqlalchemy
from sqlalchemy.orm import relationship

from src.stage import stage
from src.tagsStage import tagsStage

metadata = sqlalchemy.MetaData()


TP_table = sqlalchemy.Table(
    "typePartner",
    metadata,
    sqlalchemy.Column("TP_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("TP_name", sqlalchemy.String(200)),

)