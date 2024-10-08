"""add type partner

Revision ID: ffad4ff7e46e
Revises: e707df9e19e0
Create Date: 2024-06-01 13:20:43.160108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffad4ff7e46e'
down_revision: Union[str, None] = 'e707df9e19e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('typePartner',
    sa.Column('TP_id', sa.Integer(), nullable=False),
    sa.Column('TP_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('TP_id')
    )
    op.add_column('partner', sa.Column('partner_type', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'partner', 'typePartner', ['partner_type'], ['TP_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'partner', type_='foreignkey')
    op.drop_column('partner', 'partner_type')
    op.drop_table('typePartner')
    # ### end Alembic commands ###
