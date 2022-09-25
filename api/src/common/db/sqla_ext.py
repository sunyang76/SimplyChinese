from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


class expiretime(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(expiretime, "postgresql")
def pg_expiretime(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP) + (10 * interval '1 minute')"
