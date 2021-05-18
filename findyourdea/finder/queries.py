import os
import json
from .models  import DEA
di_path = os.path.realpath(__file__)[0:-10]



def get_data():
    with open(f"{di_path}deas.json", encoding="utf8") as file:
        return json.load(file)

data = get_data()["data"]

def insert_into(dataset):
    for dea in dataset:
        codigo_dea = dea["codigo_dea"]
        direccion_ubicacion = dea["direccion_ubicacion"]
        direccion_via_nombre = dea["direccion_via_nombre"]
        direccion_portal_numero = dea["direccion_portal_numero"]
        horario_acceso = dea["horario_acceso"]
        x_utm = dea["direccion_coordenada_x"]
        y_utm = dea["direccion_coordenada_y"]

        DEA.objects.create(
            codigo_dea = codigo_dea,
            direccion_ubicacion = direccion_ubicacion,
            direccion_via_nombre = direccion_via_nombre,
            direccion_portal_numero = direccion_portal_numero,
            horario_acceso = horario_acceso,
            x_utm = x_utm,
            y_utm = y_utm
        )