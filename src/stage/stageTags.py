import sqlalchemy
from sqlalchemy.orm import relationship

from src.stage import stage
from src.tagsStage import tagsStage

metadata = sqlalchemy.MetaData()


ST_table = sqlalchemy.Table(
    "stageTags",
    metadata,
    sqlalchemy.Column("ST_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("ST_stage", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage.stage_table.c.stage_id)),
    sqlalchemy.Column("ST_tags", sqlalchemy.Integer, sqlalchemy.ForeignKey(tagsStage.tagsStage_table.c.tag_id)),
)