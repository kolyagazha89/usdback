import sqlalchemy
metadata = sqlalchemy.MetaData()


typeStage_table = sqlalchemy.Table(
    "typeStage",
    metadata,
    sqlalchemy.Column("type_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("type_name", sqlalchemy.String(40), unique=True),
)
