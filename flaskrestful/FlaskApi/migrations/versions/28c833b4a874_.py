"""empty message

Revision ID: 28c833b4a874
Revises: 4e6cd047cfc3
Create Date: 2018-08-15 15:22:51.515911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28c833b4a874'
down_revision = '4e6cd047cfc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('u_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_name', sa.String(length=16), nullable=True),
    sa.Column('_u_password', sa.String(length=256), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('u_permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('u_id'),
    sa.UniqueConstraint('u_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
