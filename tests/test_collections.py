from marqeta import Client

BASE_URL = "https://shared-sandbox-api.marqeta.com/v3/"
USER_NAME = "user53461547583930"
PASSWORD = "1bd69e17-b826-4799-8f3a-77261ac2abab"

client = Client(BASE_URL, USER_NAME, PASSWORD)

#### Accepted Countries ####

countries_data ={
  "token": "string",
  "name": "India",
  "is_whitelist": False,
  "country_codes": [
    "724"
  ],
  "created_time": "2019-03-14T18:31:05.726Z",
  "last_modified_time": "2019-03-14T18:31:05.726Z"
}

countries_update = {
  "name": "Hindustan",
  "is_whitelist": False,
  "country_codes": [
    "724"
  ]
}

print(client.accepted_countries.list(limit =2))
print(client.accepted_countries.page())

print(client.accepted_countries.find("ec1c157a-0f8e-4b01-b10a-33c66b647d49"))
print(client.accepted_countries.create(countries_data))
print(client.accepted_countries.save("ec1c157a-0f8e-4b01-b10a-33c66b647d49",countries_update))

### Account Holder ####

account_data = {
  "token": "account_holder_group_25",
  "name": "Account Holder Group 25"
}

account_update = {
  "config": {
    "pre_kyc_controls": {
      "balance_max": 700
    }
  }
}

print((client.account_holder_groups.list(limit =3)))
print(('*****PAGE*****',client.account_holder_groups.page()))
print(client.account_holder_groups.find("account_holder_group_01"))
print(client.account_holder_groups.create(account_data))
print(client.account_holder_groups.save("account_holder_group_01", account_update))

#### AuthCOntrol ####

auth_data = {
  "merchant_scope": {
    "mid": "98765"
  },
  "association": {
    "user_token": "bigbird_token"
  },
  "token": "my_authcontrol",
  "name": "My Auth Control_test1"
}


auth_update = {
  "merchant_scope": {
    "mcc": "2345"
  }
}

print(client.auth_controls.list(limit =6))
print(client.auth_controls.find("06de4dbc-1f06-4b05-9e8a-aaed3d5970fe"))
#print(client.auth_controls.create(auth_data))
print(client.auth_controls.save("my_authcontrol", auth_update))

# ### Authcontrolls Exempt ###

auth_exmp_data = {
  "token": "my_exempt_token",
  "name": "my_exempt_mid",
  "association": {
    "card_product_token": "my_card_product"
  },
  "mid": "12345678901"
}

auth_exmp_update_data = {
  "token": "my_exempt_token",
  "name": "my_exempt_mid1233",
  "association": {
    "card_product_token": "my_card_product"
  },
  "mid": "12345678901"
}


print(client.auth_controls.exempt_mids.list())
#print(client.auth_controls.exempt_mids.find("my_exempt_token"))
#print(client.auth_controls.exempt_mids.create(auth_exmp_data))
#print(client.auth_controls.exempt_mids.save("my_exempt_token",auth_exmp_update_data ))


# #### Auto Reload ########
auto_reload_data = {
  "token": "my_user_01_autoreload_10",
  "active": False,
  "currency_code": "USD",
  "association": {
    "user_token": "my_user_01"
  },
  "funding_source_token": "my_program_funding_source_01",
  "order_scope": {
    "gpa": {
      "trigger_amount": 100,
      "reload_amount": 200
    }
  }
}

auto_reload_update = {
  "order_scope": {
    "gpa": {
      "trigger_amount": 250,
      "reload_amount": 500
    }
  }
}
print(client.auto_reloads.list(limit=3))
print(client.auto_reloads.find('my_user_01_autoreload_01'))
#print(client.auto_reloads.create(auto_reload_data))
print(client.auto_reloads.save('my_user_01_autoreload_01', auto_reload_update))


####### KYC #########

kyc_data = {
  "token": "my_kyc02",
  "user_token": "my_user_01",
  "manual_override": False
}

kyc_update = {

}
print(client.kyc.list_for_user('my_user_01'))
print(client.kyc.list_for_business('my_business_02'))
print(client.kyc.find('my_kyc01'))
print(client.kyc.create(kyc_data))
print(client.kyc.save('my_kyc01', kyc_update))

########  Balance  ########

print(client.balances.find_for_user_or_business('bluebird_token'))
print(client.balances.list_msas_for_user_or_business('my_business_02'))

#######  MSAORDER #########

msa_data = {

    "campaign_token": "my_campaign_01",
    "user_token": "my_user_01",
    "token": "my_msaorder_test_123",
    "currency_code": "USD",
    "purchase_amount": "100.00",
    "funding_source_token": "my_program_funding_source_01"
}

msa_update = {
    "active": False
}

msa_unload_data= {
  "token": "my_msaunload_12343",
  "amount": "3.00",
  "original_order_token": "my_msaorder_test_01"
}

print(client.msa_orders.find("my_msaorder_test_01"))
#print(client.msa_orders.create(msa_data))
print(client.msa_orders.save('my_msaorder_test_01',msa_update))

print(client.msa_orders.unloads.list())
print(client.msa_orders.unloads.find('my_msaunload_01'))
print(client.msa_orders.unloads.create(msa_unload_data))

#### OFFER ORDERS #######
offer_data= {
  "token": "my_offerorder_0100",
  "user_token": "my_user_01",
  "offer_token": "may_offer_100",
  "funding_source_token": "my_program_funding_source"
}


#print(client.offer_orders.find('may_offer'))
#print(client.offer_orders.create(offer_data))

##### COMMONMODES #########

command_data = {
    "token": "commando_mode_1_transition",
    "commando_mode_token": "commando_mode_1",
    "transition": {
     "commando_enabled": 'true',
     "reason": "Lost connection",
     "channel": "API",
     "user_name": "Bob"}
    }



print(client.commando_modes.list())
#print(client.commando_modes.find('commado_mode_1'))

#print(client.commando_modes('commado_mode_1').transitions.create(command_data))
#print(client.commando_modes('commado_mode_1').transitions.list())
#print(client.commando_modes('commado_mode_1').transitions.find("commando_mode_1_transition"))


#######


bulk_data = {
  "token": "bulk_10_token",
  "card_product_token": "my_card_product_02",
  "card_allocation": 3,
  "user_association": {
    "single_inventory_user": False
  },
  "name_line_1_numeric_postfix": True,
  "fulfillment": {
    "shipping": {
      "method": "USPS_REGULAR",
      "return_address": {
        "address1": "1222 Blake Street",
        "city": "Berkeley",
        "state": "CA",
        "postal_code": "94702",
        "country": "USA",
        "phone": "510-222-2222",
        "first_name": "Shipping",
        "last_name": "R_US"
      },
      "recipient_address": {
        "address1": "1255 Lake Street",
        "city": "Oakland",
        "state": "CA",
        "postal_code": "94611",
        "country": "USA",
        "phone": "510-333-3333",
        "first_name": "Saki",
        "last_name": "Dogger"
      }
    },
    "card_personalization": {
      "text": {
          "name_line_1": {
            "value": "Saki Dogger"
          },
          "name_line_2": {
            "value": "Chicken Tooth Music"
          }
      },
      "images": {
        "card": {
           "name": "my_card_logo.png",
           "thermal_color": "Black"
        },
        "carrier": {
          "name": "my_carrier_logo.png",
          "message_1": "my message"
        },
        "signature": {
          "name": "my_signature.png"
        },
        "carrier_return_window": {
          "name": "my_return_address_image.png"
        }
      }
    }
  }
}



print(client.bulk_issuances.list(limit = 3))
print(client.bulk_issuances.find('bulk_06_token'))
print(client.bulk_issuances.create(bulk_data))


###### Campaign ###########

campaign_data =       {
        "active": True,
        "name": "My campaign 10",
        "token": "my_campaign_token_10",
        "start_date": "2016-05-24",
        "end_date": "2019-05-24",
        "store_tokens": [
            "chicken_tooth_music_east_token",
            "chicken_tooth_music_west_token"
        ]
      }


campaign_update = {
    "active": "false"
}
print(client.campaigns.list(limit = 3))
#print(client.campaigns.find('My_campaign_02'))
print(client.campaigns('My_campaign_02').stores.list())
#print("test print",client.campaigns.create(campaign_data))
#print(client.campaigns.save('my_campaign_token_03',campaign_update))


##### ChargeBacks ########

charge_data = {
 "token": "my_chargeback_3000",
  "transaction_token": "222",
  "amount": 1.00,
  "credit_user": True,
  "reason_description": "FRAUD_TRANSACTION",
  "memo": "Charging back due to fraud",
  "channel": "ISSUER"
}

charge_tran_data  = {
    "token": "my_chargeback_transition_06",
    "chargeback_token": "my_chargeback_06",
    "amount": 3.00,
    "state": "CASE_WON",
    "reason": "Uncontested"
}


print(client.chargebacks.list())
#print(client.chargebacks.create(charge_data))
print(client.chargebacks.find('my_chargeback_03'))
#print(client.chargebacks('my_chargeback_03').grant_provisional_credit())
#print(client.chargebacks('my_chargeback_03').reverse_provisional_credit())

#print(client.chargebacks('my_chargeback_03').transitions.create(charge_tran_data))
#print(client.chargebacks('my_chargeback_03').transitions.find('my_chargeback_transition_06'))
print(client.chargebacks('my_chargeback_03').transitions.list())


#### Direct Deposit  #######

direct_data_update = {
    "allow_immediate_credit": True
}

trans_data = {
  "token" : "019b3329-6d18-49e6-adb7-34045a4a3a89",
  "channel": "API",
  "reason": "Manual state change",
  "direct_deposit_token" : "ff035886-5a59-4e9a-86a1-dba8a7cf9c06",
  "state": "APPLIED",
  "reason_code": "R11"
}
print(client.direct_deposits.list(limit = 3))
#client.direct_deposits.find('00acce2b-cead-45ab-9417-f8a62326c0d5')

#client.direct_deposits.accounts.find('3f0aa078-1db7-47cf-abf4-3a7ae7cd9e20')
#client.direct_deposits.accounts.save('3f0aa078-1db7-47cf-abf4-3a7ae7cd9e20',direct_data_update)

#client.direct_deposits('00acce2b-cead-45ab-9417-f8a62326c0d5').transitions.create(trans_data)
client.direct_deposits('00acce2b-cead-45ab-9417-f8a62326c0d5').transitions.list()
#client.direct_deposits('00acce2b-cead-45ab-9417-f8a62326c0d5').transitions.find('460d40c8-1a33-436b-8e49-de895eecbff3')


######   FEES    #######

fee_data = {
  "token": "my_fee_0134",
  "amount": "1.00",
  "name": "My Fee 01",
  "currency_code": "USD",
  "real_time_assessment": {
    "international_enabled": True,
    "domestic_enabled": True,
    "transaction_type": "authorization"
  },
  "tags": "My Tags"
}

fee_update = {
    "active": False
}

print(client.fees.list())
print(client.fees.find('my_fee_01'))
print(client.fees.create(fee_data))
print(client.fees.save('my_fee_01', fee_update))



####  FEEE TRansfer ######

feetrans_data = {
  "fees": [
    {
    "token": "my_fee_01",
    "memo": "Initiation fee"
    }
  ],
    "token": "my_feetransfer_0123",
    "user_token": "my_user_01"
}
print(client.fee_transfers.find('my_feetransfer_01'))
#print(client.fee_transfers.create(feetrans_data))


###### MCC Groups ########

mcc_data = {
  "token": "my_mccgroup_0112",
  "name": "My MCC Group 01",
  "mccs": ["0123", "2224-2230", "3876"
  ],
  "active": True,
  "config": {
    "authorization_controls": {
      "hold_increase": {
        "type": "PERCENT",
        "value": 20
      },
      "hold_expiration_days": 2
    }
  }
}


mcc_update = {
  "mccs": ["0123", "2224-2230"
  ]
}

print(client.mcc_groups.list(limit =6))
print(client.mcc_groups.find('my_mccgroup_01'))
print(client.mcc_groups.create(mcc_data))
print(client.mcc_groups.save('my_mccgroup_01', mcc_update))

##### MERCHANTS  ########
merchant_data = {
    "name": "My Merchant",
    "active": "true",
    "contact": "John Doe",
    "address1": "600 Pants Ave",
    "city": "Detroit",
    "state": "MI",
    "zip": "12345",
    "phone": "1236547890",
    "token": "my_merchant123"
}


merchant_update = {
    "active": "false"
}
print(client.merchants.list())
print(client.merchants.find('my_merchant'))
print(client.merchants('my_merchant').stores.list())
print(client.merchants.create(merchant_data))
print(client.merchants.save('my_merchant',merchant_update))


##### OFFERS #####
offer_data = {
    "token": "my_offer124",
    "active": "true",
    "name": "May_offer",
    "currency_code": "840",
    "purchase_amount": "200",
    "reward_amount": "50",
    "campaign_token": "my_campaign_01"
}

offer_update = {
    "start_date": "2014-12-01",
    "end_date": "2015-01-01"
}

print(client.offers.list())
print(client.offers.find('my_offer'))
print(client.offers.create(offer_data))
print(client.offers.save('my_offer', offer_update))


##### PROGRAM TRANSFER #########

pgm_data = {
  "token": "my_program_transfer_011",
  "amount": "1.00",
  "tags": "my, tags",
  "memo": "This is my program transfer",
  "type_token": "my_program_transfer_type_01",
  "user_token": "my_user_01",
  "currency_code": "USD"
}

pgm_trans_data ={
  "token": "my_program_transfer_type_01",
  "tags": "my, tags",
  "memo": "This is my program transfer type.",
  "program_funding_source_token": "my_pfs_01"
}

pgm_trans_update ={
  "program_funding_source_token": "pfs_test_02"
}

print(client.program_transfers.list(limit =1 ))
print(client.program_transfers.find('my_program_transfer_01'))
#print(client.program_transfers.create(pgm_data))

print(client.program_transfers.types.list())
#print(client.program_transfers.types.find('my_program_transfer_type_02'))
#print(client.program_transfers.types.create(pgm_trans_data))
#print(client.program_transfers.types.save('my_program_transfer_type_02',pgm_trans_update))


##### PUSHTOCARDS ##########
push_data ={
  "currency_code": "840",
  "amount": 10.00,
  "payment_instrument_token": "8b2bz20d-7cdc-492b-81z4-77a295z1e471"
}

pay_data = {
  "user_token": "myUser",
  "name_on_card": "John Smith",
  "pan": "1234123412341234",
  "cvv": "123",
  "exp_date": "0120",
  "address_1": "123 Main Street",
  "city": "Oakland",
  "state": "CA",
  "postal_code":  "94601",
  "country": "USA"
}



print(client.push_to_cards.disburse.list())
#print(client.push_to_cards.disburse.find('4fc83b87-816e-4f67-8819-3a22d912943c'))
#print(client.push_to_cards.disburse.create(push_data))

print(client.push_to_cards.payment_card.list_for_user('my_user'))
#print(client.push_to_cards.payment_card.find('8fdc41ee-95c5-4a06-83a3-3e6f2537b787'))
#print(client.push_to_cards.payment_card.create(pay_data))


#### REAL-TIME GROUP ########
real_data = {
  "name": "My Real-Time Fee Group 01",
  "token": "my_rtfg_01",
  "fee_tokens": [
    "my_fee_01", "my_fee_05"
  ]
}

real_update = {
    "active": False
}

print(client.real_time_fee_groups.list())
#print(client.real_time_fee_groups.find('my_rtfg_01'))
#print(client.real_time_fee_groups.create(real_data))
#print(client.real_time_fee_groups.save('my_rtfg_01', real_update))


##### STORES #########

store_data = {
  "token": "my_store",
  "mid": "123456",
  "state": "ca",
  "zip": "94610",
  "address1": "200 Ellis Ave",
  "city": "Newville",
  "merchant_token": "BigChainRestaurant_merchant",
  "name": "Store1"
}

store_update = {
   "contact": "my_contact"
}

print(client.stores.list(limit =6))
print(client.stores.find('my_store'))
print(client.stores.find_by_mid('123456'))
#print(client.stores.create(store_data))
print(client.stores.save('my_store', store_update))


##### TRANSACTIONS #########

print(client.transactions.list(limit =3))
#print(client.transactions.list_for_funding_source('1200'))
#print(client.transactions.find('1200'))
print(client.transactions('1201').related.list())

######  VELOCITY CONTROL ##########
vel_data= {
  "usage_limit": 10,
  "amount_limit": 500,
  "velocity_window": "DAY",
  "association": {
    "user_token": "my_user_04"
  },
  "currency_code": "USD",
  "token": "my_velocitycontrol_01234"
}

vel_update = {
  "usage_limit": 20,
  "amount_limit": 1000
}

print(client.velocity_controls.list(limit = 2))
print(client.velocity_controls.find('my_velocitycontrol_01'))
print(client.velocity_controls.list_available_for_user('my_user_04'))
print(client.velocity_controls.create(vel_data))
print(client.velocity_controls.save('my_velocitycontrol_01', vel_update))

###### WEBHOOOK ############
web_data = {
  "token": "my_webhook_token",
  "active": False,
  "events": [
    "*"
  ],
  "config": {
    "url": "https://my_secure_domain.com/webhook",
    "secret": "My_20-character-min_secret",
    "basic_auth_username": "my_username",
    "basic_auth_password": "My_20-character-min_password"
  },
  "name": "My_Webhook_Name"
}


web_update ={
  "events": [
    "transaction.*"
  ]
}

print(client.webhooks.list())
#print(client.webhooks.find('my_webhook_token'))
#print(client.webhooks('my_webhook_token').ping())
#print(client.webhooks('my_webhook_token').resend('cardtransition', 'my_webhook_token'))
#print(client.webhooks.create(web_data))
#print(client.webhooks.save('my_webhook_token', web_update))

###### Digital Wallet Token #####

wallet_data = {}
print(client.digital_wallet_tokens.list())
# print(client.digital_wallet_tokens.list_for_card('platinum_grizzcard'))
# print(client.digital_wallet_tokens.find('ccc47fa8-7730-4188-91f6-7214ba38b8f3'))
# print(client.digital_wallet_tokens.find_show_pan('ccc47fa8-7730-4188-91f6-7214ba38b8f3'))

# print(client.digital_wallet_tokens('ccc47fa8-7730-4188-91f6-7214ba38b8f3').transitions.create(wallet_data))
print(client.digital_wallet_tokens('ccc47fa8-7730-4188-91f6-7214ba38b8f3').transitions.find('my_transition_04'))
#print(client.digital_wallet_tokens('my_transition_04').transitions.list())


##### PINS ######

pins_data = {
  "control_token": "string",
  "pin": "2345"
}

pins_create_data = {
  "card_token": "string"
}

#print(client.pins.create_control_token(pins_create_data))
#print(client.pins.new(pins_data))


##### Pings #########

print(client.ping())
print(client.ping(token ='wre', payload='wdfgfg'))
