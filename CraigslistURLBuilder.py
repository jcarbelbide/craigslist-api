class CraigslistURLBuilder:
    def __init__(self):
        self._location = "sfbay"
        self._sub_location = ""
        self._board = "sss"
        self._starting_index = '0'
        self._query = "none"

    def location(self, location):
        self._location = location
        return self

    def sub_location(self, sub_location):
        self._sub_location = sub_location
        return self

    def _format_sub_location(self):
        if self._sub_location == "all":
            return ""
        else:
            return f"/%s" % self._sub_location

    def board(self, board):
        self._board = board
        return self

    def starting_index(self, starting_index):
        self._starting_index = starting_index
        return self

    def _format_starting_index(self):
        if str(self._starting_index) == '0':
            return ""
        else:
            return f"s=%s&" % self._starting_index

    def query(self, query):
        self._query = query
        return self

    def _format_query(self):
        return self._query.replace(" ", "+")

    def build(self):
        return f"https://%s.craigslist.org/search%s/%s?%squery=%s" % (self._location, self._format_sub_location(), self._board, self._format_starting_index(), self._format_query())


def builder():
    return CraigslistURLBuilder()


# Examples
# https://sfbay.craigslist.org/search/sss?s=120&query=dirt%20bike
# https://sfbay.craigslist.org/search/eby/sss?query=dirt+bike
# https://sfbay.craigslist.org/search/sss?query=dirt+bike
