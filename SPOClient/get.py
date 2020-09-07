
class List:
    def __init__(self, client):
        self.client = client
        self._title = None
        self._item = None
        self.endpoint = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.endpoint = f"/lists/getbytitle('{self._title}')"

    @property
    def items(self):
        try:
            endpoint = self.endpoint + "/items"
            select = 'Title,Id'
        except Exception:
            raise
        return self.client.send_request(endpoint, select=select)

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item_id=None, item_name=None, filters=None):
        pass
