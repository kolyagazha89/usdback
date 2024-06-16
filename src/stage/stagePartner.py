import sqlalchemy
from sqlalchemy.orm import relationship

from src.partners import partners
from src.stage import stage

metadata = sqlalchemy.MetaData()


SP_table = sqlalchemy.Table(
    "stagePartner",
    metadata,
    sqlalchemy.Column("SP_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("SP_stage", sqlalchemy.Integer, sqlalchemy.ForeignKey(stage.stage_table.c.stage_id)),
    sqlalchemy.Column("SP_partner", sqlalchemy.Integer, sqlalchemy.ForeignKey(partners.partners_table.c.partner_id)),
)
