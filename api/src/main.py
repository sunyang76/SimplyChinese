from fastapi import Depends, FastAPI
import uvicorn
# from dependencies import get_query_token, get_token_header
from routers import account

# app = FastAPI(dependencies=[Depends(get_query_token)])

app=FastAPI()
app.include_router(account.router)


@app.get("/")
async def status():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
