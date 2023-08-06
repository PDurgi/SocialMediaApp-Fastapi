"""add user table

Revision ID: ec049d7f6bfa
Revises: da772a7f1673
Create Date: 2023-08-05 22:34:22.644707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec049d7f6bfa'
down_revision: Union[str, None] = 'da772a7f1673'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    pass


def downgrade() -> None:
    pass
