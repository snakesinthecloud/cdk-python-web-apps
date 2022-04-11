"""A basic FastAPI app."""
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from mangum import Mangum
from pydantic import BaseSettings

from routers.example.views import api as example


class Settings(BaseSettings):
    app_name: str = 'CDK FastAPI'
    app_version: str = '0.1'


# Don't use root_path if you are using a custom domain name for API Gateway
stage = os.environ.get('STAGE', None)
root_path = f'/{stage}' if stage else '/'


settings = Settings()
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    root_path=root_path,
)
app.include_router(example)
templates = Jinja2Templates(directory='templates')


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse(
        'index.html', {'request': request, 'product': 'FastAPI'}
    )


@app.get('/settings')
async def info():
    return {
        'app_name': settings.app_name,
    }


handler = Mangum(app)

if __name__ == '__main__':
    uvicorn.run('main:app')
