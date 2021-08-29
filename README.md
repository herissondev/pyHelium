# PyHelium
_PyHelium is a simple api wrapper to access Helium network's api._

### How to install ?

`pip install PyHelium`

**Important**: depending on your system, make sure to use `pip3` and `python3` instead.

###How to use ?
#####Simple example:
```python
import pyHelium

#this will return a Hotspot object
myHotspot = pyHelium.initiate_hotspot_from_address("11CDbFUj3CkT2SCnFn7372f9EeNz88hb9deQaomV6xKyDFq6z1h")

#we can then print informations about your hotspot:
print(myHotspot.name)
print(myHotspot.reward_scale)
print(myHotspot.status)

#it is also possible to fetch more data about your hotspot:
myHotspot.get_activity()
#and then print it
print(myHotspot.activity)

```

