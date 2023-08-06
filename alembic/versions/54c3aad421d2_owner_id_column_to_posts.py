"""owner_id column to posts

Revision ID: 54c3aad421d2
Revises: 46f1b40116d9
Create Date: 2023-08-05 23:41:21.820166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54c3aad421d2'
down_revision: Union[str, None] = '46f1b40116d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','owner_id')
    pass
