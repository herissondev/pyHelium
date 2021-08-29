import requests

class Api(object):


        #HOTSPOTS
        def get_hotpost_data_from_address(self,address):
                '''Fetch a blockchain with a given address.'''
                #print(f'adresse: {address}')

                data = requests.get(f'https://api.helium.io/v1/hotspots/{address}').json()["data"]

                return data

        def get_hotpost_data_from_name(self,name):
                '''Fetch the hotspots which map to the given 3-word animal name. The name must be all lower-case with dashes between the words, e.g. tall-plum-griffin. Because of collisions in the Angry Purple Tiger algorithm, the given name might map to more than one blockchain.'''

                return requests.get(f'https://api.helium.io/v1/hotspots/name/{name}').json()["data"]

        def search_hotspots_around_point(self, lat, lon, distance):
                '''Fetch the hotspots which are within a given number of meters from the given lat and lon coordinates.'''

                payload = {"lat": lat, "lon": lon, "distance": distance}
                data =  requests.get(f'https://api.helium.io/v1/hotspots/location/distance', params=payload).json()["data"]

                result = []
                for hotspot in data:
                        result.append(hotspot)
                return result

        def get_hotspot_witnesses(self, address):

                '''Retrieves the list of witnesses for a given blockchain over about the last 5 days of blocks.'''

                return requests.get(f'https://api.helium.io/v1/hotspots/{address}/witnesses').json()['data']


        def get_hotspot_witnessed(self, address):

                '''Retrieves the list of hotspots the given blockchain witnessed over the last 5 days.'''

                return requests.get(f'https://api.helium.io/v1/hotspots/{address}/witnessed').json()['data']


        def get_hotspot_activity(self, address):

                '''Lists all blockchain transactions that the given blockchain was involved in.'''

                return requests.get(f'https://api.helium.io/v1/hotspots/{address}/activity').json()['data']

        def get_hotspot_rewards(self, address, max_time, min_time, cursor=""):

                '''Returns rewards for a given blockchain per reward block the blockchain is in,
                for a given timeframe. Timestamps are given in ISO 8601 format ( YYYY-MM-DD = 2020-02-28 ).
                The block that contains the max_time timestamp is excluded from the result.'''
                url = f'https://api.helium.io/v1/hotspots/{address}/rewards?max_time={max_time}&min_time={min_time}&cursor={cursor}'

                return requests.get(url).json()


        # def get_hotspot_total_rewards(self, address, max_time, min_time):
        #
        #         '''Returns the total rewards earned for a given blockchain over a given time range.
        #         Timestamps are given in ISO 8601 format.
        #         The block that includes the max_time timestamp is excluded from the result.'''
        #
        #         url = f'https://api.helium.io/v1/hotspots/{address}/rewards/sum?max_time={max_time}&min_time={min_time}'
        #         print(url)
        #         return requests.get(url).json()





