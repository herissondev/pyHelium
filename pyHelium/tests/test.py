from pyHelium import Api

api = Api()
blockchain = api.get_hotpost_from_address("11CDbFUj3CkT2SCnFn7372f9EeNz88hb9deQaomV6xKyDFq6z1h")
#print(api.get_hotspot_rewards("112Dpsf9n742y8nqZb8GFvCCVrq2xrCgG4gPs4rfgghQBdaTj2jo", "2021-08-22", "2021-08-24"))

hotspots_around = api.search_hotspots_around_point(blockchain.lat, blockchain.lng, 15000)
# print(blockchain.get_witnessed())
#
for i in hotspots_around:
      print(i.status)

# print(len(hotspots_around))
