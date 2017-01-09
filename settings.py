import os
import sys

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1000

# The maximum rent you want to pay per month.
MAX_PRICE = 2000

## Location preferences

# What Daft.ie areas to search on.
COUNTY = "Dublin City"
AREAS = ["Dublin 1", "Dublin 2", "Dublin 6", "Dublin 7", "Dublin 8"]

## Search type preferences

# The type of dwelling you are looking to search for,  i.e houses, properties, auction or apartments.
dwelling_type = 'apartments'
rent_or_sale = 'rent'

## System settings

# How long we should sleep between scrapes of Daft.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#daftsearch"

# The token that allows us to connect to slack.
# Should be set as an environment variable.
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

