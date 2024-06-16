import sqlalchemy
from src.partners import partners
metadata = sqlalchemy.MetaData()


newsPartners_table = sqlalchemy.Table(
    "newsPartner",
    metadata,
    sqlalchemy.Column("np_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("np_name", sqlalchemy.String(40), unique=True),
    sqlalchemy.Column("np_photo", sqlalchemy.String(500)),
    sqlalchemy.Column("np_link", sqlalchemy.String(500)),
    sqlalchemy.Column("np_partId",sqlalchemy.Integer, sqlalchemy.ForeignKey(partners.partners_table.c.partner_id)),
)
