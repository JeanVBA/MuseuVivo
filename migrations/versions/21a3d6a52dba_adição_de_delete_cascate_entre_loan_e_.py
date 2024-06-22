"""Adição de delete cascate entre loan e work_of_art, loan e institution

Revision ID: 21a3d6a52dba
Revises: 1d892347ab68
Create Date: 2024-06-22 08:37:14.052871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21a3d6a52dba'
down_revision = '1d892347ab68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.drop_constraint('FK__loans__work_of_a__4F7CD00D', type_='foreignkey')
        batch_op.drop_constraint('FK__loans__instituti__4E88ABD4', type_='foreignkey')
        batch_op.create_foreign_key(None, 'works_of_art', ['work_of_art_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'institutions', ['institution_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__loans__instituti__4E88ABD4', 'institutions', ['institution_id'], ['id'])
        batch_op.create_foreign_key('FK__loans__work_of_a__4F7CD00D', 'works_of_art', ['work_of_art_id'], ['id'])

    # ### end Alembic commands ###
