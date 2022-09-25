import uuid
import random
from datetime import datetime, timedelta
from common.db.decorator import session_manager
from common.db.base import object_as_dict
from model.db_model import Account
from model.db_model import AccountAccessCode
from datetime import timezone
from datetime import datetime
from datetime import timedelta
import jwt

import sqlalchemy as sa
import setting


@session_manager(setting.SCDB_CONNECT_STRING)
def exists(email, session=None):
    return bool(
        object_as_dict(session.query(Account).filter(Account.email == email).first())
    )


@session_manager(setting.SCDB_CONNECT_STRING)
def delete(email, session=None):
    existing_record = session.query(Account).filter(Account.email == email).first()
    if existing_record:
        session.delete(existing_record)
        return True
    else:
        return False


@session_manager(setting.SCDB_CONNECT_STRING)
def signup(email, name, session=None):
    email = email.lower()

    if not exists(email, session=session):
        new_account = Account(email=email, name=name)
        session.add(new_account)
        return True
    else:
        return False


@session_manager(setting.SCDB_CONNECT_STRING)
def login_request(email, session=None):
    existing_record = session.query(Account).filter(Account.email == email).first()
    if existing_record:
        ...
    else:
        raise "user does not exist"


@session_manager(setting.SCDB_CONNECT_STRING)
def login(email, keycode=None, passcode=None, session=None):
    existing_account = session.query(Account).filter(Account.email == email).first()
    if existing_account:
        login_rec = (
            session.query(AccountAccessCode)
            .filter(
                sa.and_(AccountAccessCode.account_id == existing_account.account_id),
                sa.or_(
                    AccountAccessCode.keycode == keycode,
                    AccountAccessCode.passcode == passcode,
                ),
            )
            .first()
        )

        if login_rec and login_rec.expire_at > datetime.utcnow():
            return "KEY"
    return None


@session_manager(setting.SCDB_CONNECT_STRING)
def generate_login_code(email, session=None):
    existing_account = session.query(Account).filter(Account.email == email).first()
    created_at = datetime.utcnow()
    expire_at = created_at + timedelta(minutes=10)
    if existing_account:
        session.query(AccountAccessCode).filter(
            AccountAccessCode.account_id == existing_account.account_id
        ).delete()
        new_login_rec = AccountAccessCode(
            account_id=existing_account.account_id,
            keycode=uuid.uuid1().hex,
            passcode=random.randrange(100000, 999999),
            created_at=created_at,
            expire_at=expire_at,
        )
        session.add(new_login_rec)
        return object_as_dict(new_login_rec)
    else:
        return None


def create_jwt_token(email, name, exp_in_seconds):
    iat = datetime.now(tz=timezone.utc)
    exp = iat + timedelta(seconds=exp_in_seconds)
    payload = {"email": email, "name": name, "iat": iat, "exp": exp}

    token = jwt.encode(payload, "secret")
    return token
