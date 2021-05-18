"""empty message

Revision ID: 460bb858ff31
Revises: 7d1a803123a4
Create Date: 2021-05-13 23:41:22.794719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '460bb858ff31'
down_revision = '7d1a803123a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=150), nullable=False))
    op.add_column('user', sa.Column('sex', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'sex')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###
