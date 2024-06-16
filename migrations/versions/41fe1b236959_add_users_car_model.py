"""add users car model

Revision ID: 41fe1b236959
Revises: dba5d7b0e60d
Create Date: 2024-06-03 12:08:47.675678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41fe1b236959'
down_revision: Union[str, None] = 'dba5d7b0e60d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('car_model', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'car_model')
    # ### end Alembic commands ###
