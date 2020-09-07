import os
import requests
import logging

from SPOClient.auth import SPOAuth
from dotenv import load_dotenv

# Initializing environment variables
load_dotenv()
URL = os.getenv("SHAREPOINT_DOMAIN")
CLIENT_ID = os.getenv("SHAREPOINT_CLIENTID")
CLIENT_SECRET = os.getenv("SHAREPOINT_SECRET")


class Client:
    """
        Sharepoint Online App Authentication and requests sender
    """
    logging.getLogger(f"{__name__}.spoclient")

    def __init__(self, url=URL, client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
        """
        Interface to request sharepoint online api via app authentication
        to get client_id and client_secret, consult:
        https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/register-sharepoint-add-ins

        :param url: string complete url to your site https://contoso.sharepiont.com/sites/ContosoSite
        :param client_id: string
        :param client_secret: string
        """
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth = SPOAuth(self.url, self.client_id, self.client_secret)
        self._type_value = 'application/json'

    def send_request(self, endpoint, data=None, filters=None, select=None, post=False) -> dict:
        """
        Builds a request and returns values as a dict

        :param data: dict of data to send as raw json
        :param endpoint: string e.g. '/lists/getbytitle('MyList')/items
        :param filters: string ODATA filter value
        :param select: string ODATA select value
        :param post: bool, whether the request is a post or get
        :return: dict representation of json value
        """
        headers = self.headers
        if endpoint[0] == '/':
            endpoint = endpoint[1:]
        url = '/'.join([self.url, '_api/web', endpoint])
        payload = {}
        if filters:
            payload['$filter'] = filters
        if select:
            payload['$select'] = select
        logging.debug(f'Send request to endpoint {endpoint}?{payload} with data: {data}')
        if post:
            return requests.post(url=url, headers=headers, params=payload, json=data).json()
        return requests.get(url=url, headers=headers, params=payload).json()

    @property
    def headers(self):
        return {
            "Accept":        self._type_value,
            "Content-Type":  self._type_value,
            "Authorization": f'Bearer {self.auth.token}'
        }

    @headers.setter
    def headers(self, value):
        if value == 'verbose':
            self._type_value = 'application/json;odata=verbose'
        elif value == 'normal':
            self._type_value = 'application/json'
        else:
            raise ValueError('Headers can only be verbose or normal')
