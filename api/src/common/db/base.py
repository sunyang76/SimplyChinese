from sqlalchemy import inspect


def object_as_dict(obj):
    if obj is None:
        return None

    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
