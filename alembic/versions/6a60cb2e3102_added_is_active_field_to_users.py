"""added is_active field to users

Revision ID: 6a60cb2e3102
Revises: 17be96741cf5
Create Date: 2024-07-20 01:06:54.780108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a60cb2e3102'
down_revision: Union[str, None] = '17be96741cf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###