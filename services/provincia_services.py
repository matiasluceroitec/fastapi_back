from repository.provicias_repository import get_provincia, get_provincias


class Provincias_Services():

	def get_all():
		return get_provincias()

	def get_one(id:int):
		return get_provincia(id)

