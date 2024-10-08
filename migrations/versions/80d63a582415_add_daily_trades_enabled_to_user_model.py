"""Add daily_trades_enabled to User model

Revision ID: 80d63a582415
Revises: fd1c21a8e907
Create Date: 2024-08-21 08:42:19.659195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80d63a582415'
down_revision = 'fd1c21a8e907'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('daily_trades_enabled', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('daily_trades_enabled')

    # ### end Alembic commands ###
