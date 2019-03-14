from marqeta import Client
from marqeta.errors import MarqetaError

BASE_URL = "https://shared-sandbox-api.marqeta.com/v3/"
USER_NAME = "user53971547770644"
PASSWORD = "911cfe20-9987-4ec7-ac24-c2ce554dacc9"

data_create= {
  "token": "my_business_25",
  "metadata": {
  	"my_name_1": "my_value_1",
  	"my_name_2": "my_value_2"
  },
  "notes": "My  notes",
  "password": "My_passw0rd",
  "phone": "1234567890",
  "website": "https://my_business_02.com",
  "history": "My_business_history",
  "incorporation": {
    "is_public": True,
    "stock_symbol": "MB",
    "state_of_incorporation": "CA",
    "name_registered_under": "First Middle Last",
    "address_registered_under": {
      "address1": "123 B street",
      "city": "My_city",
      "state": "CA",
      "postal_code": "94711",
      "country": "USA"
    },
    "incorporation_type": "LLC"
  },
  "ip_address": "67.120.28.118",
  "business_name_legal": "My_legal_business_name",
  "business_name_dba": "My_fictitious_business_name",
  "office_location": {
    "address1": "123 A street",
    "address2": "Suite 123",
    "city": "My_city",
    "state": "CA",
    "postal_code": "94711",
    "country": "USA"
  },
  "in_current_location_since": "2010-04-15",
  "date_established": "2010-04-15",
  "general_business_description": "My_business_description",
  "business_type": "My_business_type",
  "international_office_locations": "Athens, Greece; Buenos Aires, Argentina",
  "identifications": [
    {
      "type": "BUSINESS_TAX_ID",
      "value": "123456789"
    }
  ],
  "duns_number": "123456789",
  "primary_contact": {
    "title": "Dr",
    "department": "My_department",
    "phone": "1234567890",
    "extension": "11",
    "fax": "1234567890",
    "email": "dr_me@my_business.com",
    "full_name": "First Middle Last",
    "mobile": "1234567890"
  },
  "proprietor_or_officer": {
    "title": "Dr",
    "dob": "1954-03-07",
    "phone": "1234567890",
    "email": "dr_me@my_business.com",
    "first_name": "First",
    "middle_name": "Middle",
    "last_name": "Last",
    "alternative_names": "My alternative name",
    "home": {
      "address1": "123 B street",
      "address2": "Apt A",
      "city": "My_city",
      "state": "CA",
      "postal_code": "94711",
      "country": "USA"
    }
  }
 }

data_update = {
  "phone": "9876543210"
}

notes = {
      "token": "my_business_02",
      "description": "some notes",
      "created_by": "asha",

    }

notes_update = {

       "description": "updated some notes",

}

transition_data = {
  "token": "activate_25",
  "business_token": "my_business_02",
  "status": "ACTIVE",
  "reason_code": "00",
  "reason": "Activating business",
  "channel": "API"
}

lookup_data = {
  "dda" : "0000212992320"
}

######## Businesses Endpoint testing ##########

client = Client(BASE_URL, USER_NAME,PASSWORD)

# checking for base cases of create, list, find, update, stream and look up

try:
    create_user = client.businesses.create()
    print("***Business Created***", create_user)
except MarqetaError as error:
    print(error)

# returns list of all the users object & limit specifies the #pages
options = {
    'start_index': 0,
    'fields': 'token'
}

field_options = {
    'fields': 'token'
}

list_users = client.businesses.list(params=options, limit = 3)
print("***list of businesses***", list_users)
print("***list of users by specifying the field***", client.businesses.list(params = options, limit = 3))
print("***list of users sort_by email***", client.businesses.list(params = options, limit = 3))

#  Streaming user


def stream():
    count = 0
    user_list =[]
    for user in client.businesses.stream():
        if count == 4:
            break
        else:
            user_list.append(user)
            count += 1
    return user_list


print("****streaming user***", stream())

#find the user based on token

find = client.businesses.find('my_business_02', params = field_options)
print("**find bluebird_token***",find)

print("**BlueBird_token Last Name***", find.token)

## Save the user information / update the user information

save = client.businesses.save('my_business_02', data_update)

print(save.phone)

## Business Look Up

#print(client.businesses.look_up(lookup_data, params = options))

#print("LOOOOKUPPP", client.businesses.look_up(lookup_data)[0])


# To check for Children, Notes and Transitions of Users

print("***SSN of a Business****", client.businesses('my_business_02').ssn())
print("****Business Children****", client.businesses('my_business_02').children.list())


# Notes

client.businesses("my_business_02").notes.create(notes)
print("notes", client.businesses("my_business_02").notes.list())
print(client.businesses("my_business_02").notes.list()[0])

notes_updated = client.businesses("my_business_02").notes.save("my_business_02", notes_update)
print(notes_updated)
print(notes_updated.description)


print(client.businesses("my_business_02").notes.list()[1].description)

##### Transitions #####

print("Transitions before", client.businesses("my_business_02").transitions.list())

print(client.businesses("my_business_02").transitions.create(transition_data))

trans = client.businesses("my_business_02").transitions.find('activate_25')
print(trans.status)

