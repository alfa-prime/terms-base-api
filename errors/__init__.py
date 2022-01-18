from http import HTTPStatus
from fastapi import HTTPException


def not_found(detail="not found"):
    raise HTTPException(detail=detail, status_code=HTTPStatus.NOT_FOUND)


def already_exist(detail="already exist"):
    raise HTTPException(detail=detail, status_code=HTTPStatus.BAD_REQUEST)
