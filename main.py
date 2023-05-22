from typing import Optional, Union

from fastapi import FastAPI, Query, Depends

app = FastAPI()


class Variant30(object):
    def __init__(
            self,
            field1: Optional[str] = None,
            field2: Optional[int] = None,
            field3: Optional[bool] = None,
    ):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


class Variant31(object):
    def __init__(
            self,
            field1: Optional[Union[str]] = None,
            field2: Optional[Union[int]] = None,
            field3: Optional[Union[bool]] = None,
    ):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


class Variant32(object):
    def __init__(
            self,
            field1: Optional[str] = Query(None, nullable=True),
            field2: Optional[int] = Query(None, nullable=True),
            field3: Optional[bool] = Query(None, nullable=True),
    ):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


@app.get('/variant30')
def variant30(variant30: Variant30 = Depends()):
    pass


@app.get('/variant31')
def variant31(variant31: Variant31 = Depends()):
    pass


@app.get('/variant32')
def variant32(variant32: Variant32 = Depends()):
    pass


@app.get('/optional-variant32')
def optional_variant32(variant32: Optional[Variant32] = Depends()):
    pass


@app.get(
    '/variant32/sub',
    dependencies=[Depends(variant32)],
)
def variant32_subdependency():
    pass
