import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLEADS_YAML_FILE = os.path.join(ROOT_DIR, 'googleads.yaml')

#########################################################################
# DFP SETTINGS
#########################################################################

# A string describing the order
DFP_ORDER_NAME = 'RY Test Order Q6'

# The email of the DFP user who will be the trafficker for
# the created order
DFP_USER_EMAIL_ADDRESS = # Replace this

# The exact name of the DFP advertiser for the created order
DFP_ADVERTISER_NAME = 'RY Dev Testing'

# Names of placements the line items should target.
DFP_TARGETED_PLACEMENT_NAMES = [
    'talon'
]

# Sizes of placements. These are used to set line item and creative sizes.
DFP_PLACEMENT_SIZES = [
    {
        'width': '1',
        'height': '1'
    },
    {
        'width': '88',
        'height': '31'
    },
    {
        'width': '120',
        'height': '20'
    },
    {
        'width': '120',
        'height': '60'
    },
    {
        'width': '120',
        'height': '90'
    },
    {
        'width': '120',
        'height': '240'
    },
    {
        'width': '120',
        'height': '600'
    },
    {
        'width': '125',
        'height': '125'
    },
    {
        'width': '180',
        'height': '150'
    },
    {
        'width': '160',
        'height': '600'
    },
    {
        'width': '200',
        'height': '200'
    },
    {
        'width': '234',
        'height': '60'
    },
    {
        'width': '240',
        'height': '400'
    },
    {
        'width': '250',
        'height': '250'
    },
    {
        'width': '300',
        'height': '50'
    },
    {
        'width': '300',
        'height': '100'
    },
    {
        'width': '300',
        'height': '250'
    },
    {
        'width': '300',
        'height': '600'
    },
    {
        'width': '320',
        'height': '50'
    },
    {
        'width': '320',
        'height': '100'
    },
    {
        'width': '336',
        'height': '280'
    },
    {
        'width': '400',
        'height': '300'
    },
    {
        'width': '402',
        'height': '302'
    },
    {
        'width': '406',
        'height': '306'
    },
    {
        'width': '468',
        'height': '60'
    },
    {
        'width': '500',
        'height': '350'
    },
    {
        'width': '690',
        'height': '390'
    },
    {
        'width': '720',
        'height': '480'
    },
    {
        'width': '728',
        'height': '90'
    },
    {
        'width': '970',
        'height': '90'
    },
    {
        'width': '970',
        'height': '250'
    },
]

# Whether we should create the advertiser in DFP if it does not exist.
# If False, the program will exit rather than create an advertiser.
DFP_CREATE_ADVERTISER_IF_DOES_NOT_EXIST = False

# If settings.DFP_ORDER_NAME is the same as an existing order, add the created 
# line items to that order. If False, the program will exit rather than
# modify an existing order.

# SET TO TRUE for fixes

DFP_USE_EXISTING_ORDER_IF_EXISTS = True

# Optional
# Each line item should have at least as many creatives as the number of 
# ad units you serve on a single page because DFP specifies:
#   "Each of a line item's assigned creatives can only serve once per page,
#    so if you want the same creative to appear more than once per page,
#    copy the creative to associate multiple instances of the same creative."
# https://support.google.com/dfp_sb/answer/82245?hl=en
#
# This will default to the number of placements specified in
# `DFP_TARGETED_PLACEMENT_NAMES`.
DFP_NUM_CREATIVES_PER_LINE_ITEM = 10

# Optional
# The currency to use in DFP when setting line item CPMs. Defaults to 'USD'.
# DFP_CURRENCY_CODE = 'USD'

#########################################################################
# PREBID SETTINGS
#########################################################################

PREBID_BIDDER_CODE = None

# Price buckets. This should match your Prebid settings for the partner. See:
# http://prebid.org/dev-docs/publisher-api-reference.html#module_pbjs.setPriceGranularity
# FIXME: this should be an array of buckets. See:
# https://github.com/prebid/Prebid.js/blob/8fed3d7aaa814e67ca3efc103d7d306cab8c692c/src/cpmBucketManager.js
PREBID_PRICE_BUCKETS = {
    'precision': 2,
    'min': .01,
    'max': 1,
    'increment': 0.01,
}

# Run ~ 10 at a time to reduce load on the remote servers and allow incremental
# runs.. takes several hours for 0-100
PREBID_ORDER_BUCKETS = {
    'min': 0,
    'max': 11,
    'increment': 1.0,
}

VAST_URL_DEFAULT = 'https://invalidvast.rockyou.net'

#########################################################################

# Try importing local settings, which will take precedence.
try:
    from local_settings import *
except ImportError:
    pass
