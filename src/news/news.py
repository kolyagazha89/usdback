import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.orm import relationship, Mapped

from src.users.user import stage_table

metadata = sqlalchemy.MetaData()

news_table = sqlalchemy.Table(
    "news",
    metadata,
    sqlalchemy.Column("id_news", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name_news", sqlalchemy.String(100)),
    sqlalchemy.Column("text_news", sqlalchemy.String(5000)),
    sqlalchemy.Column("date_news", sqlalchemy.Date),
    sqlalchemy.Column("photo_news", sqlalchemy.String(200)),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage_table.c.id)),
)

