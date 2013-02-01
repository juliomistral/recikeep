import requests
from requests import ConnectionError

from recikeep.lib.loader import RemoteLoader

from flexmock import flexmock
from . import TestCase


class RemoteLoaderTest(TestCase):
    """RemoteLoader:  Loads text from a remote URL"""

    def test_should_get_the_recipe_at_the_url(self):
        """Should get the recipe at the initialized URL"""
        url = "some url"
        fake_resp = flexmock(status=200, text='some text')
        flexmock(requests).should_receive("get").with_args(url).and_return(fake_resp)

        loader = RemoteLoader(url)
        text = loader.load()

    def test_should_raise_exception_when_recipe_not_found(self):
        """Should raise an exception when the recipe can't be found"""
        fake_resp = flexmock(status=404)
        flexmock(requests).should_receive("get").with_args("some url").and_return(fake_resp)

        loader = RemoteLoader("some url")
        self.assertRaises(Exception, loader.load)

        """"Should raise an exception when the server can't be found"""
    def test_should_raise_exception_when_server_not_found(self):
        flexmock(requests).should_receive("get").with_args("some url").and_raise(ConnectionError)

        loader = RemoteLoader("some url")
        self.assertRaises(Exception, loader.load)

