import datetime as dt
from decimal import Decimal
import json

from {{cookiecutter.project_slug}}.renders import extended_encoder, JSONRenderer


def test_extended_encoder_date_parsing():
    test_date = dt.datetime(2017, 5, 10)
    assert test_date.isoformat() == extended_encoder(test_date)


def test_extended_encoder_decimal_casting():
    test_decimal = Decimal('1.0')
    assert 1.0 == extended_encoder(test_decimal)


def test_render_with_extended_encoder():
    test_date = dt.datetime(2017, 5, 10)
    test_decimal = Decimal('0.1')
    expected = dict(my_date="2017-05-10T00:00:00", my_float=0.1)
    test_response = dict(my_date=test_date, my_float=test_decimal)
    assert json.dumps(expected).encode('utf-8') == JSONRenderer().render(test_response)