"""add content column to posts table

Revision ID: da772a7f1673
Revises: 3beddd629230
Create Date: 2023-08-05 20:53:03.216227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da772a7f1673'
down_revision: Union[str, None] = '3beddd629230'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
