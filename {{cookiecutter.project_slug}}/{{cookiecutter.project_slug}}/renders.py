import datetime as dt
import decimal
import json

from apistar import http
from apistar.renderers import Renderer


def extended_encoder(obj):
    """JSON encoder function with support for ISO 8601 datetime serialization and Decimal to float casting"""
    if isinstance(obj, dt.datetime):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


class JSONRenderer(Renderer):
    """JSON Render with support for ISO 8601 datetime serialization and Decimal to float casting"""
    media_type = 'application/json'
    charset = None

    def render(self, data: http.ResponseData) -> bytes:
        return json.dumps(data, default=extended_encoder).encode('utf-8')