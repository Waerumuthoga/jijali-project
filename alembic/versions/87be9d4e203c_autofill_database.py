"""autofill database

Revision ID: 87be9d4e203c
Revises: 1318ad272dca
Create Date: 2025-01-08 20:45:44.719095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87be9d4e203c'
down_revision: Union[str, None] = '1318ad272dca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('journals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('todays_happenings', sa.String(), nullable=False),
    sa.Column('special_moments', sa.String(), nullable=False),
    sa.Column('redo_your_day', sa.String(), nullable=False),
    sa.Column('handling_stress', sa.String(), nullable=False),
    sa.Column('done_different', sa.String(), nullable=False),
    sa.Column('thoughts_and_emotions', sa.String(), nullable=False),
    sa.Column('gratitude', sa.String(), nullable=False),
    sa.Column('goals_and_intentions', sa.String(), nullable=False),
    sa.Column('status', sa.Boolean(), server_default='False', nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('moods', sa.Column('status', sa.Boolean(), server_default='False', nullable=True))
    op.add_column('moods', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('moods', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'moods', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'moods', type_='foreignkey')
    op.drop_column('moods', 'owner_id')
    op.drop_column('moods', 'created_at')
    op.drop_column('moods', 'status')
    op.drop_table('journals')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###