import sqlite3
from http import HTTPStatus
from typing import List

from fastapi import APIRouter

import errors
from config import settings
from models.categories import Category
from models.terms import Term
from schemas.terms import TermOut, TermIn

terms_route = APIRouter(prefix=f"{settings.api_ver_prefix}/terms", tags=["Terms"])


@terms_route.get("/", response_model=List[TermOut])
async def get_terms_list():
    terms_list = await Term.objects.select_related("category").all()
    return terms_list if terms_list else await errors.not_found()


@terms_route.post("/", response_model=TermIn, status_code=HTTPStatus.CREATED)
async def add_term(term: TermIn):
    category_exist = await Category.objects.filter(name=term.category.name).get()

    if not category_exist:
        errors.not_found(detail=f"category name '{term.category.name}' not exist")
    else:
        try:
            term.category = category_exist
            term_new = await Term(**term.dict()).save()
            return term_new.dict()
        except sqlite3.IntegrityError:
            errors.already_exist()






