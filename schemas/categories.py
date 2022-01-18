import pydantic


class CategoryNoId(pydantic.BaseModel):
    class Config:
        orm_mode = True

    name: str


class CategoryOut(pydantic.BaseModel):
    class Config:
        orm_mode = True

    id: int
    name: str
