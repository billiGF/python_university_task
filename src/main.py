import uvicorn
from fastapi import FastAPI
from api.library import router
from core.config import settings

app = FastAPI(title=settings.app_title)
app.include_router(router)

if __name__ == '__main__':
    #Runing app
    uvicorn.run("main:app", reload=True)