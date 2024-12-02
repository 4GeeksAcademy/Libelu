"""empty message

Revision ID: 43cf964ca299
Revises: 97e73f09ffac
Create Date: 2024-12-02 20:13:20.200608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43cf964ca299'
down_revision = '97e73f09ffac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('libros', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=480), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('libros', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
