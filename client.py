import os
import requests

from auth import SPOAuth
from dotenv import load_dotenv

# Initializing environment variables
load_dotenv()
URL = os.getenv("SHAREPOINT_DOMAIN")
CLIENT_ID = os.getenv("SHAREPOINT_CLIENTID")
CLIENT_SECRET = os.getenv("SHAREPOINT_SECRET")


class SharepointClient:
    def __init__(self, url=URL, client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth = SPOAuth(self.url, self.client_id, self.client_secret)

    def send_request(self, endpoint, filters, select, post=False):
        headers = self._get_headers()
        if endpoint[0] == '/':
            endpoint = endpoint[1:]
        url = '/'.join([self.url, '_api/web', endpoint])
        payload = {'$filter': filters, '$select': select}
        if post:
            return requests.post(url=url, headers=headers, params=payload)
        return requests.get(url=url, headers=headers, params=payload)

    def _get_headers(self):
        type_value = 'application/json;odata=verbose'
        return {
            "Accept": type_value,
            "Content-Type": type_value,
            "Authorization": f'Bearer {self.auth.token}'
            }
