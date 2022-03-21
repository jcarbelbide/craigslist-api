# Beautiful Soup and Requests
import json

import bs4
import pip._vendor.requests as requests
from bs4 import BeautifulSoup
from CraigslistListing import CraigslistListing
import CraigslistURLBuilder

# TODO 
# 1. Check for if there are no listings (ie listings[0] == none)
# 2. Assign a unique id to each listing
# 3. Store IDs in txt file so that between program resets, it knows which listings have already been created. 

# NOTE
# Looks like find will look inside of the contents of the html body or whatever. To parse through the attributes, you can index through like an array, but intsead of numbers, its the name of the string. 
# if not so specific (dont specify class), then find will default to finding the first instance of that thing.


def get_craigslist_listings(location, sub_location, board, starting_index, query):
    url = CraigslistURLBuilder.builder()\
        .location(location)\
        .sub_location(sub_location)\
        .board(board)\
        .starting_index(starting_index)\
        .query(query)\
        .build()
    # print(url)
    # /sfbay/all/sss/0/dirt+bike
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    listings = soup.find_all('li', class_='result-row')

    # Create empty dictionary
    craigslist_listings_list = []
    craigslist_listings_json_list = []

    for listing in listings:

        listing_master_info = listing.find('a', class_='result-title hdrlnk')
        # Implement some error catcher here.
        if listing_master_info is None:
            listing_title = None
        else:
            listing_title = listing_master_info.text

        listing_id = listing_master_info['data-id']
        # Implement some error catcher here.
        if listing_id is None:
            pass
        else:
            pass

        html_link = listing_master_info['href']
        # Implement some error catcher here.
        if html_link is None:
            pass
        else:
            pass

        price = listing.find('span', class_='result-price')
        # Implement some error catcher here.
        if price is None:
            pass
        else:
            price = price.text

        date_time = listing.find('time', class_='result-date')['datetime']
        # Implement some error catcher here.
        if date_time is None:
            pass
        else:
            pass

        location = listing.find('span', class_='result-hood')
        # Implement some error catcher here.
        if location is None:
            pass
        else:
            location = location.text

        # Create the craigslist listing object
        craigslist_listing = CraigslistListing(listing_id, html_link, listing_title, price, date_time, location)

        # Put it into the dictionary.
        craigslist_listings_list.append(craigslist_listing)

    json_list = json.dumps(craigslist_listings_list, default=lambda obj: obj.__dict__)

    # test_listing = craigslist_listings_list[0]
    # print(test_listing.date_time, test_listing.listing_title, test_listing.location, test_listing.url, test_listing.price, test_listing.unix_time)

    return json_list


if __name__ == '__main__':
    location = "sfbay"
    sub_location = "all"
    board = "sss"
    starting_index = 0
    query = "dirt bike"
    json_list = get_craigslist_listings(location, sub_location, board, starting_index, query)
    print(json_list)
