from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.backends import sqlalchemy_backend
from apistar.backends.sqlalchemy_backend import Session
from apistar.handlers import docs_urls, static_urls

from .models import Base
from .renders import JSONRenderer


def welcome():
    return {"message": "welcome to {{cookiecutter.project_slug}}"}


routes = [
    Route('/', 'GET', welcome),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

_settings = {
    'DATABASE': {
        'URL': 'postgresql://@localhost/{{cookiecutter.project_name}}',
        'METADATA': Base.metadata
    },
    'RENDERERS': [JSONRenderer()]
}


routes = routes

commands = sqlalchemy_backend.commands

components = sqlalchemy_backend.components


def application_factory(settings={}):
    """Returns an instance of Cookie API"""
    app_settings = {**_settings, **settings}
    return App(settings=app_settings,
               commands=commands,
               components=components,
               routes=routes)
