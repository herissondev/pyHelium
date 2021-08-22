from api import Api

api = Api()
hotspot = api.get_hotpost_data_from_address("11CDbFUj3CkT2SCnFn7372f9EeNz88hb9deQaomV6xKyDFq6z1h")

print(hotspot.name)

hotspots_around = api.search_hotspots_around_point(hotspot.lat, hotspot.lng, 3000)
print(hotspot.get_witnessed())

for i in hotspots_around:
        print(i.name)