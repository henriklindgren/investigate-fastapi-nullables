from typing import Optional, Union

from pydantic import BaseModel, Field


class Variant10Model(BaseModel):
    """
    Variant 1-0
    Using first thought, minimal effort typing
    """
    field1: Optional[str] = None
    field2: Optional[int] = None
    field3: Optional[bool] = None


class Variant11Model(BaseModel):
    """
    Variant 1-1
    Base case but with unions to hint null type
    """
    field1: Optional[Union[str, None]] = None
    field2: Optional[Union[int, None]] = None
    field3: Optional[Union[bool, None]] = None


class Variant12Model(BaseModel):
    """
    Variant 1-2
    Using @krisztianpinter's solution

    see https://github.com/pydantic/pydantic/issues/1270#issuecomment-734467055
    """
    field1: Optional[str] = Field(None, nullable=True)
    field2: Optional[int] = Field(None, nullable=True)
    field3: Optional[bool] = Field(None, nullable=True)


class Variant13Model(BaseModel):
    """
    Variant 1-3
    Mixing variant 1-1 and 1-2.
    """
    field1: Optional[Union[str, None]] = Field(None, nullable=True)
    field2: Optional[Union[int, None]] = Field(None, nullable=True)
    field3: Optional[Union[bool, None]] = Field(None, nullable=True)


class PatchedBaseModel(BaseModel):
    """
    Quickfix adding nullable=True to schema for OpenAPI 3.0 compatibility.
    From https://github.com/pydantic/pydantic/issues/1270#issuecomment-729555558
    and https://github.com/pydantic/pydantic/issues/1270#issuecomment-734454493
    """
    class Config:
        @staticmethod
        def schema_extra(schema, model):
            """Fixes nullable fields in OpenApi v3+ generator"""
            for prop, value in schema.get('properties', {}).items():
                # retrieve right field from alias or name
                field = [x for x in model.__fields__.values() if x.alias == prop][0]
                if field.allow_none:
                    if '$ref' in value:
                        if issubclass(field.type_, BaseModel):
                            # add 'title' in schema to have the exact same behaviour as the rest
                            value['title'] = field.type_.__config__.title or field.type_.__name__
                        value['anyOf'] = [{'$ref': value.pop('$ref')}]
                    value['nullable'] = True


class Variant20Model(PatchedBaseModel):
    """Variant 2-0"""
    field1: Optional[str] = None
    field2: Optional[int] = None
    field3: Optional[bool] = None


class Variant21Model(PatchedBaseModel):
    """Variant 2-1"""
    field1: Optional[Union[str, None]] = None
    field2: Optional[Union[int, None]] = None
    field3: Optional[Union[bool, None]] = None


class Variant22Model(PatchedBaseModel):
    """Variant 2-2"""
    field1: Optional[str] = Field(None, nullable=True)
    field2: Optional[int] = Field(None, nullable=True)
    field3: Optional[bool] = Field(None, nullable=True)


class Variant23Model(PatchedBaseModel):
    """
    Variant 2-3
    Mixing variant 2-1 and 2-2.
    """
    field1: Optional[Union[str, None]] = Field(None, nullable=True)
    field2: Optional[Union[int, None]] = Field(None, nullable=True)
    field3: Optional[Union[bool, None]] = Field(None, nullable=True)
