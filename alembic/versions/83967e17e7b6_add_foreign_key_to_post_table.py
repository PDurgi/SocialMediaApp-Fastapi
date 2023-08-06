"""add foreign key to post table

Revision ID: 83967e17e7b6
Revises: 83fca4345069
Create Date: 2023-08-05 23:03:00.984588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83967e17e7b6'
down_revision: Union[str, None] = '83fca4345069'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','owner_id')
    pass
