# SPOClient
A simple python Sharepoint Online client to query Sharepoint API

### Requirements
- Python > 3.6
- requests
- python-dotenv

### Getting started
install from github or clone 
`python -m pip install git+(git repo)`

You will need to have your Sharepoint app client_id and client_secret

[For more info : click here for MSFT doc](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/register-sharepoint-add-ins)

create a .env file in the same folder with those variables :
```
SHAREPOINT_CLIENTID="12345yourclientid12345"
SHAREPOINT_SECRET="12345yourclientsecret12345"
SHAREPOINT_DOMAIN="https://{{yourtenant}}.sharepoint.com/sites/{{YourSharepointSite}}"
```
Then you can use the client this way:

```
from SPOClient import SPOClient
s = SPOClient()
# to query all the items Title and Id
endpoint = "/lists/getbytitle('MyList')/items"
select = 'Title,Id'
r = s.send_request(endpoint, select=select)
for i in r['d']['results']:
    print(i['Id'], i['Title'])
```
For now, only Put and Get methods are implemented

For more information on api endpoints:

[https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints)

Enjoy!