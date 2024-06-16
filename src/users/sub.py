import sqlalchemy

from src.users.user import stage_table

metadata = sqlalchemy.MetaData()

sub_table = sqlalchemy.Table(
    "sub",
    metadata,
    sqlalchemy.Column("sub_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("sub_din_brand", sqlalchemy.String(50)),
    sqlalchemy.Column("sub_amp_brand", sqlalchemy.String(50)),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage_table.c.id)),
)