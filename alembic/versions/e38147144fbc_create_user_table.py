"""create user table

Revision ID: e38147144fbc
Revises: 01ae015d4bc0
Create Date: 2024-10-27 17:56:25.370112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e38147144fbc'
down_revision: Union[str, None] = '01ae015d4bc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('age', sa.Integer, nullable=True),
    )
    pass


def downgrade() -> None:
    op.drop_table('user')

    pass
