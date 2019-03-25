import os

from marqeta import Client


BASE_URL = "https://shared-sandbox-api.marqeta.com/v3/"
USER_NAME = "user53971547770644"
PASSWORD = "911cfe20-9987-4ec7-ac24-c2ce554dacc9"
client = Client(BASE_URL, USER_NAME, PASSWORD)

# card_product_options = {
#     "name": "Card Create Product",
#     "start_date": "2019-02-01",
#     "config": {
#         "fulfillment": {
#             "payment_instrument": "VIRTUAL_PAN"
#         }
#     }
# }
# card_product = client.card_products.create(card_product_options)
#
# user = client.users.create({})
#
# card_request = {
#     "card_product_token": card_product.token,
#     "user_token": user.token
# }
#
# card = client.cards.create(card_request)
#
# card_update_request = {
#     "metadata": {
#         "prop1": "Red nose"
#     }
# }
#
# client.cards.save(data= card_update_request)
#

card_product_options = {
    "name": "Card Create Product",
    "start_date": "2019-02-01",
    "config": {
        "fulfillment": {
            "payment_instrument": "VIRTUAL_PAN"
        }
    }
}
card_product = client.card_products.create(card_product_options)

user = client.users.create({})

card_request = {
    "card_product_token": card_product.token,
    "user_token": user.token
}

card_to_find = client.cards.create(card_request)

card_found = client.cards.find_show_pan(card_to_find.token)

print(card_found.pan)

tokens = client.cards.tokens_for_pan(card_found.pan)

print(tokens)