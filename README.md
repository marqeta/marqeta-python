**Marqeta Python SDK** 

Marqeta python SDK is a lightweight SDK wrapper around the Marqeta API.

Requirements:
    Marqeta Account
    Python >= 2.7 or >=3.6
    Pyhton requests module >= 2.0.0
    

Installation:

$ pip install marqeta


Initial setup:

from marqeta import Client
 
base_url = "https://shared-sandbox-api.marqeta.com"
application_token = "user42291540313074"
access_token = "xxx"
 
client = Client(base_url, application_token, access_token)


Making requests:

options = {
     
    # Paging
    "count": 5,
    "start_index": 0,
     
    # Sorting
    "sort_by": "-lastModifiedTime",
 
    # Filtering and expansion
    "fields": ["field_1", "field_2"],
    "expand": "user"
}
client.get("cards", params=options)

body = {
    # Consult API reference
}

client.post("cards", params=body)

body = {
    # Consult API reference
}

client.put("cards", params=body)
