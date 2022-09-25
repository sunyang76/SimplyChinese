from fastapi import APIRouter
from model.accout_model import (
    AccessRequest,
    LoginByCodeRequest,
    SignupRequest,
    GenericResponse,
    LoginResponse,
)

# from dependencies import get_token_header

router = APIRouter(
    prefix="/account",
    tags=["account"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("/get_access")
async def get_access(user: AccessRequest) -> GenericResponse:
    ...


@router.post("/login")
async def login_account(user: LoginByCodeRequest) -> LoginResponse:
    ...


@router.post("/signup")
async def signup_new_account(user: SignupRequest) -> GenericResponse:
    ...
