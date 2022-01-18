import databases
import sqlalchemy

from config import settings

# database initialization https://collerek.github.io/ormar/fastapi/
metadata = sqlalchemy.MetaData()
database = databases.Database(settings.database_url)
