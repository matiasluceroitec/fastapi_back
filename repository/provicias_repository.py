from db.db import db
from models.provincias import Provincias

def get_provincias():
	return  db.query(Provincias).all()

def get_provincia(id:int):
	return db.query(Provincias).filter(Provincias.id==id).first()
