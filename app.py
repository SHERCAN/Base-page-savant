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
from security.auth import auth_routes
from routes.routes import routes
from routes.main import main
from dotenv import load_dotenv
from os import getenv
load_dotenv()

# -----------------------------------run---------------

app = FastAPI(title='Server Enerion',
              description='Server with all data for SAVANT', version='0.0.1')
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(main)
app.include_router(auth_routes, prefix='/api')
app.include_router(routes)

if __name__ == '__main__':
    uvicorn.run('app:app', log_level='info', access_log=False, reload=True)
