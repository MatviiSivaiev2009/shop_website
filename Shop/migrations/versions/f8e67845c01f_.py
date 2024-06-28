"""empty message

Revision ID: f8e67845c01f
Revises: 1647f0d8ab11
Create Date: 2024-06-28 01:50:51.194019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8e67845c01f'
down_revision = '1647f0d8ab11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('order_pending',
               existing_type=sa.INTEGER(),
               type_=sa.Boolean(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('order_pending',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
