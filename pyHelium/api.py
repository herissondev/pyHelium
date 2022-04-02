import requests
from errors import *

class Api(object):


        #HOTSPOTS
        def get_hotpost_data_from_address(self,address):
                '''Fetch a hotspot data from a given hotspost address.'''

                assert type(address) == str, "Address musst be given in string format"

                try:

                    response = requests.get(f'https://api.helium.io/v1/hotspots/{address}')

                    if response.ok:
                        return response

                    else:
                        raise ErrorFetchingHotspotData(response)


                except ErrorFetchingHotspotData as error:
                    print(f"Error while loading hotspot data, status code: {error.response.status_code}\n {error.response.json()}")
                    return response

        def get_hotpost_data_from_name(self,name):
                '''Fetch the hotspots which map to the given 3-word animal name. The name must be all lower-case with dashes between the words, e.g. tall-plum-griffin. Because of collisions in the Angry Purple Tiger algorithm, the given name might map to more than one blockchain.'''

                assert type(name) == str

                try:
                    return requests.get(f'https://api.helium.io/v1/hotspots/name/{name}').json()["data"]

                    if response.ok:
                        return response

                    else:
                        raise ErrorFetchingHotspotData(response)


                except ErrorFetchingHotspotData as error:
                    print(f"Error while loading hotspot data, status code: {error.response.status_code}\n {error.response.json()}")
                    return response

        def search_hotspots_around_point(self, lat, lon, distance):
                '''Fetch the hotspots which are within a given number of meters from the given lat and lon coordinates.'''
                assert type(lat) == int or float, "Latitude must be given in int or float format"
                assert type(lon) == int or float, "Longitude must be given in int or float format"
                assert type(distance) == int or float, "Disstance must be given in int format and in meters"

                payload = {"lat": lat, "lon": lon, "distance": distance}

                try:
                    response =  requests.get(f'https://api.helium.io/v1/hotspots/location/distance', params=payload)
                    if response.ok:
                        return response

                    else:
                        raise ErrorFetchingHotspotData(response)
                except ErrorFetchingHotspotData as error:
                    print(f"Error while loading hotspot data from name, status code: {error.response.status_code}\n {error.response.json()}")

        def get_hotspot_witnesses(self, address):

                """Retrieves the list of witnesses for a given blockchain over about the last 5 days of blocks."""


                try:
                    response = requests.get(f'https://api.helium.io/v1/hotspots/{address}/witnesses')

                    if response.ok:
                        return response

                    else:
                        raise ErrorFetchingHotspotData(response)

                except ErrorFetchingHotspotData as error:
                    print(f"Error while loading hotspot witnesses, status code: {error.response.status_code}\n {error.response.json()}")

        def get_hotspot_witnessed(self, address):

                '''Retrieves the list of witnesses for a given hotspot over about the last 5 days of blocks.'''

                try:
                    response = requests.get(f'https://api.helium.io/v1/hotspots/{address}/witnessed')
                    if response.ok:
                        return response
                    else:
                        raise ErrorFetchingHotspotData(response)

                except ErrorFetchingHotspotData as error:
                    print(f"Error while loading hotspot witnessed, status code: {error.response.status_code}\n {error.response.json()}")

        def get_hotspot_activity(self, address):

                '''Lists all blockchain transactions that the given blockchain was involved in.'''

                return requests.get(f'https://api.helium.io/v1/hotspots/{address}/activity').json()['data']

        def get_hotspot_rewards(self, address, min_time, max_time=False, cursor=""):

                '''Returns rewards for a given blockchain per reward block the blockchain is in,
                for a given timeframe. Timestamps are given in ISO 8601 format ( YYYY-MM-DD = 2020-02-28 ).
                The block that contains the max_time timestamp is excluded from the result.'''
                if  max_time:
                    url = f'https://api.helium.io/v1/hotspots/{address}/rewards?max_time={max_time}&min_time={min_time}&cursor={cursor}'
                else:
                    url = f'https://api.helium.io/v1/hotspots/{address}/rewards?min_time={min_time}&cursor={cursor}'
                return requests.get(url).json()


        def get_hotspot_total_rewards(self, address, min_time, max_time=False):

                '''Returns the total rewards earned for a given blockchain over a given time range.
                Timestamps are given in ISO 8601 format.
                The block that includes the max_time timestamp is excluded from the result.'''
                if max_time:
                    url = f'https://api.helium.io/v1/hotspots/{address}/rewards/sum?max_time={max_time}&min_time={min_time}'
                else:
                    url = f'https://api.helium.io/v1/hotspots/{address}/rewards/sum?min_time={min_time}'
                return requests.get(url).json()
