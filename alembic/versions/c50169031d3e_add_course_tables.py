"""add course tables

Revision ID: c50169031d3e
Revises: 1e6f2f97950a
Create Date: 2022-09-21 14:33:47.934900

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "c50169031d3e"
down_revision = "1e6f2f97950a"
branch_labels = None
depends_on = None


def upgrade() -> None:    
    course_level_table = op.create_table(
        "course_level",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("level", sa.Integer, unique=True),
        sa.Column("name", sa.String(100), unique=True, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column("updated_at", sa.TIMESTAMP, server_default=sa.func.now()),
    )

    op.bulk_insert(
        course_level_table,
        [
            {"level": 1, "name": "superbeginner"},
            {"level": 2, "name": "beginner"},
            {"level": 3, "name": "intermediate"},
            {"level": 4, "name": "advanced"},
        ],
    )
    op.create_table(
        "course",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Unicode(100), unique=True, nullable=False),
        sa.Column("description", sa.Unicode(1000), nullable=True),
        sa.Column("level_id", sa.Integer, sa.ForeignKey('course_level.id'), unique=True),
        sa.Column("youtube_link", sa.String(100), nullable=True),
        sa.Column("is_free", sa.Boolean, nullable=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("course")
    op.drop_table("course_level")
