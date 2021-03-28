import requests
import tweepy


class Auth(requests.auth.AuthBase):

    def __init__(self, bearer):
        self._bearer = bearer

    def __call__(self, r: requests.Request):
        r.headers['Authorization'] = "Bearer {}".format(self._bearer)

    def apply_auth(self):
        return tweepy.auth.OAuth2Bearer(self._bearer)

