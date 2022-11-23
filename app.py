# -----------------------------------modules-----------------------------
import uvicorn
from fastapi import FastAPI
# from routes.main import web
# from config.var_env import mode
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import datetime as dt
from fastapi import APIRouter
from starlette.responses import RedirectResponse
import pathlib
import json


# -----------------------------------run---------------
app = FastAPI(title='Config MPPT',
              description='Configuration of the BMS server', version='0.0.1')
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/static", StaticFiles(directory="static"), name="js")


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response


@app.get('/button', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('button.html', context=context)
    return response


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response


if __name__ == '__main__':
    uvicorn.run('app:app', log_level='info', access_log=False, reload=True)
