"""authors_books_tables

Revision ID: 90d9d58e3ddf
Revises: a94a6f9f0703
Create Date: 2025-02-24 19:38:53.431107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90d9d58e3ddf'
down_revision: Union[str, None] = 'a94a6f9f0703'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_id', sa.Integer(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birth_date', sa.String(), nullable=True),
    sa.Column('death_date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_api_id'), 'authors', ['api_id'], unique=True)
    op.create_index(op.f('ix_authors_birth_date'), 'authors', ['birth_date'], unique=False)
    op.create_index(op.f('ix_authors_death_date'), 'authors', ['death_date'], unique=False)
    op.create_index(op.f('ix_authors_id'), 'authors', ['id'], unique=False)
    op.create_index(op.f('ix_authors_name'), 'authors', ['name'], unique=False)
    op.create_index(op.f('ix_authors_slug'), 'authors', ['slug'], unique=True)
    op.create_table('authors_books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_books_author_id'), 'authors_books', ['author_id'], unique=True)
    op.create_index(op.f('ix_authors_books_book_id'), 'authors_books', ['book_id'], unique=True)
    op.create_index(op.f('ix_authors_books_id'), 'authors_books', ['id'], unique=False)
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    op.create_index(op.f('ix_books_name'), 'books', ['name'], unique=False)
    op.create_index(op.f('ix_books_slug'), 'books', ['slug'], unique=True)
    op.add_column('quotes', sa.Column('text', sa.String(), nullable=True))
    op.add_column('quotes', sa.Column('author', sa.String(), nullable=True))
    op.create_index(op.f('ix_quotes_author'), 'quotes', ['author'], unique=False)
    op.create_index(op.f('ix_quotes_text'), 'quotes', ['text'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quotes_text'), table_name='quotes')
    op.drop_index(op.f('ix_quotes_author'), table_name='quotes')
    op.drop_column('quotes', 'author')
    op.drop_column('quotes', 'text')
    op.drop_index(op.f('ix_books_slug'), table_name='books')
    op.drop_index(op.f('ix_books_name'), table_name='books')
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_authors_books_id'), table_name='authors_books')
    op.drop_index(op.f('ix_authors_books_book_id'), table_name='authors_books')
    op.drop_index(op.f('ix_authors_books_author_id'), table_name='authors_books')
    op.drop_table('authors_books')
    op.drop_index(op.f('ix_authors_slug'), table_name='authors')
    op.drop_index(op.f('ix_authors_name'), table_name='authors')
    op.drop_index(op.f('ix_authors_id'), table_name='authors')
    op.drop_index(op.f('ix_authors_death_date'), table_name='authors')
    op.drop_index(op.f('ix_authors_birth_date'), table_name='authors')
    op.drop_index(op.f('ix_authors_api_id'), table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###
