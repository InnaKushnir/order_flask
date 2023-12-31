"""empty message

Revision ID: df3968ef5648
Revises: 2f419e1b9a37
Create Date: 2023-07-29 09:36:25.964601

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'df3968ef5648'
down_revision = '2f419e1b9a37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=100), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
