"""add course tables

Revision ID: c50169031d3e
Revises: 1e6f2f97950a
Create Date: 2022-09-21 14:33:47.934900

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = "c50169031d3e"
down_revision = "1e6f2f97950a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    now = datetime.now()
    course_level_table = op.create_table(
        "course_level",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("level", sa.Integer, unique=True),
        sa.Column("name", sa.String(100), unique=True, nullable=False),
        sa.Column("create_at", sa.DateTime, nullable=False),
        sa.Column("update_at", sa.DateTime, nullable=False),
    )

    op.bulk_insert(course_level_table, [
        {
            "level": 1,            
            "name":"beginner",
            "create_at": now,
            "update_at": now
        },
        {
            "level": 2,
            "name":"intermediate",
            "create_at": now,
            "update_at": now
        },
        {
            "level": 3,
            "name":"advanced",
            "create_at": now,
            "update_at": now
        }
    ])
    op.create_table(
        "course",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Unicode(100), unique=True, nullable=False),
        sa.Column("description", sa.Unicode(1000), nullable=True),
        sa.Column("level", sa.Integer, unique=True),
        sa.Column("youtube_link", sa.String(100), nullable=True),
        sa.Column("create_at", sa.DateTime, nullable=False),
        sa.Column("update_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("account")
