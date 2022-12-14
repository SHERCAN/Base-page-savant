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
from fastapi.responses import FileResponse
from fastapi import APIRouter
from starlette.responses import RedirectResponse
import pathlib
from security.jwt_functions import validate_token, write_token
import json
from csv import DictWriter
from security.auth import auth_routes
from classobject.classes import signupClass, Hash
from config.bd import dataBase
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.status import HTTP_302_FOUND
from security.jwt_functions import validate_token, write_token

main = APIRouter()

templates = Jinja2Templates(directory='templates')


@main.get('/signin', response_class=HTMLResponse)
async def signin(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('signin.html', context=context)
    return response


@main.post("/signin")
async def login(email: str = Form(), password: str = Form(), request: Request = None):
    try:
        user = list(dataBase.readUser(id=email))
    except:
        # sin conexión base de datos
        context = {'request': request, 'message': 'BD'}
        response = templates.TemplateResponse(
            'signin.html', context=context)
        return response
    if len(user) > 0:
        if Hash.verify_password(password, user[0]['password']):
            token = write_token({'email': email})
            response = RedirectResponse('/', status_code=HTTP_302_FOUND)
            response.set_cookie(key="Authorization", value=token)
        else:
            context = {'request': request, 'message': 'IP'}
            response = templates.TemplateResponse(
                'signin.html', context=context)
    else:
        context = {'request': request, 'message': 'ENT'}
        response = templates.TemplateResponse(
            'signin.html', context=context)
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


@main.get("/get_csv")
async def get_csv():
    return FileResponse('data.csv', filename='data.csv')


@main.post('/addData')
async def webhook(request: dict):
    dataBase.sendData(request)
    return ''


@main.get("/get_register/{cli}/{reg}",response_class=JSONResponse)
async def get_register(request:Request,reg: str, cli: str):
    #cli es cliente y reg es el registro a solicitar
    documentos : list= dataBase.readDataData()[0]
    documentos.pop("_id")
    print(documentos)
    for _, value in documentos.items():
    # Recorre todos los campos del documento
        for campo, valor in value.items():
            print(valor.replace(" ", ""),reg)
            # Si el valor del campo es igual al valor buscado, muestra el nombre del campo
            if valor.replace(" ", "") ==reg:
                keyCampo=campo
                break
    print(keyCampo)
    consulta= [{'client':cli},{keyCampo:1}]
    getData = dataBase.readData(consulta)
    base = list(getData).copy()
    for data in base:
        data['data']=data[keyCampo]
        data.pop(keyCampo)
        data.pop('_id')
    base = jsonable_encoder(base)
    return JSONResponse(content=base)
