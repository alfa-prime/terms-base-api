import ormar

from models.basemeta import BaseMeta
from models.categories import Category


class Term(ormar.Model):
    class Meta(BaseMeta):
        tablename = "terms"
        constraints = [ormar.UniqueColumns("name_eng", "name_rus", "category")]

    id: int = ormar.Integer(primary_key=True)
    name_eng: str = ormar.String(max_length=100, index=True)
    name_rus: str = ormar.String(max_length=100, index=True)
    category: Category = ormar.ForeignKey(Category)
