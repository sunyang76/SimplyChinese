from fastapi import APIRouter, Depends, HTTPException

# from dependencies import get_token_header

router = APIRouter(
    prefix="/account",
    tags=["account"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.post("/login")
async def login_account():
    ...

@router.post("/signup")
async def signup_new_account():
    ...

