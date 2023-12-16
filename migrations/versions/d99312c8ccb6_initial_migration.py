"""Initial migration

Revision ID: d99312c8ccb6
Revises: 
Create Date: 2023-11-30 20:53:52.737767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99312c8ccb6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id_curso', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('data_publicacao', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id_curso')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curso')
    # ### end Alembic commands ###
