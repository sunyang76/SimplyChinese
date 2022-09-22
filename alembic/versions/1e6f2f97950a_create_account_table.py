"""create account table

Revision ID: 1e6f2f97950a
Revises: 
Create Date: 2022-09-21 14:17:18.631941

"""
from enum import unique
from alembic import op
import sqlalchemy as sa

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
        sa.Column("create_at", sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column("update_at", sa.TIMESTAMP, server_default=sa.func.now()),
    )

    op.create_index("ix_email", "account", ["email"])

    op.bulk_insert(
        account_table,
        [
            {
                "email": "sunyang76@gmail.com",
                "name": "Yang Sun",
            }
        ],
    )

    account_table = op.create_table(
        "account_login",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "account_id",
            sa.Integer,
            sa.ForeignKey("account.id"),
            unique=True,
            nullable=False,
        ),
        sa.Column("keycode", sa.String(100), nullable=False),
        sa.Column("passcode", sa.Integer, nullable=False),
        sa.Column("create_at", sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column("expire_at", sa.TIMESTAMP, server_default=sa.func.now()),
    )

    op.create_index("ix_account_id", "account_login", ["account_id"])
    op.create_index("ix_expire_at", "account_login", ["expire_at"])


def downgrade() -> None:
    op.drop_table("account_login")
    op.drop_table("account")
