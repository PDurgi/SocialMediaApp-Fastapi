"""create foreign key

Revision ID: 46f1b40116d9
Revises: 83967e17e7b6
Create Date: 2023-08-05 23:17:38.578041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46f1b40116d9'
down_revision: Union[str, None] = '83967e17e7b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.add_column('posts', sa.Column('mycolumn', sa.String(), nullable=False))
    # op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


# def downgrade() -> None:
#     op.drop_constraint('posts_users_fk', table_name="posts")
#     op.drop_column('posts','owner_id')
#     pass