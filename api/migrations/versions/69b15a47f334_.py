"""empty message

Revision ID: 69b15a47f334
Revises: 42681ac46798
Create Date: 2018-06-05 16:18:01.117591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69b15a47f334'
down_revision = '42681ac46798'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('state_cd', sa.String(length=40), nullable=True))
    op.drop_constraint('requests_stateCd_fkey', 'requests', type_='foreignkey')
    op.create_foreign_key(None, 'requests', 'states', ['state_cd'], ['cd'])
    op.drop_column('requests', 'stateCd')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('stateCd', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'requests', type_='foreignkey')
    op.create_foreign_key('requests_stateCd_fkey', 'requests', 'states', ['stateCd'], ['cd'])
    op.drop_column('requests', 'state_cd')
    # ### end Alembic commands ###
