import settings
import sys

def post_listing_to_slack(sc, listing):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = "{0} | {1} | {2} | <{3}>".format(listing[0], listing[1], listing[2], listing[3])
    sc.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL, text=desc,
        username='HousingBot', icon_emoji=':robot_face:'
    )
