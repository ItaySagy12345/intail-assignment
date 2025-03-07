"""quote_name_removal

Revision ID: 23a38c13e49d
Revises: 3a933901731f
Create Date: 2025-02-26 21:22:30.031298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23a38c13e49d'
down_revision: Union[str, None] = '3a933901731f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_quotes_name', table_name='quotes')
    op.drop_column('quotes', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quotes', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_quotes_name', 'quotes', ['name'], unique=False)
    # ### end Alembic commands ###
