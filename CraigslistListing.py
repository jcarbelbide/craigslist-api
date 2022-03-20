import datetime
import json
from time import mktime


class CraigslistListing:

    def __init__(self, listing_id, url, listing_title, price, date_time, location):
        # Class attributes
        self.listing_id = listing_id
        self.listing_title = listing_title
        self.url = url
        self.price = price
        self.date_time = date_time
        self.unix_time = self._calculate_unix_time()
        self.location = location

    def to_json(self):
        return json.dumps(self.__dict__)

    def _calculate_unix_time(self):
        # ts = ciso8601.parse_datetime(self.date_time)
        datetime_split = str.split(self.date_time)
        date_split = str.split(datetime_split[0], '-')
        year = int(date_split[0])
        month = int(date_split[1])
        day = int(date_split[2])
        time_split = str.split(datetime_split[1], ':')
        hour = int(time_split[0])
        minute = int(time_split[1])

        ts = datetime.datetime(year, month, day, hour, minute)
        return int(mktime(ts.timetuple()))
