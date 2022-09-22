# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_id_seq'::regclass)"))
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    create_at = Column(DateTime, server_default=text("now()"))
    update_at = Column(DateTime, server_default=text("now()"))


class CourseLevel(Base):
    __tablename__ = 'course_level'

    id = Column(Integer, primary_key=True, server_default=text("nextval('course_level_id_seq'::regclass)"))
    level = Column(Integer, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    create_at = Column(DateTime, server_default=text("now()"))
    update_at = Column(DateTime, server_default=text("now()"))


class AccountLogin(Base):
    __tablename__ = 'account_login'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_login_id_seq'::regclass)"))
    account_id = Column(ForeignKey('account.id'), nullable=False, unique=True)
    keycode = Column(String(100), nullable=False)
    passcode = Column(Integer, nullable=False)
    create_at = Column(DateTime, server_default=text("now()"))
    expire_at = Column(DateTime, index=True, server_default=text("now()"))

    account = relationship('Account', uselist=False)


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, server_default=text("nextval('course_id_seq'::regclass)"))
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(1000))
    level_id = Column(ForeignKey('course_level.id'), unique=True)
    youtube_link = Column(String(100))
    is_free = Column(Boolean)
    create_at = Column(DateTime, server_default=text("now()"))
    update_at = Column(DateTime, server_default=text("now()"))

    level = relationship('CourseLevel', uselist=False)
