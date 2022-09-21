"""create account table

Revision ID: 1e6f2f97950a
Revises: 
Create Date: 2022-09-21 14:17:18.631941

"""
from enum import unique
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = "1e6f2f97950a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    account_table = op.create_table(
        "account",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(100), unique=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("create_at", sa.DateTime, nullable=False),
        sa.Column("update_at", sa.DateTime, nullable=False),
    )

    now = datetime.now()

    op.bulk_insert(
        account_table,
        [
            {
                "email": "sunyang76@gmail.com",
                "name": "Yang Sun",
                "create_at": now,
                "update_at": now,
            }
        ],
    )

    account_table = op.create_table(
        "account_login",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("account_id", sa.String(100), unique=True, nullable=False),
        sa.Column("pass", sa.Integer, nullable=False),
        sa.Column("create_at", sa.DateTime, nullable=False),
        sa.Column("expire_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("account")
