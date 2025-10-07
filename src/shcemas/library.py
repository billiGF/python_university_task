from pydantic import BaseModel, validator

class CategoryCreate(BaseModel):
    name: str


class Pagination(BaseModel):
    limit: str
    offset: str

class MagazineCreate(BaseModel):
    name: str
    theme: int