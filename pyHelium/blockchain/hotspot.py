from ..api import Api


def initiate_hotspot_from_address(address):

        print(address)
        data = Api().get_hotpost_data_from_address(address)
        return Hotspot(data)

def initiate_hotspot_from_name(name):
        data = Api.get_hotpost_data_from_name(name)
        return Hotspot(data)

def initiate_hotspot_from_data(data):
        return Hotspot(data)


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
                self.witnesses = Api().get_hotspot_witnesses(self.address)
                return self.witnesses

        def get_witnessed(self):
                self.witnessed = Api().get_hotspot_witnessed(self.address)
                return  self.witnessed

        def get_activity(self):
                self.activity = Api().get_hotspot_activity(self.address)
                return  self.activity

        def get_rewards(self, max_time, min_time, cursor=""):
                data = Api().get_hotspot_rewards(self.address, max_time, min_time, cursor)["data"]
                self.rewards = data
                #self.rewards_cursor = data["cursor"]
                return self.rewards, self.rewards_cursor