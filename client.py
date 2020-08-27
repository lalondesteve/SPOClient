import os
import requests

from auth import SPOAuth
from dotenv import load_dotenv

# Initializing environment variables
load_dotenv()
URL = os.getenv("SHAREPOINT_DOMAIN")
CLIENT_ID = os.getenv("SHAREPOINT_CLIENTID")
CLIENT_SECRET = os.getenv("SHAREPOINT_SECRET")


class SPOClient:
    """
        Sharepoint Online App Authentication and requests sender
    """
    def __init__(self, url=URL, client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
        """
        Interface to accelerate requests to a sharepoint online api
        to get client_id and client_secret, consult:
        https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/register-sharepoint-add-ins

        :param url: string complete url to your site https://contoso.sharepiont.com/sites/ContosoSite
        :param client_id: string of authorized sharepoint app
        :param client_secret: string
        """
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth = SPOAuth(self.url, self.client_id, self.client_secret)

    def send_request(self, endpoint, filters=None, select=None, post=False):
        """
        Builds a request and returns response.json

        :param endpoint: string e.g. '/lists/getbytitle('MyList')/items
        :param filters: string ODATA filter value
        :param select: string ODATA select value
        :param post: bool, whether the request is a post or get
        :return: dict representation of json value
        """
        headers = self._get_headers()
        if endpoint[0] == '/':
            endpoint = endpoint[1:]
        url = '/'.join([self.url, '_api/web', endpoint])
        payload = {}
        if filters:
            payload['$filter'] = filters
        if select:
            payload['$select'] = select
        if post:
            return requests.post(url=url, headers=headers, params=payload).json()
        return requests.get(url=url, headers=headers, params=payload).json()

    def _get_headers(self):
        type_value = 'application/json;odata=verbose'
        return {
            "Accept": type_value,
            "Content-Type": type_value,
            "Authorization": f'Bearer {self.auth.token}'
            }
