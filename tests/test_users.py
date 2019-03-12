from marqeta import Client
from marqeta.errors import MarqetaError

BASE_URL = "https://shared-sandbox-api.marqeta.com/v3/"
USER_NAME = "user53461547583930"
PASSWORD = "1bd69e17-b826-4799-8f3a-77261ac2abab"

data_create= {
        "first_name": "BlueRed",
        "last_name": "BirdRed",
        "token": "bluebird_tokenRed",
        "email": "bluebirdRed123@gmail.com",
        "password": "My_passw0rdR",
        "notes" : "added some notes",
        "identifications": [
        {
          "type": "SSN",
          "value": "4444"
        }
        ],
        "birth_date": "1991-01-01",
        "address1": "1234 Blake Street",
        "city": "Berkeley",
        "state": "CA",
        "country": "USA",
        "postal_code": "94702",
        "phone": "5101111111",
        "gender": "M",
        "uses_parent_account": False,
        "corporate_card_holder": False,
        "metadata": {
            "key1":"value1",
            "key2":"value2"
            }
       }

data_update = {

            "first_name": "BlueRUpdate",
            "last_name": "BirdRUpdate",
            "metadata": {"key2": None
                         }
              }

notes = {
      "token": "bluebird_tokenRed",
      "description": "some notes",
      "created_by": "asha",

    }

notes_update = {
       "description": "updated some notes",

}

transition_data = {
  "token": "bluebird_tokenRed",
  "status": "ACTIVE",
  "reason_code": "01",
  "channel": "API",
  "user_token": "bluebird_tokenRed"
}

lookup_data = {
    "ssn": "4444"
}

######## User cases testing ##########

client = Client(BASE_URL, USER_NAME,PASSWORD)

# checking for base cases of create, list, find, update, stream and look up

try:
    create_user = client.users.create()
    print("***User Created***", create_user)
except MarqetaError as error:
    print(error)

# returns list of all the users object & limit specifies the #pages
options = {
    'start_index': 0,
    'fields': 'token, email'
}

field_options = {
    'fields': 'email, token'
}

list_users = client.users.list(params=options, limit = 3)
print(len(list_users))
print("***list of users***", list_users)
#print("***User First Name***", list_users[0].first_name)
print("***list of users by specifying the field***",client.users.list(params = options, limit = 3))
print("***list of users sort_by email***", client.users.list(params = options,limit = 3))

#  Streaming user


def stream():
    count = 0
    user_list =[]
    for user in client.users.stream():
        if count == 4:
            break
        else:
            user_list.append(user)
            count += 1
    return user_list


print("****streaming user***", stream())

#find the user based on token

find = client.users.find('bluebird_token',params = field_options)
print("**find bluebird_token***",find)

print("**BlueBird_token Last Name***", find.email)

## Save the user information / update the user information

save = client.users.save('bluebird_tokenR', data_update)

print(save.first_name)

print(save.address1)

## User Look Up

print(client.users.look_up(lookup_data, params = options))

print("LOOOOKUPPP",client.users.look_up(lookup_data)[0].first_name)


# To check for Children, Notes and Transitions of Users

print("***SSN of a user****",client.users('bluebird_token').ssn())
print("****BlueBird Children****",client.users('bluebird_token').children.list())


# Notes

client.users("bluebird_tokenRed").notes.create(notes)
print("notes",client.users("bluebird_tokenRed").notes.list())
print(client.users("bluebird_tokenRed").notes.list()[0].created_by)

notes_updated = client.users("bluebird_tokenRed").notes.save("bluebird_tokenRed",notes_update)
print(notes_updated)
print(notes_updated.description)


print(client.users("bluebird_tokenRed").notes.list()[0].description)

##### Transitions #####

print("Transitions before",client.users("bluebird_tokenRed").transitions.list()[0].reason_code)

print(client.users("bluebird_tokenRed").transitions.create(transition_data))

trans = client.users("bluebird_tokenRed").transitions.find('bluebird_tokenRed')
print(trans.status)
