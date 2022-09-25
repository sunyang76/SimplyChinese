"""create account table

Revision ID: 1e6f2f97950a
Revises: 
Create Date: 2022-09-21 14:17:18.631941

"""
from enum import unique
from alembic import op
import sqlalchemy as sa
from common.db.sqla_ext import utcnow
from common.db.sqla_ext import expiretime

# revision identifiers, used by Alembic.
revision = "1e6f2f97950a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    account_role_table = op.create_table(
        "account_role",
        sa.Column("role_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), unique=True, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=utcnow()),
        sa.Column("updated_at", sa.TIMESTAMP, server_default=utcnow()),
    )

    op.bulk_insert(
        account_role_table,
        [
            {"role_id": 1, "name": "admin"},
            {"role_id": 2, "name": "author"},
            {"role_id": 3, "name": "tutor"},
            {"role_id": 100, "name": "student"},
        ],
    )

    account_table = op.create_table(
        "account",
        sa.Column("account_id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(100), unique=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=utcnow()),
        sa.Column("updated_at", sa.TIMESTAMP, server_default=utcnow()),
    )

    op.create_index("ix_account_email", "account", ["email"])

    op.create_table(
        "account_role_assignment",
        sa.Column("assignment_id", sa.Integer, primary_key=True),
        sa.Column(
            "account_id",
            sa.Integer,
            sa.ForeignKey("account.account_id"),
            unique=True,
            nullable=False,
        ),
        sa.Column(
            "role_id",
            sa.Integer,
            sa.ForeignKey("account_role.role_id"),
            unique=True,
            nullable=False,
        ),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False, server_default=utcnow()),
    )

    op.create_table(
        "account_access_code",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "account_id",
            sa.Integer,
            sa.ForeignKey("account.account_id"),
            unique=True,
            nullable=False,
        ),
        sa.Column("keycode", sa.String(100), nullable=False),
        sa.Column("passcode", sa.Integer, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False, server_default=utcnow()),
        sa.Column(
            "expire_at",
            sa.TIMESTAMP,
            nullable=False,
            server_default=expiretime(),
        ),
    )

    op.create_index("ix_account_id", "account_access_code", ["account_id"])
    op.create_index("ix_expire_at", "account_access_code", ["expire_at"])

    # add initializtion data
    # op.bulk_insert(
    #     account_table,
    #     [
    #         {
    #             "email": "sunyang76@gmail.com",
    #             "name": "Yang Sun",
    #         }
    #     ],
    # )


def downgrade() -> None:
    op.drop_table("account_access_code")
    op.drop_table("account_role_assignment")
    op.drop_table("account")
    op.drop_table("account_role")
