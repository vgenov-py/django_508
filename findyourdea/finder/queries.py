import os
import json
from .models  import DEA
import utm
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

class Dea:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_distance(self, user_x, user_y):
        result = ((user_x - self.x)**2 + (user_y - self.y)**2)**0.5 
        return result 
#44776165

def nearest_dea(user_lat, user_long, dataset):
    user_xy = utm.from_latlon(user_lat, user_long)
    first_dea = list(dataset)[0]
    result = first_dea
    first_object = Dea(first_dea.x_utm, first_dea.y_utm)
    distance_to_beat = first_object.calculate_distance(user_xy[0], user_xy[1])

    for dea in dataset:
        dea_object = Dea(dea.x_utm, dea.y_utm)
        distance = dea_object.calculate_distance(user_xy[0], user_xy[1])
        if distance <= distance_to_beat:
            result = dea
            distance_to_beat = distance
        else:
            continue
    print(result.y_utm)

    dea_latlng = utm.to_latlon(result.x_utm,result.y_utm, 30, "N")
    url = f"https://www.google.com/maps/dir/{user_lat},{user_long}/{dea_latlng[0]},{dea_latlng[1]} "
    return result, url