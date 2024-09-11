"""empty message

Revision ID: f1d93e02e21e
Revises: b5db93e372d8
Create Date: 2024-09-11 22:37:59.089479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1d93e02e21e'
down_revision = 'b5db93e372d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('district',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('district',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=12),
               existing_nullable=True)

    # ### end Alembic commands ###
