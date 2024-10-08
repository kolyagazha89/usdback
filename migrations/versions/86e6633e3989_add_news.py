"""add news

Revision ID: 86e6633e3989
Revises: 81dda1ac54cd
Create Date: 2024-07-01 14:04:45.556273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86e6633e3989'
down_revision: Union[str, None] = '81dda1ac54cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id_news', sa.Integer(), nullable=False),
    sa.Column('name_news', sa.String(length=100), nullable=True),
    sa.Column('text_news', sa.String(length=5000), nullable=True),
    sa.Column('date_news', sa.Date(), nullable=True),
    sa.Column('photo_news', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id_news')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###
