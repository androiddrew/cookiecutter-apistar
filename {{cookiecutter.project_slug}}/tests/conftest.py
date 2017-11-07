from apistar.frameworks.wsgi import WSGIApp
from apistar.backends.sqlalchemy_backend import SQLAlchemyBackend, get_session

import pytest

from {{cookiecutter.project_slug}}.models import Base
from {{cookiecutter.project_slug}}.renders import JSONRenderer
from {{cookiecutter.project_slug}}.app import commands, routes, components

settings = {
    'DATABASE': {
        #'URL': 'postgresql://apistar:local@localhost/{{cookiecutter.project_slug}}',
        'URL': 'sqlite:///',
        'METADATA': Base.metadata
    },
    'RENDERERS': [JSONRenderer()],
}

backend = SQLAlchemyBackend(settings)


@pytest.fixture(autouse=True)
def create_db():
    """Creates a test database with session scope"""
    Base.metadata.create_all(backend.engine)

    yield

    Base.metadata.drop_all(backend.engine)


@pytest.fixture(name='rb_session')
def db_session_fixure():
    """Returns a SQLAlchemy session with automatic rollback"""
    session = backend.Session()
    try:
        yield session
        session.rollback()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@pytest.fixture(name='app', scope='session')
def apistar_app_fixture():
    """Returns a session scoped WSGIApp instance"""
    return WSGIApp(settings=settings,
                   commands=commands,
                   components=components,
                   routes=routes)