from marqeta import Client

BASE_URL = "https://shared-sandbox-api.marqeta.com/v3/"
USER_NAME = "user53461547583930"
PASSWORD = "1bd69e17-b826-4799-8f3a-77261ac2abab"

card_product_data = {
  "name": "My Card Product 01",
  "token": "my_cardproduct_10",
  "start_date": "2017-04-27",
  "config": {
    "poi" : {
      "ecommerce" : False,
      "atm" : False,
      "other": {
        "allow": True,
        "card_presence_required": False,
        "cardholder_presence_required": False
      }
    },
    "transaction_controls" : {
      "accepted_countries_token": "accept_us_only",
      "always_require_pin": False,
      "always_require_icc": False,
      "allow_gpa_auth": True,
      "require_card_not_present_card_security_code": False,
      "allow_mcc_group_authorization_controls": True,
      "allow_first_pin_set_via_financial_transaction": True,
      "ignore_card_suspended_state": False,
      "allow_network_load": False,
      "allow_network_load_card_activation": False,
      "allow_quasi_cash": False,
      "enable_partial_auth_approval": True
    },
    "fulfillment": {
      "shipping": {
        "return_address": {
          "address1": "123 Henry St",
          "address2": "Suite 101",
          "city": "Porterville",
          "state": "CA",
          "postal_code": "93257",
          "country": "USA",
          "phone": "831-555-5555",
          "first_name": "Saki",
          "middle_name": "R",
          "last_name": "Dogger"
        },
        "recipient_address": {
          "address1": "1000 Pacific Ave",
          "city": "Santa Lucia",
          "state": "WA",
          "postal_code": "00112",
          "country": "USA",
          "phone": "345-123-9876",
          "first_name": "Big",
          "last_name": "Bird"
        },
        "method": "FEDEX_EXPEDITED"
      },
      "payment_instrument": "PHYSICAL_MSR",
      "package_id": "0",
      "all_zero_card_security_code": False,
      "bin_prefix": "111111",
      "bulk_ship": False,
      "pan_length": "16",
      "fulfillment_provider": "PERFECTPLASTIC"
    },
    "selective_auth" : {
      "sa_mode" : 1,
      "enable_regex_search_chain" : False,
      "dmd_location_sensitivity" : 0
    },
    "card_life_cycle" : {
      "activate_upon_issue" : True,
      "expiration_offset": {
        "unit": "YEARS",
        "value": 10
      },
      "card_service_code" : 101,
      "update_expiration_upon_activation": False
    },
    "jit_funding": {
      "paymentcard_funding_source": {
        "enabled": True
      }
    }
  }
}

card_product_update_data = {
  "name": "My Card Product 10", }

cards_data = {
  "token": "mytestcard10",
  "user_token": "my_user_01",
  "fulfillment": {
    "card_personalization": {
      "text": {
          "name_line_1": {
            "value": "My card personalization line 1"
          },
          "name_line_2": {
            "value": "My card personalization line 2"
          }
      },
      "images": {
        "card": {
           "name": "my_card_logo.png",
           "thermal_color": "Black"
        },
        "carrier": {
          "name": "my_carrier_logo.png",
          "message_1": "My message"
        },
        "signature": {
          "name": "my_signature.png"
        },
        "carrier_return_window": {
          "name": "my_return_address_image.png"
        }
      }
    }
  },
  "card_product_token": "red_cardproduct",
  "metadata": {
    	"key1":"value1",
    	"key2":"value2"
  }
}

card_update_data = {
  "user_token": "my_user_03"
}

transition_data = {
    "token": "activate_10",
    "state": "ACTIVE",
    "reason": "I want to use this card, so activate it.",
    "reason_code": "00",
    "channel": "API",
    "card_token": "mytestcard10",
    }


client = Client(BASE_URL, USER_NAME,PASSWORD)

## cards

print("CardProduct List",client.card_products.list(limit = 4))

print("CardProduct Create",client.card_products.create(card_product_data))

print("CardProduct Find",client.card_products.find("my_cardproduct_10"))

print("CardProduct update",client.card_products.save("my_cardproduct_10", card_product_update_data).name)

print("Cards List",client.cards.list(4444))
print("Cards List for user",client.cards.list_for_user('my_user_01'))

print("Card Create",client.cards.create(cards_data))

print("Card Find",client.cards.find("mytestcard01"))

print("Find by Pan",client.cards.find_show_pan("mytestcard01"))
#print(client.cards.find_by_barcode("12345678943"))
# #print(client.cards.tokens_for_pan({
#     "pan": "5454545454545454"
# }))
print("Card cUpdate",client.cards.save("mytestcard10",data=card_update_data))

print("Card Transition create",client.cards('mytestcard01').transitions.create(transition_data))
print("Card Transition Find",client.cards('mytestcard10').transitions.find("activate_10"))
print("Card Transition List",client.cards('mytestcard01').transitions.list())

# client.cards.find_for_merchant(token)
# client.cards.find_for_merchant_show_pan(token)
# client.cards.create_for_merchant(token)
####### FUNDING SOURCE ############
print("************funding********")
ach_funding_data = {
  "token": "bigbird_fundingsource_token25",
  "business_token": "my_business_02",
  "routing_number": "121000358",
  "name_on_account": "Big Bird",
  "is_default_account": True,
  "account_number": "987654321",
  "account_type": "savings",
  "verification_notes": "These are my verification notes.",
  "verification_override": True
}


ach_funding_data_b = {
  "token": "bigbird_fundingsource_token15",
  "user_token": "bluebird_token",
  "routing_number": "121000358",
  "name_on_account": "Big Bird",
  "is_default_account": True,
  "account_number": "987654321",
  "account_type": "savings",
  "verification_notes": "These are my verification notes.",
  "verification_override": True
}
ach_update = {
"active": "false",
"verify_amount1": 0.48,
"verify_amount2": 0.11
}

payment_data = {
  "token": "paycard_fs4_11",
  "postal_code": "94608",
  "user_token": "blue_bird_token",

  "is_default_account": True,
  "exp_date": "0120",
  "account_number": "4112344112344113",
  "cvv_number": "123"
}

payment_update = {
  "is_default_account": True,
  "exp_date": "0120"
}

program_data = {
  "token": "my_programfundingsource_token10",
  "name": "my_programfundingsource_name",
  "active": True
}

program_update= {
    "name": "your_programfundingsource_name",
    "active": False
}

program_gateway_data = {
  "token": "my_pgfs_token10",
  "basic_auth_username": "my_username",
  "basic_auth_password": "My_20-character-min_password",
  "url": "https://my_secure_domain.com/my_gateway",
  "name": "my_pgfs_name"
}

program_gateway_update = {
  "active": False
}

address_data = {
    "token": "my_funding_source_address_biz_04_02",
    "city": "Berkeley",
    "state": "CA",
    "postal_code": "94705",
    "country": "USA",
    "phone": "5104444444",
    "business_token": "my_business_04",
    "first_name": "My",
    "last_name": "Biz",
    "address_1": "3333 Bogus Way"
  }

print("ACH Create",client.funding_sources.ach.create(ach_funding_data))
print("ACH Create",client.funding_sources.ach.create(ach_funding_data_b))
print("ACH find",client.funding_sources.ach.find("bigbird_fundingsource_token05"))
print("ACH Verfication",client.funding_sources.ach("bigbird_fundingsource_token05").verification_amounts())
#print("ACH Update",client.funding_sources.ach.save("bigbird_fundingsource_token10",ach_update))

#print("payment card create",client.funding_sources.payment_card.create(payment_data))
print("payment card find",client.funding_sources.payment_card.find("paycard_fs4_01"))
#print("payment card update",client.funding_sources.payment_card.save("bigbird_fundingsource_token10", payment_update))

print("program card create",client.funding_sources.program.create(program_data))
print("program card find",client.funding_sources.program.find("my_programfundingsource_token10"))
print("program card save",client.funding_sources.program.save("my_programfundingsource_token10",program_update))


print("program_gateway card create",client.funding_sources.program_gateway.create(program_gateway_data))
print("program_gateway card find",client.funding_sources.program_gateway.find("my_pgfs_token10"))
print("program_gateway card save",client.funding_sources.program_gateway.save("my_pgfs_token10",program_gateway_update))

#print("list_for_user card list",client.funding_sources.list_for_user("bluebird_token"))
print("list_for_business card list",client.funding_sources.list_for_business("my_business_02"))

#print("addresses card create",client.funding_sources.addresses.create(address_data))
# print("addresses card list",client.funding_sources.addresses.list_for_user("bluebird_token"))
# print("addresses card list",client.funding_sources.addresses.list_for_business("my_business_02"))
print("addresses card find",client.funding_sources.addresses.find("my_funding_source_address_biz_04_02"))

print("addresses card save",client.funding_sources.addresses.save("my_funding_source_address_biz_04_02", {
    "address_1": "333 Elm Street"
}))


####### GPA ORDERS ############

gpa_data = {
  "token": "my_gpaorder_13",
  "user_token": "my_user_01",
  "amount": "1000",
  "currency_code": "USD",
  "funding_source_token": "bigbird_fundingsource_token35"
}

gpa_unload_data = {
  "token": "my_unload_01",
  "original_order_token": "my_gpaorder_01",
  "amount": 500
}

#print("gpa create",client.gpa_orders.create(gpa_data))

print("gpa find",client.gpa_orders.find("my_gpaorder_01"))

print("gpa unload create",client.gpa_orders.unloads.create(gpa_unload_data))
print("gpa unload list",client.gpa_orders.unloads.list())
print("gpa unload find",client.gpa_orders.unloads.find("my_unload_01"))
