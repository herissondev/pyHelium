import requests

class Hotspot():

        def __init__(self, data):

                self.name = data['name']
                self.address = data['address']
                self.lng = data['lng']
                self.lat = data['lat']
                self.timestamp_added = data['timestamp_added']
                self.status = data['status']
                self.reward_scale = data['reward_scale']
                self.payer = data['payer']
                self.owner = data['owner']
                self.nonce = data['nonce']
                self.mode = data['mode']
                self.location_hex = data['location_hex']
                self.location = data['location']
                self.last_poc_challenge = data['last_poc_challenge']
                self.last_change_block = data['last_change_block']
                self.geocode = data['geocode']
                self.gain = data['gain']
                self.elevation = data['elevation']
                self.block_added = data['block_added']


        def get_witnesses(self):

                '''Retrieves the list of witnesses for a given hotspot over about the last 5 days of blocks.'''

                self.witnesses = requests.get(f'https://api.helium.io/v1/hotspots/{self.address}/witnesses').json()['data']
                return self.witnesses

        def get_witnessed(self):

                '''Retrieves the list of hotspots the given hotspot witnessed over the last 5 days.'''

                self.witnessed = requests.get(f'https://api.helium.io/v1/hotspots/{self.address}/witnessed').json()['data']
                return self.witnessed

        def get_hotspot_activity(self):

                '''Lists all blockchain transactions that the given hotspot was involved in.'''

                self.activity = requests.get(f'https://api.helium.io/v1/hotspots/{self.address}/activity').json()['data']

                return self.activity