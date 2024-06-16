import sqlalchemy
from sqlalchemy import Integer, Column, String, Boolean,ForeignKey


metadata = sqlalchemy.MetaData()


stage_table = sqlalchemy.Table(
    "user",
    metadata,
    Column("id",Integer, primary_key=True),
    Column("username", String(300)),
    Column("grz", String(10)),
    Column("team", String(100)),
    Column("photo", String(300)),
    Column("number_phone",String(20)),
    Column("car_model",String(30)),
    Column("email",String(100), unique=True, index=True, nullable=False),
    Column("hashed_password", String(1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
