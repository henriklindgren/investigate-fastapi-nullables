import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture(scope='module')
def client():
    return TestClient(app)


_NOT_SET = object()


def test_variants(client):
    r = client.get('/openapi.json')
    assert r.status_code == 200
    r_json = r.json()
    assert r_json['openapi'], '3.0.2'

    variant30_field1 = r_json['paths']['/variant30']['get']['parameters'][0]
    assert variant30_field1['name'], 'field1'
    assert variant30_field1['schema'].get('nullable', _NOT_SET) is _NOT_SET

    variant30_field2 = r_json['paths']['/variant30']['get']['parameters'][0]
    assert variant30_field2['name'], 'field2'
    assert variant30_field2['schema'].get('nullable', _NOT_SET) is _NOT_SET

    variant30_field3 = r_json['paths']['/variant30']['get']['parameters'][0]
    assert variant30_field3['name'], 'field3'
    assert variant30_field3['schema'].get('nullable', _NOT_SET) is _NOT_SET

    variant31_field1 = r_json['paths']['/variant31']['get']['parameters'][0]
    assert variant31_field1['name'], 'field1'
    assert variant31_field1['schema'].get('nullable', _NOT_SET) is _NOT_SET

    variant31_field2 = r_json['paths']['/variant31']['get']['parameters'][0]
    assert variant31_field2['name'], 'field2'
    assert variant31_field2['schema'].get('nullable', _NOT_SET) is _NOT_SET

    variant31_field3 = r_json['paths']['/variant31']['get']['parameters'][0]
    assert variant31_field3['name'], 'field3'
    assert variant31_field3['schema'].get('nullable', _NOT_SET) is _NOT_SET

    variant32_field1 = r_json['paths']['/variant32']['get']['parameters'][0]
    assert variant32_field1['name'], 'field1'
    assert variant32_field1['schema'].get('nullable', _NOT_SET) is True

    variant32_field2 = r_json['paths']['/variant32']['get']['parameters'][0]
    assert variant32_field2['name'], 'field2'
    assert variant32_field2['schema'].get('nullable', _NOT_SET) is True

    variant32_field3 = r_json['paths']['/variant32']['get']['parameters'][0]
    assert variant32_field3['name'], 'field3'
    assert variant32_field3['schema'].get('nullable', _NOT_SET) is True
