"""add content column to posts table

Revision ID: ccbbe854a6b5
Revises: da19a86ff0a8
Create Date: 2023-05-08 11:54:10.307192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccbbe854a6b5'
down_revision = 'da19a86ff0a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
