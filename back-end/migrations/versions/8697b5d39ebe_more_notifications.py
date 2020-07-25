"""more notifications

Revision ID: 8697b5d39ebe
Revises: c4b937f9fbdb
Create Date: 2018-11-20 22:08:10.239719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8697b5d39ebe'
down_revision = 'c4b937f9fbdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_followeds_posts_read_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('last_follows_read_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('last_likes_read_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('last_likes_read_time')
        batch_op.drop_column('last_follows_read_time')
        batch_op.drop_column('last_followeds_posts_read_time')

    # ### end Alembic commands ###
