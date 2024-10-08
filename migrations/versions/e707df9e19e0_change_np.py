"""change np

Revision ID: e707df9e19e0
Revises: 14f76da7ef83
Create Date: 2024-06-01 13:12:06.637794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e707df9e19e0'
down_revision: Union[str, None] = '14f76da7ef83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('newsPartner', sa.Column('np_link', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('newsPartner', 'np_link')
    # ### end Alembic commands ###
