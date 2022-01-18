import sqlite3
from http import HTTPStatus
from typing import List

import ormar.exceptions
from fastapi import APIRouter

from config import settings
from db.base import Category
from models.terms import Term
from schemas.categories import CategoryNoId, CategoryOut
import errors

categories_route = APIRouter(prefix=f"{settings.api_ver_prefix}/categories", tags=["Categories"])


@categories_route.get("/", response_model=List[CategoryOut])
async def list_categories():
    """
    Get list of categories.

    :return: List[Category], otherwise, not found
    """
    categories_list = await Category.objects.all()
    return categories_list if categories_list else await errors.not_found()


@categories_route.get("/{category_id}", response_model=Category)
async def get_category(category_id: int):
    """
    Get category.

    :param category_id: category ID
    :return:  Category, otherwise, not found
    """
    try:
        return await Category.objects.get(id=category_id)
    except ormar.exceptions.NoMatch:
        await errors.not_found()


@categories_route.post("/", response_model=CategoryNoId, status_code=HTTPStatus.CREATED)
async def add_category(category: CategoryNoId):
    """
    Add category

    :return: new Category name, otherwise, already exist
    """
    try:
        category.name = category.name.lower()
        return await Category(**category.dict()).save()
    except sqlite3.IntegrityError:
        await errors.already_exist()


@categories_route.put("/{category_id}", response_model=Category)
async def update_category(category_id: int, category: CategoryNoId):
    try:
        category.name = category.name.lower()
        category_exist = await Category.objects.get(id=category_id)
        return await category_exist.update(**category.dict())
    except ormar.exceptions.NoMatch:
        await errors.not_found()


@categories_route.delete("/{category_id}", status_code=HTTPStatus.OK)
async def delete_category(category_id: int, keep_terms: bool = False):
    """
    Delete category.

    :param category_id : category ID
    :param keep_terms: True - deletes a category, relations with terms, but leaves the terms,
                       False - removes a category and related terms, defaults to False
    :return: True if successful, otherwise, not found
    """
    try:
        category = await Category.objects.get(id=category_id)
        await category.terms.clear(keep_reversed=keep_terms)
        await category.delete()
        return True
    except ormar.exceptions.NoMatch:
        await errors.not_found()

