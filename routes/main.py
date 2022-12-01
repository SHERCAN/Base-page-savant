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
from classobject.classes import signupClass, Hash

main = APIRouter()

templates = Jinja2Templates(directory='templates')


@main.get('/signin', response_class=HTMLResponse)
async def signin(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('signin.html', context=context)
    return response


@main.post('/userin', response_class=HTMLResponse)
async def signin(username: str = Form(), password: str = Form(), email: str = Form(), code: str = Form(), request: Request = None):
    insert = None
    if code == 'enerion':
        insert = signupClass.postUser(email=email, password=Hash.get_password_hash(
            password), username=username)

    if insert is not None:
        context = {'request': request, 'message': 'User created'}
        response = templates.TemplateResponse('signin.html', context=context)
        return response
    else:
        context = {'request': request, 'message': 'AAC'}
        response = templates.TemplateResponse('signup.html', context=context)
        return response


@main.get('/signup', response_class=HTMLResponse)
async def signup(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('signup.html', context=context)
    return response
