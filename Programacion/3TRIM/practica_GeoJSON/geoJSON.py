import json

# Carga el archivo JSON original
with open('2024_FEBRUARY.json') as f:
    data = json.load(f)

# Crea un archivo GeoJSON vacío
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Iterar sobre cada elemento en el array timelineObjects
for obj in data['timelineObjects']:
    # Extrae la información relevante
    if obj.get('activitySegment'):
        startLoc = obj['activitySegment']['startLocation']
        duration = obj['activitySegment']['duration']
        
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [startLoc['longitudeE7'] / 1e7, startLoc['latitudeE7'] / 1e7]
            },
            "properties": {
                "duration": duration,
            }
        }
        # Agrega el objeto Feature al array features
        geojson['features'].append(feature)
        
    elif obj.get('placeVisit'):
        subObj = obj.get('placeVisit')
        # Iterar sobre cada elemento en el diccionario placaVisits
        for clave in subObj:
            if clave == 'location':
                location = subObj['location']
                duration = subObj['duration']
                
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [location['longitudeE7'] / 1e7, location['latitudeE7'] / 1e7]
                    },
                    "properties": {
                        "duration": duration,
                    }
                }
                # Agrega el objeto Feature al array features
                geojson['features'].append(feature)
            elif clave == 'otherCandidateLocations':
                subSubObj = subObj.get('otherCandidateLocations')
                # Iterar sobre cada elemento en el array otherCandidateLocations
                for member in subSubObj:
                    # No todos los elementos tienen el campo nombre, por lo que hacemos un try-except para evitar errores
                    try:
                        feature = {
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [member['longitudeE7'] / 1e7, member['latitudeE7'] / 1e7]
                            },
                            "properties": {
                                "address": member['address'],
                                "name": member['name'],
                            }
                        }
                        # Agrega el objeto Feature al array features
                        geojson['features'].append(feature)
                    except KeyError:
                        feature = {
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [member['longitudeE7'] / 1e7, member['latitudeE7'] / 1e7]
                            },
                            "properties": {
                                "address": member['address'],
                            }
                        }
                        # Agrega el objeto Feature al array features
                        geojson['features'].append(feature)
            
            elif clave == 'childVisits':
                subSubObj = subObj['childVisits']
                # Iterar sobre cada elemento en el array childVisits
                for member in subSubObj[0]:
                    if member == 'location':
                        location = subSubObj[0]['location']
                        duration = subSubObj[0]['duration']
                        
                        feature = {
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [location['longitudeE7'] / 1e7, location['latitudeE7'] / 1e7]
                            },
                            "properties": {
                                "duration": duration,
                            }
                        }
                        # Agrega el objeto Feature al array features
                        geojson['features'].append(feature)
                        
                    elif member == 'otherCandidateLocations':
                        subSubSubObj = subSubObj[0].get('otherCandidateLocations')
                        # Iterar sobre cada elemento en el array otherCandidateLocations
                        for subMember in subSubSubObj:
                            # No todos los elementos tienen el campo nombre, por lo que hacemos un try-except para evitar errores
                            try:
                                feature = {
                                    "type": "Feature",
                                    "geometry": {
                                        "type": "Point",
                                        "coordinates": [subMember['longitudeE7'] / 1e7, subMember['latitudeE7'] / 1e7]
                                    },
                                    "properties": {
                                        "address": subMember['address'],
                                        "name": subMember['name'],
                                    }
                                }
                                # Agrega el objeto Feature al array features
                                geojson['features'].append(feature)
                                
                            except KeyError:
                                feature = {
                                    "type": "Feature",
                                    "geometry": {
                                        "type": "Point",
                                        "coordinates": [subMember['longitudeE7'] / 1e7, subMember['latitudeE7'] / 1e7]
                                    },
                                    "properties": {
                                        "address": subMember['address'],
                                    }
                                }
                                # Agrega el objeto Feature al array features
                                geojson['features'].append(feature)
                    

# Guarda el archivo GeoJSON
with open('output.geojson', 'w', encoding="utf-8") as f:
    json.dump(geojson, f)


































# import json

# # Lee el archivo JSON
# with open('2024_FEBRUARY.json', 'r') as f:
#     data = json.load(f)

# # Crea un nuevo archivo GeoJSON
# with open('2024_FEBRURY.geojson', 'w') as f:
#     # Agrega la estructura básica del formato GeoJSON
#     f.write('{\n')
#     f.write('"type": "FeatureCollection",\n')
#     f.write('"features": [\n')

#     # Agrega los datos relevantes al archivo GeoJSON
#     f.write('{\n')
#     f.write('"type": "Feature",\n')
#     f.write('"geometry": {\n')
#     f.write(f'"type": "Point",\n')
#     f.write(f'"coordinates": [{data["timelineObjects"][0]["activitySegment"]["startLocation"]['longitudeE7']}, {data["timelineObjects"][0]["activitySegment"]["startLocation"]['latitudeE7']}]\n')
#     f.write('},\n')
#     f.write('"properties": {\n')
#     # f.write(f'"name": "{data['name']}",\n')
#     # f.write(f'"date": "{data['date']}",\n')
#     f.write('}\n')
#     f.write('}\n')

#     # Cierra la sección de features
#     f.write(']\n')
#     f.write('}\n')


