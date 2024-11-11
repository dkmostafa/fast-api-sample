"""first migrations

Revision ID: 01ae015d4bc0
Revises: 
Create Date: 2024-10-22 18:44:36.903007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '01ae015d4bc0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    ...


def downgrade() -> None:
    ...
