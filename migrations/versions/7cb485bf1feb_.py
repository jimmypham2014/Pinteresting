"""empty message

Revision ID: 7cb485bf1feb
Revises: 
Create Date: 2023-04-30 20:13:45.261879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cb485bf1feb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=20), nullable=False),
    sa.Column('lastName', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('about', sa.String(length=500), nullable=True),
    sa.Column('image', sa.String(length=1500), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('imageUrl', sa.String(length=1500), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.create_table('pins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('save', sa.Boolean(), nullable=True),
    sa.Column('url', sa.String(length=1500), nullable=True),
    sa.Column('imageUrl', sa.String(length=1500), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pinnings',
    sa.Column('pinId', sa.Integer(), nullable=False),
    sa.Column('boardId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['boardId'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['pinId'], ['pins.id'], ),
    sa.PrimaryKeyConstraint('pinId', 'boardId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pinnings')
    op.drop_table('pins')
    op.drop_table('followers')
    op.drop_table('boards')
    op.drop_table('users')
    # ### end Alembic commands ###