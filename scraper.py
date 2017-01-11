from daftlistings import Daft
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from util import post_listing_to_slack
from slackclient import SlackClient
import time
import settings
import sys


engine = create_engine('sqlite:///listings.db', echo=False)

Base = declarative_base()

class Daft_Listing(Base):
    """
    A table to store data on Daft listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    building_type = Column(String)
    address = Column(String)
    price = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    area = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def scrape_area(area):
    """
    Scrapes Daft for a certain area, and finds the latest listings based on certain filtering criteria
    :param area:
    :return: A list of results.
    """

    d = Daft()
    offset = 0
    pages = True

    while pages:

        daft_houses = d.get_listings(
            county=settings.COUNTY,
            area=area,
            offset=offset,
            listing_type=settings.dwelling_type,
            sale_type=settings.rent_or_sale,
            max_price=settings.MAX_PRICE,
            min_price=settings.MIN_PRICE
        )

        results = []

        if not daft_houses:
            pages = False


        for listing in daft_houses:
            foo = session.query(Daft_Listing).filter_by(link=listing.get_daft_link()).first()
            # Don't store the listing if it already exists.
            if foo is None:
        
                # Create the listing object.
                foo = Daft_Listing(
                    link=listing.get_daft_link(),
                    created=listing.get_posted_since(),
                    building_type=listing.get_dwelling_type(),
                    address=listing.get_formalised_address(),
                    price=listing.get_price(),
                    bedrooms=listing.get_num_bedrooms(),
                    bathrooms =listing.get_num_bathrooms(),
                    area=listing.get_town()
                )

                # Save the listing so we don't grab it again.
                session.add(foo)
                session.commit()

                price = listing.get_price()
                if price is not None:
                    price = price.encode('utf-8')
                    results.append([listing.get_formalised_address(),price,listing.get_num_bedrooms(),listing.get_daft_link()])

            offset += 10
        return results



def do_scrape():
    """
    Runs the scraper, and posts data to slack.
    """

    # Create a slack client.
    sc = SlackClient(settings.SLACK_TOKEN)

    # Get all the results from Daft.
    all_results = []
    for area in settings.AREAS:
        all_results += scrape_area(area)

    print("{}: Got {} results".format(time.ctime(), len(all_results)))

    # Post each result to slack.
    for result in all_results:
        post_listing_to_slack(sc, result)