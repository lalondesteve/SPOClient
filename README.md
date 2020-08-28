# SPOClient
A simple python Sharepoint Online client to query Sharepoint API

### Requirements
- Python > 3.6
- requests
- python-dotenv

### Getting started
to install, clone the repo or install via pip:

`python -m pip install git+https://github.com/lalondesteve/SPOClient.git`


You will need to have your Sharepoint app client_id and client_secret

[For more info : click here for MSFT doc](https://docs.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs)

If you're not a global admin but the owner of a site, you will need to edit the urls in the step by step documentation to point to your site instead of the tenant, e.g.

`https://{{yourtenant}}.sharepoint.com/sites/{{yoursite}}`

And use the following xml for permission:
[MSFT Add-in Permission doc](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/add-in-permissions-in-sharepoint)

```
<AppPermissionRequests AllowAppOnlyPolicy="true">  
   <AppPermissionRequest Scope="http://sharepoint/content/sitecollection" 
    Right="FullControl" />
</AppPermissionRequests>
```
[permission cheat sheet](https://medium.com/ng-sp/sharepoint-add-in-permission-xml-cheat-sheet-64b87d8d7600)

create a .env file in the root folder with those variables :

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