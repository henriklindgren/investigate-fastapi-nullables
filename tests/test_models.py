from models import Variant10Model, Variant11Model, Variant12Model, Variant13Model, Variant20Model, Variant21Model, \
    Variant22Model, Variant23Model

_NOT_SET = object()


def test_variant_1_0():
    resulting_schema = Variant10Model().schema()
    assert resulting_schema['properties']['field1'].get('nullable', _NOT_SET) == _NOT_SET
    assert resulting_schema['properties']['field2'].get('nullable', _NOT_SET) == _NOT_SET
    assert resulting_schema['properties']['field3'].get('nullable', _NOT_SET) == _NOT_SET


def test_variant_1_1():
    resulting_schema = Variant11Model().schema()
    assert resulting_schema['properties']['field1'].get('nullable', _NOT_SET) == _NOT_SET
    assert resulting_schema['properties']['field2'].get('nullable', _NOT_SET) == _NOT_SET
    assert resulting_schema['properties']['field3'].get('nullable', _NOT_SET) == _NOT_SET


def test_variant_1_2():
    resulting_schema = Variant12Model().schema()
    assert resulting_schema['properties']['field1']['nullable'] is True
    assert resulting_schema['properties']['field2']['nullable'] is True
    assert resulting_schema['properties']['field3']['nullable'] is True


def test_variant_1_3():
    resulting_schema = Variant13Model().schema()
    assert resulting_schema['properties']['field1']['nullable'] is True
    assert resulting_schema['properties']['field2']['nullable'] is True
    assert resulting_schema['properties']['field3']['nullable'] is True


def test_variant_2_0():
    resulting_schema = Variant20Model().schema()
    assert resulting_schema['properties']['field1']['nullable'] is True
    assert resulting_schema['properties']['field2']['nullable'] is True
    assert resulting_schema['properties']['field3']['nullable'] is True


def test_variant_2_1():
    resulting_schema = Variant21Model().schema()
    assert resulting_schema['properties']['field1']['nullable'] is True
    assert resulting_schema['properties']['field2']['nullable'] is True
    assert resulting_schema['properties']['field3']['nullable'] is True


def test_variant_2_2():
    resulting_schema = Variant22Model().schema()
    assert resulting_schema['properties']['field1']['nullable'] is True
    assert resulting_schema['properties']['field2']['nullable'] is True
    assert resulting_schema['properties']['field3']['nullable'] is True


def test_variant_2_3():
    resulting_schema = Variant23Model().schema()
    assert resulting_schema['properties']['field1']['nullable'] is True
    assert resulting_schema['properties']['field2']['nullable'] is True
    assert resulting_schema['properties']['field3']['nullable'] is True


