import SPOClient


def update_list_item(client: SPOClient.Client, list_name: str, item_id: int, values: dict) -> dict:
    endpoint = f"/list/getbytitle('{list_name}')/items({item_id})/ValidateUpdateListItem"
    form_values = _get_form_values(values)
    return client.send_request(endpoint, data=form_values, post=True)


def create_list_item(client: SPOClient.Client, list_name: str, values: dict) -> dict:
    endpoint = f"/list/getbytitle('{list_name}')/items/AddValidateUpdateItem"
    form_values = _get_form_values(values)
    return client.send_request(endpoint, data=form_values, post=True)


def _get_form_values(values: dict) -> dict:
    return {"formValues": [{"FieldName": x, "FieldValue": values[x]} for x in values]}


def get_items(client: SPOClient.Client, list_name: str,
              column_values: dict = None, select_attributes: list = None) -> dict:
    """
    return all items in list, unless filter or select are specified

    :param client:
    :param list_name:
    :param column_values: dict of column_id : value to filter the list
    :param select_attributes: column_id of items to return
    :return:
    """
    filt = select = None
    endpoint = f"/list/getbytitle('{list_name}')/items"
    if column_values:
        filt = ' and '.join([f"{k} eq '{column_values[k]}'" for k in column_values])
    if select_attributes:
        select = ','.join(select_attributes)
    return client.send_request(endpoint, filters=filt, select=select)


def get_column_value(client: SPOClient.Client, list_name, item_id: int, column_id: str) -> dict:
    endpoint = f"/list/getbytitle('{list_name}')/items({item_id}"
    select = column_id
    return client.send_request(endpoint, select=select)
