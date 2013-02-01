import requests

class RemoteLoader(object):
    url = None

    def __init__(self, url):
        super(RemoteLoader, self).__init__()
        self.url = url

    def load(self):
        resp = requests.get(self.url)
        if resp.status != 200:
            raise Exception("Provided URL doesn't exist: %s", self.url)
        return resp.text