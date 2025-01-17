"""empty message

Revision ID: 24b84cb1ee03
Revises: c100f0c2fec3
Create Date: 2024-06-23 23:22:06.650319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b84cb1ee03'
down_revision = 'c100f0c2fec3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_done', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('canceled', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.drop_column('canceled')
        batch_op.drop_column('is_done')

    # ### end Alembic commands ###
