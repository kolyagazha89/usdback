import sqlalchemy
from sqlalchemy.orm import relationship

from src.typeStage import typeStage
metadata = sqlalchemy.MetaData()


stage_table = sqlalchemy.Table(
    "stage",
    metadata,
    sqlalchemy.Column("stage_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("stage_name", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("stage_desc", sqlalchemy.String(1000)),
    sqlalchemy.Column("stage_photo", sqlalchemy.String(200)),
    sqlalchemy.Column("stage_city", sqlalchemy.String(200)),
    sqlalchemy.Column("stage_place", sqlalchemy.String(200)),
    sqlalchemy.Column("stage_date", sqlalchemy.Date),
    sqlalchemy.Column("stage_type", sqlalchemy.Integer, sqlalchemy.ForeignKey(typeStage.typeStage_table.c.type_id)),
)
