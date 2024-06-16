import sqlalchemy
metadata = sqlalchemy.MetaData()


tagsStage_table = sqlalchemy.Table(
    "tagsStage",
    metadata,
    sqlalchemy.Column("tag_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("tag_name", sqlalchemy.String(40), unique=True),

)
