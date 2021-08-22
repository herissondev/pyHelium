import requests
from hotspot import Hotspot

class Api():

        def get_hotpost_data_from_address(self,address):
                '''Fetch a hotspot with a given address.'''
                #print(f'adresse: {address}')

                data = requests.get(f'https://api.helium.io/v1/hotspots/{address}').json()["data"]

                return Hotspot(data)

        def get_hotpost_data_from_name(self,name):
                '''Fetch the hotspots which map to the given 3-word animal name. The name must be all lower-case with dashes between the words, e.g. tall-plum-griffin. Because of collisions in the Angry Purple Tiger algorithm, the given name might map to more than one hotspot.'''

                return requests.get(f'https://api.helium.io/v1/hotspots/name/{name}').json()["data"]

        def search_hotspots_around_point(self, lat, lon, distance):
                '''Fetch the hotspots which are within a given number of meters from the given lat and lon coordinates.'''

                payload = {"lat": lat, "lon": lon, "distance": distance}
                data =  requests.get(f'https://api.helium.io/v1/hotspots/location/distance', params=payload).json()["data"]

                result = []
                for hotspot in data:
                        result.append(Hotspot(hotspot))
                return result


