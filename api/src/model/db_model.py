# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Account(Base):
    __tablename__ = 'account'

    account_id = Column(Integer, primary_key=True, server_default=text("nextval('account_account_id_seq'::regclass)"))
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=text("timezone('utc'::text, CURRENT_TIMESTAMP)"))
    updated_at = Column(DateTime, server_default=text("timezone('utc'::text, CURRENT_TIMESTAMP)"))


class AccountRole(Base):
    __tablename__ = 'account_role'

    role_id = Column(Integer, primary_key=True, server_default=text("nextval('account_role_role_id_seq'::regclass)"))
    name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=text("timezone('utc'::text, CURRENT_TIMESTAMP)"))
    updated_at = Column(DateTime, server_default=text("timezone('utc'::text, CURRENT_TIMESTAMP)"))


class CourseLevel(Base):
    __tablename__ = 'course_level'

    id = Column(Integer, primary_key=True, server_default=text("nextval('course_level_id_seq'::regclass)"))
    level = Column(Integer, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))


class AccountAccessCode(Base):
    __tablename__ = 'account_access_code'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_access_code_id_seq'::regclass)"))
    account_id = Column(ForeignKey('account.account_id'), nullable=False, unique=True)
    keycode = Column(String(100), nullable=False)
    passcode = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("timezone('utc'::text, CURRENT_TIMESTAMP)"))
    expire_at = Column(DateTime, nullable=False, index=True, server_default=text("(timezone('utc'::text, CURRENT_TIMESTAMP) + ((10)::double precision * '00:01:00'::interval))"))

    account = relationship('Account', uselist=False)


class AccountRoleAssignment(Base):
    __tablename__ = 'account_role_assignment'

    assignment_id = Column(Integer, primary_key=True, server_default=text("nextval('account_role_assignment_assignment_id_seq'::regclass)"))
    account_id = Column(ForeignKey('account.account_id'), nullable=False, unique=True)
    role_id = Column(ForeignKey('account_role.role_id'), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, server_default=text("timezone('utc'::text, CURRENT_TIMESTAMP)"))

    account = relationship('Account', uselist=False)
    role = relationship('AccountRole', uselist=False)


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, server_default=text("nextval('course_id_seq'::regclass)"))
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(1000))
    level_id = Column(ForeignKey('course_level.id'), unique=True)
    youtube_link = Column(String(100))
    is_free = Column(Boolean)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))

    level = relationship('CourseLevel', uselist=False)
