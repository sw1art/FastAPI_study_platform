import uvicorn
from fastapi import FastAPI, APIRouter
from settings import settings
from api.routers import user_router


app = FastAPI(title='Study platform')

api_router = APIRouter()

api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)