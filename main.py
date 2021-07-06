from fastapi import FastAPI, APIRouter ,Request

#Controlarores
from controllers.provincias_controllers import router as provincia_router

#Aplicacion
app = FastAPI()

#Rutas API
api_router = APIRouter()
app.include_router(provincia_router, tags=["Provincia"], prefix="/provincias")


