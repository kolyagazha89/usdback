import sqlalchemy
from src.stage import stage
metadata = sqlalchemy.MetaData()

videoStage_table = sqlalchemy.Table(
    "videoStage",
    metadata,
    sqlalchemy.Column("video_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("video_path", sqlalchemy.String(200), unique=True),
    sqlalchemy.Column("video_stage", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage.stage_table.c.stage_id)),
)
