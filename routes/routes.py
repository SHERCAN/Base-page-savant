# -----------------------------------modules-----------------------------
from security.verify_route import VerifyTokenRoute
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
from security.auth import auth_routes
from dotenv import load_dotenv
from config.bd import dataBase
load_dotenv()

routes = APIRouter(route_class=VerifyTokenRoute)
# routes = APIRouter()

templates = Jinja2Templates(directory='templates')


@routes.get('/index', response_class=HTMLResponse)
async def main(request: Request):
    data = dataBase.readDataData()[0]
    data.pop('_id')
    context = {'request': request, 'data': data}
    response = templates.TemplateResponse('index.html', context=context)
    return response


@routes.get('/', response_class=HTMLResponse)
async def main():
    response = RedirectResponse('/index')
    return response


@routes.get('/addclient', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('addclient.html', context=context)
    return response


@routes.post('/addclient', response_class=HTMLResponse)
async def main(state: str = Form(), city: str = Form(), client: str = Form(), request: Request = None):
    context = {'request': request}
    dataBase.sendClient({'state': state, 'city': city, 'client': client})
    response = templates.TemplateResponse('addclient.html', context=context)
    return response


@routes.get('/token', response_class=HTMLResponse)
async def main(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('token.html', context=context)
    return response


# @routes.post('/', response_class=HTMLResponse)
# async def main(request: Request):

#     context = {'request': request}
#     response = templates.TemplateResponse('index.html', context=context)
#     return response
