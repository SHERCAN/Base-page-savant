# -----------------------------------modules-----------------------------
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates
from security.auth import auth_routes
from routes.routes import routes
from routes.main import main

# -----------------------------------run---------------

app = FastAPI(title='Server Enerion',
              description='Server with all data for SAVANT', version='0.0.1')
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(main)
app.include_router(auth_routes, prefix='/api')
app.include_router(routes)

if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, log_level='info',
                access_log=False, reload=True)
