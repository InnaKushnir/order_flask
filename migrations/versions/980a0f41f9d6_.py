"""empty message

Revision ID: 980a0f41f9d6
Revises: 
Create Date: 2023-07-25 23:41:00.395289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980a0f41f9d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('street', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_address_id'), ['id'], unique=False)

    op.create_table('object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=255), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('object', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_object_id'), ['id'], unique=False)

    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_order_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_order_id'))

    op.drop_table('order')
    with op.batch_alter_table('object', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_object_id'))

    op.drop_table('object')
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_address_id'))

    op.drop_table('address')
    # ### end Alembic commands ###