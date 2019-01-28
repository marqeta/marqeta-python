from marqeta import Client
from marqeta.errors import MarqetaError

BASE_URL = "https://shared-sandbox-api.marqeta.com/v3/"
USER_NAME = "user53461547583930"
PASSWORD = "1bd69e17-b826-4799-8f3a-77261ac2abab"

card_product_token_data = data = {"start_date": "2017-01-01",
            "name": "Example Card Product",
            "config": {
                    "fulfillment": {"payment_instrument":"VIRTUAL_PAN"},
             "poi": {"ecommerce": True},
             "card_life_cycle": {"activate_upon_issue": True}
                      }
            }

funding_data = {"name": "Program Funding"}

user_data ={}

'''card_data ={
        "user_token": usertoken,
        "card_product_token": cardproducttoken

    }'''

client = Client(BASE_URL, USER_NAME,PASSWORD)


def simulation():
    try:
        # creating a card product and storing the card product token
        card_product_token = client.post("cardproducts", data=card_product_token_data)
        card_product_token = card_product_token[0]['token']
        print(card_product_token)

        # creating a user and storing user token
        user_token = client.post("users", data = user_data)
        user_token = user_token[0]['token']
        print(user_token)

        card_data = {"user_token": user_token,"card_product_token": card_product_token}
        # create a card
        card_token = client.post("cards", data = card_data)
        print(card_token)
        new_card_token = card_token[0]['token']
        print("Newcard:",new_card_token)
        card_pan = {'last_four' : card_token[0]["pan"]}

        print (card_token)

        # get method
        users = client.get("users")
        print(users)

        card = client.get("cards",card_pan)
        print(card)

        # Put Method

        card = client.put("cards/{}".format(new_card_token), data ={})
        print("card:",card)

    except MarqetaError as error:
        print(error)
        print(error.code)


simulation()
