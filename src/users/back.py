import sqlalchemy

from src.users.user import stage_table

metadata = sqlalchemy.MetaData()

back_table = sqlalchemy.Table(
    "back",
    metadata,
    sqlalchemy.Column("back_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("back_din_brand", sqlalchemy.String(50)),
    sqlalchemy.Column("back_amp_brand", sqlalchemy.String(50)),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage_table.c.id)),
)