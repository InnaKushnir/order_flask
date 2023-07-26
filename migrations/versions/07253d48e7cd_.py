"""empty message

Revision ID: 07253d48e7cd
Revises: 
Create Date: 2023-07-26 23:23:41.117211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07253d48e7cd'
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

    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('color', sa.String(length=255), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_id'), ['id'], unique=False)

    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_order_id'), ['id'], unique=False)

    op.create_table('sub_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sub_address_details', sa.String(length=255), nullable=False),
    sa.Column('main_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['main_address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('sub_address', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_sub_address_id'), ['id'], unique=False)

    op.create_table('orderitem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('orderitem', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_orderitem_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orderitem', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_orderitem_id'))

    op.drop_table('orderitem')
    with op.batch_alter_table('sub_address', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_sub_address_id'))

    op.drop_table('sub_address')
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_order_id'))

    op.drop_table('order')
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_id'))

    op.drop_table('product')
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_address_id'))

    op.drop_table('address')
    # ### end Alembic commands ###