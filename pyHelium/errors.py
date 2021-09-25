class  ErrorFetchingHotspotData(Exception):
    """docstring for ErrorFetchingHotspotData."""

    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code

    def __str__(self):
        return(repr(self))
