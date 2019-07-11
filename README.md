# marqeta-python

The Marqeta Python library provides access to the Marqeta platform [Core API](https://www.marqeta.com/api/docs/WYDH6igAAL8FnF21/api-introduction).

This library is released as a Beta. If you find anything that needs fixing or can be improved, please [create an issue](issues) on GitHub.

## Documentation

For complete reference documentation, see the [Marqeta Core API Reference](https://www.marqeta.com/api/docs/WYDH6igAAL8FnF21/api-introduction).

## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/stable/), a package manager for Python.

```
pip install marqeta
```

### Requirements

* Python 3.7+

### Dependencies

* [Requests](http://docs.python-requests.org/)

## Usage

### Configuring the client

Create an account on marqeta.com to retrieve your application token and access token for the shared sandbox. For production, you will need to change `base_url` too.

Configure your client object.

```
from marqeta import Client

base_url = "https://shared-sandbox-api.marqeta.com/v3/"
application_token = "MY_APPLICATION_TOKEN"
access_token = "MY_ACCESS_TOKEN"
timeout = 60 # seconds

client = Client(base_url, application_token, access_token, timeout)
```

When specifying your base url, include the `/v3/` version prefix with the trailing slash.

### Accessing resources

Access resource collections of the Core API as properties of the client object.

For example, to access the `/users` endpoint:

```
client.users
```

Nested resource collection are properties of the parent collection.

For example, to access the `/chargebacks/{token}/transitions` endpoint:

```
client.chargebacks(token).transitions
```

### Listing objects

There are multiple ways to retrieve collections of objects, depending on your use case. The library will intelligently handle pagination for you, unless you request a specific page of data.

To simply retrieve every object in a collection, call `list(limit=None)` on the resource.

```
users = client.users.list(limit=None)
```

If an integer is specified for 'limit', the library will return up to maximum of `limit` objects. The default value of `limit` is typically `None`, however for `client.users.list()` and `client.card_products.list()` the default limits are 1000 and 25 respectively.

The `stream()` method returns a generator that efficiently downloads subsequent pages as needed, as opposed to downloading all objects into memory at once.

```
for user in client.users.stream():
    pass
```

To retrieve a single page, call the `page()` method specifying `start_index` and `count`.

```
page = client.users.page(start_index=0, count=5)
users = page.data
```

You can specify by which field the results should be sorted by passing a `params` dictionary:

```
client.users.list(params={'sort_by': '-lastModifiedTime'})
```

See [Sorting & Pagination](https://www.marqeta.com/api/docs/Vh2cbhwAAMsAF3db/sorting--pagination) for further details.

### Specifying additional query parameters

Most methods support specifying additional query parameters as a `params` dictionary. The keys and values are the same as the HTTP API.

```
client.cards.find_show_pan(card_token, params={'show_cvv_number': True})
```

### Finding a specific objects

Call the `find()` method on a resource collection, passing in the object's token.

```
user = client.users.find(token)
```

### Creating objects

Call the `create()` method of a resource collection, passing in `data` as a Python dict.

```
data = {
    'first_name': 'Sarah'
}
created_user = client.users.create(data)
```

### Updating objects

Call the `save()` method of a resource collection, passing in the object's token and a Python dictionary containing the fields you wish to update.

```
fields_to_update = {
    'first_name': 'Updated Value'
}
updated_user = client.users.save(user_token, fields_to_update)
```

### Handling errors

The SDK will raise a `MarqetaError` exception for unsuccessful requests.

```
from marqeta import Client
from marqeta.errors import MarqetaError
from requests.exceptions import RequestException

try:
    user = client.users.find(token)
except MarqetaError as error:
    print(error.code)
except RequestException as error:
    print(error)
```

The exception's `code` card_products contains the value returned by the API in the JSON response. See [Error codes and messages](https://www.marqeta.com/api/docs/Vh2cTBwAAB8AF3aI/errors#error_codes_and_messages).

## Resources

The library supports the following endpoints:

| Endpoint | Python code |
| -------- | ----------- |
| [/acceptedcountries](#Accepted-Countries-/acceptedcountries) | `client.accepted_countries` |
| [/accountholdergroups](#Account-Holder-Groups-/accountholdergroups) | `client.account_holder_groups` |
| [/authcontrols](#Auth-Controls-/authcontrols) | `client.auth_controls` |
| [/authcontrols/exemptmids](#Exempt-MIDs-/authcontrols/exemptmids) | `client.auth_controls.exempt_mids` |
| [/autoreloads](#Autoreloads-/autoreloads) | `client.auto_reloads` |
| [/balances](#Balances-/balances) | `client.balances` |
| [/bulkissuances](#Bulk-Issuances-/bulkissuances) | `client.bulk_issuances` |
| [/businesses](#Businesses-/businesses) | `client.businesses` |
| [/businesstransitions](#Business-Transitions-/businesstransitions) | `client.businesses(business_token).transitions` |
| [/businesses/{token}/notes](#Business-Notes-/businesses/{token}/notes) | `client.businesses(token).notes` |
| [/cardproducts](#Card-Products-/cardproducts) | `client.card_products` |
| [/cards](#Cards-/cards) | `client.cards` |
| [/cardtransitions](#Card-Transitions-/cardtransitions) | `client.cards(token).transitions` |
| [/chargebacks](#Chargebacks-/chargebacks) | `client.chargebacks` |
| [/chargebacks/transitions](#Chargeback-Transitions-/chargebacks/transitions) | `client.chargebacks(token).transitions` |
| [/commandomodes](#Commando-Modes-/commandomodes) | `client.commando_modes` |
| [/commandomodes/transitions](#Commando-Mode-Transitions-/commandomodes/transitions) | `client.commando_modes(token).transitions` |
| [/digitalwallettokens](#Digital-Wallet-Tokens-/digitalwallettokens) | `client.digital_wallet_tokens` |
| [/digitalwallettokentransitions](#Digital-Wallet-Token-Transitions-/digitalwallettokentransitions) | `client.digital_wallet_tokens(token).transitions` |
| [/directdeposits](#Direct-Deposits-/directdeposits) | `client.direct_deposits` |
| [/directdeposits/transitions](#Direct-Deposit-Transitions-/directdeposits/transitions) | `client.direct_deposits(token).transitions` |
| [/directdeposits/accounts](#Direct-Deposit-Accounts-/directdeposits/accounts) | `client.direct_deposits.accounts` |
| [/fees](#Fees-/fees) | `client.fees` |
| [/feetransfers](#Fee-Transfers-/feetransfers) | `client.fee_transfers` |
| [/fundingsources](#Funding-Sources-/fundingsources) | `client.funding_sources` |
| [/fundingsources/addresses](#Funding-Source-Addresses-/fundingsources/addresses) | `client.funding_sources.addresses` |
| [/fundingsources/ach](#ACH-Funding-Sources-/fundingsources/ach) | `client.funding_sources.ach` |
| [/fundingsources/paymentcard](#Payment-Card-Funding-Sources-/fundingsources/paymentcard) | `client.funding_sources.payment_card` |
| [/fundingsources/programgateway](#Program-Gateway-Funding-Sources-/fundingsources/programgateway) | `client.funding_sources.program_gateway` |
| [/fundingsources/program](#Program-Funding-Sources-/fundingsources/program) | `client.funding_sources.program` |
| [/gpaorders](#GPA-Orders-/gpaorders) | `client.gpa_orders` |
| [/gpaorders/unloads](#GPA-Returns-/gpaorders/unloads) | `client.gpa_orders.unloads` |
| [/kyc](#KYC-/kyc) | `client.kyc` |
| [/mccgroups](#MCC-Groups-/mccgroups) | `client.mcc_groups` |
| [/merchants](#Merchants-/merchants) | `client.merchants` |
| [/merchants/{token}/stores](#Merchant-Stores-/merchants/{token}/stores) | `client.merchants(token).stores` |
| [/msaorders](#MSA-Orders-/msaorders) | `client.msa_orders` |
| [/msaorders/unloads](#MSA-Order-Unloads-/msaorders/unloads) | `client.msa_orders.unloads` |
| [/offerorders](#Offer-Orders-/offerorders) | `client.offer_orders` |
| [/pins](#Pin-Control-Tokens-/pins) | `client.pins` |
| [/programtransfers](#Program-Transfers-/programtransfers) | `client.program_transfers` |
| [/programtransfers/types](#Program-Transfer-Types-/programtransfers/types) | `client.program_transfers.types` |
| [/pushtocards](#Push-to-Cards-/pushtocards) | `client.push_to_cards` |
| [/pushtocards/disburse](#Push-to-Card-Disbursements-/pushtocards/disburse) | `client.push_to_cards.disburse` |
| [/pushtocards/paymentcard](#Push-to-Card-Payment-Cards-/pushtocards/paymentcard) | `client.push_to_cards.payment_card` |
| [/realtimefeegroups](#Realtime-Fee-Groups-/realtimefeegroups) | `client.real_time_fee_groups` |
| [/transactions](#Transactions-/transactions) | `client.transactions` |
| [/transactions/{token}/related](#Related-Transations-/transactions/{token}/related) | `client.transactions(token).related` |
| [/users](#Users-/users) | `client.users` |
| [/usertransitions](#User-Transitions-/usertransitions) | `client.users(token).transitions` |
| [/users/{token}/notes](#User-Notes-/users/{token}/notes) | `client.users(token).notes` |
| [/velocitycontrols](#Velocity-Controls-/velocitycontrols) | `client.velocity_controls` |
| [/webhooks](#Webhooks-/webhooks) | `client.webhooks` |

### Examples


#### Accepted Countries (`/acceptedcountries`)

```
# List all accepted countries
accepted_countries = client.accepted_countries.list()
for accepted_country in client.accepted_countries.stream():
    pass
accepted_countries_page = client.accepted_countries.page(start_index=0)

# Retrieve a specific accepted country
accepted_country = client.accepted_countries.find(token)

# Create an accepted country
accepted_country = client.accepted_countries.create({...})

# Update an accepted country
accepted_country = client.accepted_countries.save(token, {...})
```

#### Account Holder Groups (`/accountholdergroups`)

```
# List all account holder groups
account_holder_groups = client.account_holder_groups.list()
for account_holder_group in client.account_holder_groups.stream():
    pass
account_holder_groups_page = client.account_holder_groups.page(start_index=0)

# Retrieve a specific account holder group
account_holder_group = client.account_holder_groups.find(token)

# Create an account holder group
account_holder_group = client.account_holder_groups.create({...})

# Update an account holder group
account_holder_group = client.account_holder_groups.save(token, {...})
```

#### Auth Controls (`/authcontrols`)

```
# List all auth controls
auth_controls = client.auth_controls.list()
for auth_control in client.auth_controls.stream():
    pass
auth_controls_page = client.auth_controls.page(start_index=0)

# Retrieve a specific auth control
auth_control = client.auth_controls.find(token)

# Create an auth control
auth_control = client.auth_controls.create({...})

# Update an auth control
auth_control = client.auth_controls.save(token, {...})
```

#### Exempt MIDs (`/authcontrols/exemptmids`)

```
# List all exempt mids
exempt_mi_ds = client.auth_controls.exempt_mids.list()
for exempt_mid in client.auth_controls.exempt_mids.stream():
    pass
exempt_mi_ds_page = client.auth_controls.exempt_mids.page(start_index=0)

# Retrieve a specific exempt mid
exempt_mid = client.auth_controls.exempt_mids.find(token)

# Create an exempt mid
exempt_mid = client.auth_controls.exempt_mids.create({...})

# Update an exempt mid
exempt_mid = client.auth_controls.exempt_mids.save(token, {...})
```

#### Autoreloads (`/autoreloads`)

```
# List all autoreloads
autoreloads = client.auto_reloads.list()
for autoreload in client.auto_reloads.stream():
    pass
autoreloads_page = client.auto_reloads.page(start_index=0)

# Retrieve a specific autoreload
autoreload = client.auto_reloads.find(token)

# Create an autoreload
autoreload = client.auto_reloads.create({...})

# Update an autoreload
autoreload = client.auto_reloads.save(token, {...})
```

#### Balances (`/balances`)

```
# List all MSA balances
balances = client.balances.list_msas_for_user_or_business(token)
for balance in client.balances.stream_msas_for_user_or_business(token):
    pass

# Retrieve a specific balance
balance = client.balances.find_for_user_or_business(token)
```

#### Bulk Issuances (`/bulkissuances`)

```
# List all bulk issuances
bulk_issuances = client.bulk_issuances.list()
for bulk_issuance in client.bulk_issuances.stream():
    pass
bulk_issuances_page = client.bulk_issuances.page(start_index=0)

# Retrieve a specific bulk issuance
bulk_issuance = client.bulk_issuances.find(token)

# Create a bulk issuance
bulk_issuance = client.bulk_issuances.create({...})
```

#### Businesses (`/businesses`)

```
# List all businesses
businesses = client.businesses.list()
for business in client.businesses.stream():
    pass
businesses_page = client.businesses.page(start_index=0)

# Retrieve a specific business
business = client.businesses.find(token)

# Create a business
business = client.businesses.create({...})

# Update a business
business = client.businesses.save(token, {...})

# Retrieve a specific business SSN
ssn = client.businesses(token).ssn()

# Retrieve a specific business Full SSN
ssn = client.businesses(token).ssn(full_ssn = True)

# List all children of parent business
child_cardholders = client.businesses(token).children.list()
for child_cardholder in client.businesses(token).children.stream():
    pass
child_cardholders_page = client.businesses(token).children.page(start_index=0)

# Search for businesses
businesss = client.businesses.look_up({...})
```

#### Business Transitions (`/businesstransitions`)

```
# Create a business transition
transition = client.businesses(business_token).transitions.create(...)

# Retrieve a specific business transition
transition = client.businesses(business_token).transitions.find(token)

# List transitions for a specific business
transitions = client.businesses(business_token).transitions.list()
for transition in client.businesses(business_token).transitions.stream():
    pass
transitions_page = client.businesses(business_token).transitions.page(start_index=0)
```

#### Business Notes (`/businesses/{token}/notes`)

```
# List all business notes
business_notes = client.businesses(token).notes.list()
for business_note in client.businesses(token).notes.stream():
    pass
business_notes_page = client.businesses(token).notes.page(start_index=0)

# Create a business note
business_note = client.businesses(token).notes.create({...})

# Update a business note
business_note = client.businesses(token).notes.save(token, {...})
```

#### Card Products (`/cardproducts`)

```
# List all card products. Default limit is 25.
card_products = client.card_products.list()
for card_product in client.card_products.stream():
    pass
card_products_page = client.card_products.page(start_index=0)

# Retrieve a specific card product
card_product = client.card_products.find(token)

# Create a card product
card_product = client.card_products.create({...})

# Update a card product
card_product = client.card_products.save(token, {...})
```

#### Cards (`/cards`)

```
# List cards by last 4
cards = client.cards.list(last_four='6789')
for card in client.cards.stream():
    pass
cards_page = client.cards.page()

# Lists all cards for one user
cards = client.cards.list_for_user(token)
for card in client.cards.stream_for_user(token):
    pass

# Returns a specific card
card = client.cards.find(token)

# Returns a specific card - PAN visible
card = client.cards.find_show_pan(token)

# Retrieve a card by its barcode
card = client.cards.find_by_barcode(barcode)

# Creates a card
data = {...}
card = client.cards.create(data)

# Returns the user and card tokens for specified PAN
tokens = client.cards.tokens_for_pan(pan)

# Updates a card
data = {...}
card = client.cards.save(data)

# Returns a merchant onboarding card
card = client.cards.find_for_merchant(token)

# Returns a specific card - PAN visible
card = client.cards.find_for_merchant_show_pan(token)

# Creates a merchant onboarding card
data = {...}
card = client.cards.create_for_merchant(token, data)
```

#### Card Transitions (`/cardtransitions`)

```
# Create a card transition
transition = client.cards(token).transitions.create(...)

# Retrieve a specific card transition
transition = client.cards(token).transitions.find(token)

# List transitions for a specific card
transitions = client.cards(token).transitions.list()
for transition in client.cards(token).transitions.stream():
    pass
transitions_page = client.cards(token).transitions.page(start_index=0)
```

#### Chargebacks (`/chargebacks`)

```
# List all chargebacks
chargebacks = client.chargebacks.list()
for chargeback in client.chargebacks.stream():
    pass
chargebacks_page = client.chargebacks.page(start_index=0)

# Retrieve a specific chargeback
chargeback = client.chargebacks.find(token)

# Create a chargeback
chargeback = client.chargebacks.create({...})

# Grant provisional credit
client.chargebacks(token).grant_provisional_credit()

# Reverse provisional credit
client.chargebacks(token).reverse_provisional_credit()
```

#### Chargeback Transitions (`/chargebacks/transitions`)

```
# Create a chargeback transition
transition = client.chargebacks(token).transitions.create(...)

# Retrieve a specific chargeback transition
transition = client.chargebacks(token).transitions.find(token)

# List transitions for a specific chargeback
transitions = client.chargebacks(token).transitions.list()
for transition in client.chargebacks(token).transitions.stream():
    pass
transitions_page = client.chargebacks(token).transitions.page(start_index=0)
```

#### Commando Modes (`/commandomodes`)

```
# List all commando modes
commando_modes = client.commando_modes.list()
for commando_mode in client.commando_modes.stream():
    pass
commando_modes_page = client.commando_modes.page(start_index=0)

# Retrieve a specific commando mode
commando_mode = client.commando_modes.find(token)
```

#### Commando Mode Transitions (`/commandomodes/transitions`)

```
# Retrieve a specific commando mode transition
transition = client.commando_modes(token).transitions.find(token)

# List transitions for a specific commando mode
transitions = client.commando_modes(token).transitions.list()
for transition in client.commando_modes(token).transitions.stream():
    pass
transitions_page = client.commando_modes(token).transitions.page(start_index=0)
```

#### Digital Wallet Tokens (`/digitalwallettokens`)

```
# List all digital wallet tokens
digital_wallet_tokens = client.digital_wallet_tokens.list()
for digital_wallet_token in client.digital_wallet_tokens.stream():
    pass
digital_wallet_tokens_page = client.digital_wallet_tokens.page(start_index=0)

# Retrieve a specific digital wallet token
digital_wallet_token = client.digital_wallet_tokens.find(token)

# Retrieve a specific digital wallet token with PAN
digital_wallet_token = client.digital_wallet_tokens.find_show_pan(token)
```

#### Digital Wallet Token Transitions (`/digitalwallettokentransitions`)

```
# Create a digital wallet token transition
transition = client.digital_wallet_tokens(token).transitions.create(...)

# Retrieve a specific digital wallet token transition
transition = client.digital_wallet_tokens(token).transitions.find(token)

# List transitions for a specific digital wallet token
transitions = client.digital_wallet_tokens(token).transitions.list()
for transition in client.digital_wallet_tokens(token).transitions.stream():
    pass
transitions_page = client.digital_wallet_tokens(token).transitions.page(start_index=0)
```

#### Direct Deposits (`/directdeposits`)

```
# List all direct deposits
direct_deposits = client.direct_deposits.list()
for direct_deposit in client.direct_deposits.stream():
    pass
direct_deposits_page = client.direct_deposits.page(start_index=0)

# Retrieve a specific direct deposit
direct_deposit = client.direct_deposits.find(token)
```

#### Direct Deposit Transitions (`/directdeposits/transitions`)

```
# Create a direct deposit transition
transition = client.direct_deposits(token).transitions.create(...)

# Retrieve a specific direct deposit transition
transition = client.direct_deposits(token).transitions.find(token)

# List transitions for a specific direct deposit
transitions = client.direct_deposits(token).transitions.list()
for transition in client.direct_deposits(token).transitions.stream():
    pass
transitions_page = client.direct_deposits(token).transitions.page(start_index=0)
```

#### Direct Deposit Accounts (`/directdeposits/accounts`)

```

# Retrieve a specific direct deposit account
direct_deposit_account = client.direct_deposits.accounts.find(token)

# Update a direct deposit account
direct_deposit_account = client.direct_deposits.accounts.save(token, {...})
```

#### Fees (`/fees`)

```
# List all fees
fees = client.fees.list()
for fee in client.fees.stream():
    pass
fees_page = client.fees.page(start_index=0)

# Retrieve a specific fee
fee = client.fees.find(token)

# Create a fee
fee = client.fees.create({...})

# Update a fee
fee = client.fees.save(token, {...})
```

#### Fee Transfers (`/feetransfers`)

```

# Retrieve a specific fee transfer
fee_transfer = client.fee_transfers.find(token)

# Create a fee transfer
fee_transfer = client.fee_transfers.create({...})
```

#### Funding Sources (`/fundingsources`)

```
# List all funding sources for a specific user
funding_sources = client.list_for_user(user_token)
for funding_source in client.stream_for_user(user_token):
    pass

# List all funding sources for a specific business
funding_sources = client.list_for_business(business_token)
for funding_source in client.stream_for_business(business_token):
    pass
```

#### Funding Source Addresses (`/fundingsources/addresses`)

```

# Retrieve a specific funding source address
funding_source_address = client.funding_sources.addresses.find(token)

# Create a funding source address
funding_source_address = client.funding_sources.addresses.create({...})

# Update a funding source address
funding_source_address = client.funding_sources.addresses.save(token, {...})

# list funding source addresses for a specific user
addresses = client.funding_sources.addresses.list_for_user(user_token)
for address in client.funding_sources.addresses.stream_for_user(user_token)
    pass

# list funding source addresses for a specific business
addresses = client.funding_sources.addresses.list_for_business(business_token)
for address in client.funding_sources.addresses.stream_for_business(business_token)
    pass
```

#### ACH Funding Sources (`/fundingsources/ach`)

```

# Retrieve a specific ach funding source
ach_funding_source = client.funding_sources.ach.find(token)

# Create an ach funding source
ach_funding_source = client.funding_sources.ach.create({...})

# Update an ach funding source
ach_funding_source = client.funding_sources.ach.save(token, {...})

# Retrieve the dollar amounts used to verify an ACH funding source
client.funding_sources.addresses(token).verification_amounts()
```

#### Payment Card Funding Sources (`/fundingsources/paymentcard`)

```

# Retrieve a specific payment card funding source
payment_card_funding_source = client.funding_sources.payment_card.find(token)

# Create a payment card funding source
payment_card_funding_source = client.funding_sources.payment_card.create({...})

# Update a payment card funding source
payment_card_funding_source = client.funding_sources.payment_card.save(token, {...})
```

#### Program Gateway Funding Sources (`/fundingsources/programgateway`)

```

# Retrieve a specific program gateway funding source
program_gateway_funding_source = client.funding_sources.program_gateway.find(token)

# Create a program gateway funding source
program_gateway_funding_source = client.funding_sources.program_gateway.create({...})

# Update a program gateway funding source
program_gateway_funding_source = client.funding_sources.program_gateway.save(token, {...})
```

#### Program Funding Sources (`/fundingsources/program`)

```

# Retrieve a specific program funding source
program_funding_source = client.funding_sources.program.find(token)

# Create a program funding source
program_funding_source = client.funding_sources.program.create({...})

# Update a program funding source
program_funding_source = client.funding_sources.program.save(token, {...})
```

#### GPA Orders (`/gpaorders`)

```

# Retrieve a specific gpa order
gpa_order = client.gpa_orders.find(token)

# Create a gpa order
gpa_order = client.gpa_orders.create({...})
```

#### GPA Returns (`/gpaorders/unloads`)

```
# List all gpa returns
gpa_returns = client.gpa_orders.unloads.list()
for gpa_return in client.gpa_orders.unloads.stream():
    pass
gpa_returns_page = client.gpa_orders.unloads.page(start_index=0)

# Retrieve a specific gpa return
gpa_return = client.gpa_orders.unloads.find(token)

# Create a gpa return
gpa_return = client.gpa_orders.unloads.create({...})
```

#### KYC (`/kyc`)

```
# List KYC results for a specific user
kyc_results = client.kyc.list_for_user(user_token)
for kyc_result in client.kyc.stream_for_user(user_token):
    pass

# List KYC results for a specific business
kyc_results = client.kyc.list_for_business(business_token)
for kyc_result in client.kyc.stream_for_business(business_token):
    pass

# Retrieve a specific KYC result
kyc = client.kyc.find(token)

# Update KYC answers
client.kyc.save(token, {...})

# Perform a KYC operation
client.kyc.create({...})
```

#### MCC Groups (`/mccgroups`)

```
# List all mcc groups
mcc_groups = client.mcc_groups.list()
for mcc_group in client.mcc_groups.stream():
    pass
mcc_groups_page = client.mcc_groups.page(start_index=0)

# Retrieve a specific mcc group
mcc_group = client.mcc_groups.find(token)

# Create a mcc group
mcc_group = client.mcc_groups.create({...})

# Update a mcc group
mcc_group = client.mcc_groups.save(token, {...})
```

#### Merchants (`/merchants`)

```
# List all merchants
merchants = client.merchants.list()
for merchant in client.merchants.stream():
    pass
merchants_page = client.merchants.page(start_index=0)

# Retrieve a specific merchant
merchant = client.merchants.find(token)

# Create a merchant
merchant = client.merchants.create({...})

# Update a merchant
merchant = client.merchants.save(token, {...})
```

#### Merchant Stores (`/merchants/{token}/stores`)

```
# List all merchant stores
merchant_stores = client.merchants(token).stores.list()
for merchant_store in client.merchants(token).stores.stream():
    pass
merchant_stores_page = client.merchants(token).stores.page(start_index=0)
```

#### MSA Orders (`/msaorders`)

```
# Retrieve a specific msa order
msa_order = client.msa_orders.find(token)

# Create a msa order
msa_order = client.msa_orders.create({...})

# Update a msa order
msa_order = client.msa_orders.save(token, {...})
```

#### MSA Order Unloads (`/msaorders/unloads`)

```
# List all msa order unloads
msa_order_unloads = client.msa_orders.unloads.list()
for msa_order_unload in client.msa_orders.unloads.stream():
    pass
msa_order_unloads_page = client.msa_orders.unloads.page(start_index=0)

# Retrieve a specific msa order unload
msa_order_unload = client.msa_orders.unloads.find(token)

# Create a msa order unload
msa_order_unload = client.msa_orders.unloads.create({...})
```

#### Offer Orders (`/offerorders`)

```
# Retrieve a specific offer order
offer_order = client.offer_orders.find(token)

# Create an offer order
offer_order = client.offer_orders.create({...})
```

#### Pin Control Tokens (`/pins`)

```
# Create a pin control token
pin_control_token = client.pins.create({...})

# Update a pin control token
pin_control_token = client.pins.save(token, {...})
```

#### Program Transfers (`/programtransfers`)

```
# List all program transfers
program_transfers = client.program_transfers.list()
for program_transfer in client.program_transfers.stream():
    pass
program_transfers_page = client.program_transfers.page(start_index=0)

# Retrieve a specific program transfer
program_transfer = client.program_transfers.find(token)

# Create a program transfer
program_transfer = client.program_transfers.create({...})
```

#### Program Transfer Types (`/programtransfers/types`)

```
# List all program transfer types
program_transfer_types = client.program_transfers.types.list()
for program_transfer_type in client.program_transfers.types.stream():
    pass
program_transfer_types_page = client.program_transfers.types.page(start_index=0)

# Retrieve a specific program transfer type
program_transfer_type = client.program_transfers.types.find(token)

# Create a program transfer type
program_transfer_type = client.program_transfers.types.create({...})

# Update a program transfer type
program_transfer_type = client.program_transfers.types.save(token, {...})
```

#### Push-to-Cards (`/pushtocards`)

```
# List all push-to-cards
push_to_cards = client.push_to_cards.list()
for push_to_card in client.push_to_cards.stream():
    pass
push_to_cards_page = client.push_to_cards.page(start_index=0)

# Retrieve a specific push-to-card
push_to_card = client.push_to_cards.find(token)

# Create a push-to-card
push_to_card = client.push_to_cards.create({...})

# Update a push-to-card
push_to_card = client.push_to_cards.save(token, {...})
```

#### Push-to-Card Disbursements (`/pushtocards/disburse`)

```
# List all push-to-card disbursements
push_to_card_disbursements = client.push_to_cards.disburse.list()
for push_to_card_disbursement in client.push_to_cards.disburse.stream():
    pass
push_to_card_disbursements_page = client.push_to_cards.disburse.page(start_index=0)

# Retrieve a specific push-to-card disbursement
push_to_card_disbursement = client.push_to_cards.disburse.find(token)

# Create a push-to-card disbursement
push_to_card_disbursement = client.push_to_cards.disburse.create({...})
```

#### Push-to-Card Payment Cards (`/pushtocards/paymentcard`)

```
# List all push-to-card payment cards
push_to_card_payment_cards = client.push_to_cards.payment_card.list()
for push_to_card_payment_card in client.push_to_cards.payment_card.stream():
    pass
push_to_card_payment_cards_page = client.push_to_cards.payment_card.page(start_index=0)

# Retrieve a specific push-to-card payment card
push_to_card_payment_card = client.push_to_cards.payment_card.find(token)

# Create a push-to-card payment card
push_to_card_payment_card = client.push_to_cards.payment_card.create({...})
```

#### Realtime Fee Groups (`/realtimefeegroups`)

```
# List all realtime fee groups
realtime_fee_groups = client.real_time_fee_groups.list()
for realtime_fee_group in client.real_time_fee_groups.stream():
    pass
realtime_fee_groups_page = client.real_time_fee_groups.page(start_index=0)

# Retrieve a specific realtime fee group
realtime_fee_group = client.real_time_fee_groups.find(token)

# Create a realtime fee group
realtime_fee_group = client.real_time_fee_groups.create({...})

# Update a realtime fee group
realtime_fee_group = client.real_time_fee_groups.save(token, {...})
```

#### Transactions (`/transactions`)

```
# List all transactions
transactions = client.transactions.list()
for transaction in client.transactions.stream():
    pass
transactions_page = client.transactions.page(start_index=0)

# List all transactions for a specific funding source
transactions = client.transactions.list_for_funding_source(funding_source_token)
for transaction in client.transactions.stream_for_funding_source(funding_source_token):
    pass

# Retrieve a specific transaction
transaction = client.transactions.find(token)
```

#### Related Transations (`/transactions/{token}/related`)

```
# List all related transations
related_transations = client.transactions(token).related.list()
for related_transation in client.transactions(token).related.stream():
    pass
related_transations_page = client.transactions(token).related.page(start_index=0)
```

#### Users (`/users`)

```
# List all users. Default limit is 1000.
users = client.users.list()
for user in client.users.stream():
    pass
users_page = client.users.page(start_index=0)

# Retrieve a specific user
user = client.users.find(token)

# Create a user
user = client.users.create({...})

# Update a user
user = client.users.save(token, {...})

# Retrieve a specific user SSN
ssn = client.users(token).ssn()

# Retrieve a specific user Full SSN
ssn = client.users(token).ssn(full_ssn = True)

# List all children of parent user
child_cardholders = client.users(token).children.list()
for child_cardholder in client.users(token).children.stream():
    pass
child_cardholders_page = client.users(token).children.page(start_index=0)

# Search for users, if look_up data is not specified by default lists 1000 users 
users = client.users.look_up({...})
```

#### User Transitions (`/usertransitions`)

```
# Create a user transition
transition = client.users(token).transitions.create(...)

# Retrieve a specific user transition
transition = client.users(token).transitions.find(token)

# List transitions for a specific user
transitions = client.users(token).transitions.list()
for transition in client.users(token).transitions.stream():
    pass
transitions_page = client.users(token).transitions.page(start_index=0)
```

#### User Notes (`/users/{token}/notes`)

```
# List all user notes
user_notes = client.users(token).notes.list()
for user_note in client.users(token).notes.stream():
    pass
user_notes_page = client.users(token).notes.page(start_index=0)

# Create a user note
user_note = client.users(token).notes.create({...})

# Update a user note
user_note = client.users(token).notes.save(token, {...})
```

#### Velocity Controls (`/velocitycontrols`)

```
# List all velocity controls
velocity_controls = client.velocity_controls.list()
for velocity_control in client.velocity_controls.stream():
    pass
velocity_controls_page = client.velocity_controls.page(start_index=0)

# Retrieve a specific velocity control
velocity_control = client.velocity_controls.find(token)

# Create a velocity control
velocity_control = client.velocity_controls.create({...})

# Update a velocity control
velocity_control = client.velocity_controls.save(token, {...})

# List velocity controls available for a specific user
velocity_controls = list_available_for_user(user_token)
for velocity_control in stream_available_for_user(user_token):
    pass
```

#### Webhooks (`/webhooks`)

```
# List all webhooks
webhooks = client.webhooks.list()
for webhook in client.webhooks.stream():
    pass
webhooks_page = client.webhooks.page(start_index=0)

# Retrieve a specific webhook
webhook = client.webhooks.find(token)

# Create a webhook
webhook = client.webhooks.create({...})

# Update a webhook
webhook = client.webhooks.save(token, {...})

# Ping a webhook
client.webhooks(token).ping()

# Resend a webhook
client.webhooks(token).resent(event_type, event_token)
```
