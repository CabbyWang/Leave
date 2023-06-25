"""empty message

Revision ID: 7f67805a9766
Revises: 9f52d6a1eff1
Create Date: 2023-06-18 14:47:01.443094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f67805a9766'
down_revision = '9f52d6a1eff1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apply', schema=None) as batch_op:
        batch_op.add_column(sa.Column('actual_back_date', sa.DateTime(), nullable=True, comment='实际返回时间'))
        batch_op.add_column(sa.Column('outdays', sa.Integer(), nullable=True, comment='外出天数'))
        batch_op.alter_column('leave_date',
               existing_type=sa.DATE(),
               comment='离开日期',
               existing_comment='离开时间',
               existing_nullable=False)
        batch_op.alter_column('back_date',
               existing_type=sa.DATE(),
               comment='返回日期',
               existing_comment='返回时间',
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apply', schema=None) as batch_op:
        batch_op.alter_column('back_date',
               existing_type=sa.DATE(),
               comment='返回时间',
               existing_comment='返回日期',
               existing_nullable=False)
        batch_op.alter_column('leave_date',
               existing_type=sa.DATE(),
               comment='离开时间',
               existing_comment='离开日期',
               existing_nullable=False)
        batch_op.drop_column('outdays')
        batch_op.drop_column('actual_back_date')

    # ### end Alembic commands ###