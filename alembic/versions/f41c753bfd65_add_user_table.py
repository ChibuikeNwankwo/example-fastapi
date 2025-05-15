"""add user table

Revision ID: f41c753bfd65
Revises: 2add0e62dfd6
Create Date: 2025-05-15 14:03:40.955942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f41c753bfd65'
down_revision: Union[str, None] = '2add0e62dfd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), primary_key = True, nullable = False),
                    sa.Column('email', sa.String(), nullable = False, unique = True),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('now()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
