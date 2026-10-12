import json
def load_config(path="config.json"): """Carga la configuracion del servicio desde un archivo JSON.""" 
	with open(path) as f:
		return json.load(f)
