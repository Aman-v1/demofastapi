"""add foreign key to the post table

Revision ID: 97a0da426918
Revises: a0b4a615b18c
Create Date: 2023-05-08 12:24:22.283520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97a0da426918'
down_revision = 'a0b4a615b18c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
