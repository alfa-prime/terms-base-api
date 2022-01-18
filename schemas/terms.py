import pydantic

from schemas.categories import CategoryNoId


class TermIn(pydantic.BaseModel):
    class Config:
        orm_mode = True

    name_eng: str
    name_rus: str
    category: CategoryNoId


class TermOut(pydantic.BaseModel):
    class Config:
        orm_mode = True

    id: int
    name_eng: str
    name_rus: str
    category: CategoryNoId
