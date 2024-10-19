# ******************************************
# Ejercicio 3 del Examen del 3er Trimestre
# Samuel Plaza Sáez
# ******************************************

import csv
import json

with open("paises_2016_geom_10.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    geojson = {
    "type": "FeatureCollection",
    "features": []
    }
    
    for row in reader:
        if row[3].isalpha():
            pass
        else:
            pais = row[1]
            longitud = (row[3])
            latitud = (row[4])
            
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [longitud, latitud]
                },
                "properties": {
                    "name" : pais
                }
            }
            
            geojson['features'].append(feature)
        
with open('output.geojson', 'w', encoding="utf-8") as f:
    json.dump(geojson, f)
