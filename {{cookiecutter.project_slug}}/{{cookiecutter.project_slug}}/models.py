from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Numeric
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime as DateTimeType


class utcnow(expression.FunctionElement):
    type = DateTimeType()


@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


Base = declarative_base()


class DBMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, server_default=utcnow())
    modified_date = Column(DateTime, server_default=utcnow(), onupdate=utcnow())

    def to_dict(self):
        d = self.__dict__.copy()
        if '_sa_instance_state' in d:
            d.pop('_sa_instance_state')
        return d


def ReferenceCol(tablename, nullable=False, **kw):
    return Column(ForeignKey('{}.id'.format(tablename)), nullable=nullable, **kw)
