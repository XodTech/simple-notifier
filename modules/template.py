# REQUIRES:

#pylint: disable=missing-docstring
#pylint: disable=import-error

from fastapi import APIRouter

router = APIRouter()

@router.post("/template")
def handle_template() -> dict:
    pass
