import sqlalchemy

from src.users.user import stage_table

metadata = sqlalchemy.MetaData()

battery_table = sqlalchemy.Table(
    "battery",
    metadata,
    sqlalchemy.Column("battery_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("battery_type", sqlalchemy.String(50)),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage_table.c.id)),
)