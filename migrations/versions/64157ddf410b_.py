"""empty message

Revision ID: 64157ddf410b
Revises: 
Create Date: 2021-10-24 12:42:13.492887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64157ddf410b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklisted',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklist_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('recipes',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('recipe_name', sa.String(length=100), nullable=False),
    sa.Column('ingredients', sa.String(length=256), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('recipe_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    op.drop_table('categories')
    op.drop_table('users')
    op.drop_table('blacklisted')
    # ### end Alembic commands ###
