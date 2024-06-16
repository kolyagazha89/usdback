import sqlalchemy

from src.users.user import stage_table

metadata = sqlalchemy.MetaData()

front_table = sqlalchemy.Table(
    "front",
    metadata,
    sqlalchemy.Column("front_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("front_din_brand", sqlalchemy.String(50)),
    sqlalchemy.Column("front_amp_brand", sqlalchemy.String(50)),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage_table.c.id)),
)