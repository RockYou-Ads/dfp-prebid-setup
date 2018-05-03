import logging
import os
import pprint

from googleads import dfp

from dfp.client import get_client

logger = logging.getLogger(__name__)


def create_creatives(creatives):
    """
    Creates creatives in DFP.

    Args:
      creatives (arr): an array of objects, each a creative configuration
    Returns:
      an array: an array of created creative IDs
    """
    dfp_client = get_client()
    creative_service = dfp_client.GetService('CreativeService',
                                             version='v201802')
    creatives = creative_service.createCreatives(creatives)

    # Return IDs of created line items.
    created_creative_ids = []
    for creative in creatives:
        created_creative_ids.append(creative['id'])
        logger.info(u'Created creative with name "{name}".'.format(
            name=creative['name']))
    return created_creative_ids


def create_vast_creative_config(name, advertiser_id, vast_url):
    # https://developers.google.com/doubleclick-publishers/docs/reference/v201802/CreativeService.Creative

    # vast_url = settings.VAST_URL_DEFAULT

    config = {
        'xsi_type': 'VastRedirectCreative',
        'name': name,
        'advertiserId': advertiser_id,
        'size': {
            'width': '1',
            'height': '1'
        },
        'vastXmlUrl': vast_url,
        'duration': 15000,
        # # https://github.com/prebid/Prebid.js/issues/418
        # 'isSafeFrameCompatible': False,
    }

    return config

def create_banner_creative_config(name, advertiser_id):
    """
    Creates a creative config object.

    Args:
      name (str): the name of the creative
      advertiser_id (int): the ID of the advertiser in DFP
    Returns:
      an object: the line item config
    """

    snippet_file_path = os.path.join(os.path.dirname(__file__),
                                     'creative_snippet.html')
    with open(snippet_file_path, 'r') as snippet_file:
        snippet = snippet_file.read()

    # https://developers.google.com/doubleclick-publishers/docs/reference/v201802/CreativeService.Creative
    config = {
        'xsi_type': 'ThirdPartyCreative',
        'name': name,
        'advertiserId': advertiser_id,
        'size': {
            'width': '1',
            'height': '1'
        },
        'snippet': snippet,
        # https://github.com/prebid/Prebid.js/issues/418
        'isSafeFrameCompatible': False,
    }

    return config


def build_creative_name(bidder_code, order_base, creative_num, is_vast=False):
    """
    Returns a name for a creative.

    Args:
      bidder_code (str): the bidder code for the header bidding partner
      order_base (dict): the name of the order in DFP
      creative_num (int): the num_creatives distinguising this creative from any
        duplicates
    Returns:
      a string
    """
    vast_decorator = '[v]' if is_vast else ''

    format_string = '{bidder_code}: HB {order_name}, #{num}{vast}'
    if bidder_code is None:
        format_string = 'HB {order_name}, #{num}{vast}'

    return format_string.format(
        bidder_code=bidder_code,
        order_name=order_base['name'],
        num=creative_num,
        vast=vast_decorator,
    )


def create_duplicate_creative_configs(bidder_code, order_base, advertiser_id,
                                      vast_url,
                                      num_creatives=1):
    """
    Returns an array of creative config object.

    Args:
      bidder_code (str): the bidder code for the header bidding partner
      order_base (dict): the name of the order in DFP
      advertiser_id (int): the ID of the advertiser in DFP
      vast_url (str): the vast URL to populate video creatives with
      num_creatives (int): how many creative configs to generate
    Returns:
      an array: an array of length `num_creatives`, each item a line item config
    """
    creative_configs = []
    vast_configs = []
    for creative_num in range(1, num_creatives + 1):
        config = create_banner_creative_config(
            name=build_creative_name(bidder_code, order_base, creative_num),
            advertiser_id=advertiser_id,
        )
        creative_configs.append(config)

        vast = create_vast_creative_config(
            name=build_creative_name(bidder_code, order_base, creative_num,
                                     is_vast=True),
            advertiser_id=advertiser_id,
            vast_url=vast_url
        )
        vast_configs.append(vast)

    return {
        'banner': creative_configs,
        'vast': vast_configs
    }
