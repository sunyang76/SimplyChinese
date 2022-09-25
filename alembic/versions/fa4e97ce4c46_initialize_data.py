"""initialize data

Revision ID: fa4e97ce4c46
Revises: c50169031d3e
Create Date: 2022-09-25 14:38:45.725219

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = "fa4e97ce4c46"
down_revision = "c50169031d3e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
INSERT INTO account (email, "name") VALUES ('sunyang76@gmail.com', 'Yang Sun');

INSERT INTO account_role_assignment (account_id, role_id) VALUES (LASTVAL(), 1);
    """);    


def downgrade() -> None:
    op.execute(
        """
DELETE FROM account_role_assignment 
WHERE role_id = 1 AND account_id IN (
    SELECT account_id FROM account WHERE email ='sunyang76@gmail.com'
);

DELETE FROM account where email = 'sunyang76@gmail.com';
    """
    )
