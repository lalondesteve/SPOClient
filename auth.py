import requests


class SPOAuth:
    def __init__(self, url, client_id, client_secret):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.principal = "00000003-0000-0ff1-ce00-000000000000"
        self.realm = self.get_realm()
        self.resource = self.get_resource()
        self._token = self.auth()

    @property
    def token(self):
        return self._token['access_token']

    def get_realm(self):
        response = requests.head(url=self.url, headers={'Authorization': 'Bearer'})
        key = 'WWW-Authenticate'
        if key in response.headers:
            values = response.headers[key].split(',')
            for value in values:
                if 'realm' in value:
                    try:
                        _, realm = value.split('=')
                    except Exception as e:
                        raise e
                    else:
                        return realm.replace('"', '')
        return None

    def get_resource(self):
        hostname = self.url.split('/')[2]
        return f'{self.principal}/{hostname}@{self.realm}'

    def get_request(self):
        return {
            'grant_type': 'client_credentials',
            'client_id': f'{self.client_id}@{self.realm}',
            'client_secret': f'{self.client_secret}',
            'resource': f'{self.resource}'
            }

    def auth(self):
        auth_url = f'https://accounts.accesscontrol.windows.net/{self.realm}/tokens/OAuth/2'
        req = self.get_request()
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=auth_url,headers=headers,data=req)
        return response.json()
