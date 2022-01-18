import asyncio
import uvicorn
from fastapi import FastAPI
from config import settings
from models.basemeta import BaseMeta
from routes.all import categories_route, terms_route
from db.init import populate_db

# Create and setup FastAPI instance https://fastapi.tiangolo.com/tutorial/first-steps/
app = FastAPI(
    title=settings.app_title,
    description=settings.api_description,
    docs_url=settings.api_ver_prefix + settings.api_doc_endpoint,
    redoc_url=None
)

# database initialization & connection https://collerek.github.io/ormar/fastapi/
app.state.database = BaseMeta.database


@app.on_event("startup") # noqa
async def startup() -> None:
    """ Connect db on app startup. """
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """ Disconnect db on app shutdown. """
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

# add routes to app https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=include#include-an-apirouter-in-another
app.include_router(terms_route)
app.include_router(categories_route)


async def run_app():
    """ Start app. """
    await populate_db()

    # run server https://www.uvicorn.org/#running-programmatically, https://fastapi.tiangolo.com/deployment/manually/
    uvicorn.run("main:app", reload=True, debug=True)


if __name__ == "__main__":
    asyncio.run(run_app())
