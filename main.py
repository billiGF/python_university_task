import uvicorn
from fastapi import FastAPI
from src.api.library import router
from src.core.config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.app_title)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    #Runing app
    uvicorn.run("main:app", reload=True)