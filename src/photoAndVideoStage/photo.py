import sqlalchemy

from src.stage import stage

metadata = sqlalchemy.MetaData()
photoStage_table = sqlalchemy.Table(
    "photoStage",
    metadata,
    sqlalchemy.Column("photo_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("photo_path", sqlalchemy.String(200), unique=True),
    sqlalchemy.Column("photo_stage", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage.stage_table.c.stage_id)),
)
