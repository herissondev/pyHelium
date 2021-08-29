from pytest import fixture
from pyHelium import api as d
@fixture
def test_api():
    api = d.Api()
    response = api.get_hotpost_from_address("11CDbFUj3CkT2SCnFn7372f9EeNz88hb9deQaomV6xKyDFq6z1h")
    print(response.address)