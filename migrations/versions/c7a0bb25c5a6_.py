"""empty message

Revision ID: c7a0bb25c5a6
Revises: 
Create Date: 2022-04-06 20:23:06.947637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a0bb25c5a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('first_shot_date', sa.DateTime(), nullable=True),
    sa.Column('second_shot_date', sa.DateTime(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=True),
    sa.Column('health_unit_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cpf')
    )
    op.drop_table('heros')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heros',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('race', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='heros_pkey')
    )
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###
