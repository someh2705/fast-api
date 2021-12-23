from fastapi import FastAPI
from Router import cookie

app = FastAPI()

app.include_router(cookie.router)