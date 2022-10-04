#By Josh Sternfeld
from random import randint
from lithic import *

# API Endpoint vars
lithic = Lithic(
  api_key="REPLACE YOUR OWN KEY",
  environment="sandbox",
)

# Random values to fuck with
amount_value = randint(20, 1000)
store = "ToysRUs"

# Lists the cards on account based off of api_key
def list_cards():
    page = lithic.cards.list()
    card = page.data[0]
    print(card.created)
    print(page)

# Function to create cards
def create_card():
    card = lithic.cards.create({
        "memo": "test 2",
        "type": "VIRTUAL",
    })
    return card

# Function to create transactions
def create_transactions():
    transaction = lithic.transactions.simulate_authorization({
        "amount": amount_value,
        "descriptor": store,
        "pan": "4111111289144142",
        "status": "AUTHORIZATION",
        "merchant_currency": "USD",
    })


#####################################################################################
# Uncomment to enact the above functions

# create_card()
# create_transactions()
# list_cards()
