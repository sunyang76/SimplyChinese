from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker


@contextmanager
def db_session(connection_string, database=None, echo=False):
    """
    create a database session
    """
    connect_args = {}
    if database:
        connect_args["database"] = database

    engine = create_engine(connection_string, connect_args=connect_args, echo=echo)
    Session = sessionmaker(engine)
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()
        engine.dispose()


def session_manager(conn_string, database=None, echo=False):
    """
    session manager decorator. this will expect the function to have a named parameter session
    """
    def session_decorator(db_func):
        def wrapper(*args, **kwargs):
            session_arg = kwargs.get("session", None)
            if session_arg:
                return db_func(*args, **kwargs)
            else:
                with db_session(
                    conn_string, database=database, echo=echo
                ) as new_session:
                    kwargs["session"] = new_session
                    return db_func(*args, **kwargs)

        return wrapper

    return session_decorator
