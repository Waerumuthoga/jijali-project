"""creating moods table

Revision ID: 1318ad272dca
Revises: 
Create Date: 2025-01-08 20:30:48.976273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1318ad272dca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('moods', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=True,),
                    sa.Column('mood', sa.String(), nullable=False,),
                    sa.Column('feel', sa.String(), nullable=False,),
                    sa.Column('todays_influence', sa.String(), nullable=False,),
                    sa.Column('mood_shift', sa.String(), nullable=False,),
                    sa.Column('fears_and_anxieties', sa.String(), nullable=False,),
                    sa.Column('affect', sa.String(), nullable=False,),
                    sa.Column('steps', sa.String(), nullable=False,),
                    sa.Column('negative_thoughts', sa.String(), nullable=False,),
                    sa.Column('main_thoughts', sa.String(), nullable=True,),
                    sa.Column('support', sa.String(), nullable=False,),
                    )
    pass


def downgrade() -> None:
    op.drop_table('moods')
    pass
