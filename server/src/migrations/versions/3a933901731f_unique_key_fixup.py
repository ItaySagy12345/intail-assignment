"""unique_key_fixup

Revision ID: 3a933901731f
Revises: 39a59824670a
Create Date: 2025-02-26 20:26:35.053876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a933901731f'
down_revision: Union[str, None] = '39a59824670a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_authors_api_id', table_name='authors')
    op.create_index(op.f('ix_authors_api_id'), 'authors', ['api_id'], unique=False)
    op.create_foreign_key(None, 'authors_books', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'authors_books', 'authors', ['author_id'], ['id'])
    op.drop_index('ix_books_api_id', table_name='books')
    op.create_index(op.f('ix_books_api_id'), 'books', ['api_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_api_id'), table_name='books')
    op.create_index('ix_books_api_id', 'books', ['api_id'], unique=True)
    op.drop_constraint(None, 'authors_books', type_='foreignkey')
    op.drop_constraint(None, 'authors_books', type_='foreignkey')
    op.drop_index(op.f('ix_authors_api_id'), table_name='authors')
    op.create_index('ix_authors_api_id', 'authors', ['api_id'], unique=True)
    # ### end Alembic commands ###
