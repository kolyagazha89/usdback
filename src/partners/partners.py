import sqlalchemy

from src.partners import typePartner

metadata = sqlalchemy.MetaData()


partners_table = sqlalchemy.Table(
    "partner",
    metadata,
    sqlalchemy.Column("partner_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("partner_name", sqlalchemy.String(40), unique=True),
    sqlalchemy.Column("partner_desc", sqlalchemy.String(500)),
    sqlalchemy.Column("partner_logo", sqlalchemy.String(200)),
    sqlalchemy.Column("partner_type", sqlalchemy.Integer, sqlalchemy.ForeignKey(typePartner.TP_table.c.TP_id)),
)
