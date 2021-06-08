import requests

class Solr:
    def __init__(self, host, port, core):
        self._host = host
        self._port = port
        self._core = core

    def _buildURL(self, handler):
        return f"http://{self._host}:{self._port}/solr/{self._core}{handler}"

    def select(self, params):
        url = self._buildURL("/select")
        res = requests.get(url, params=params)
        return res.json()