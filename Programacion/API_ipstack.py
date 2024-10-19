from ipstack import GeoLookup
geo_lookup = GeoLookup("598c13a2ee867061d090b46a43efc115")
location = geo_lookup.get_location("vodafone.es")
print(location)
print(location["location"]["languages"][0]["name"])
print(location["city"])