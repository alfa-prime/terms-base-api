import ormar
from db.setup import metadata, database


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
